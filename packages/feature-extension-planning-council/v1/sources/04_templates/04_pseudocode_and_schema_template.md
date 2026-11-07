# Pseudocode and Schema Template

## Interface contracts

```ts
interface FeatureExtensionUseCase<Input, Output> {
  execute(input: Input, context: ExecutionContext): Promise<Output>;
}

interface PermissionPolicy {
  canExecute(action: ExtensionAction, actor: ActorContext, resource: ResourceContext): boolean;
}

interface StoragePort<RecordType> {
  get(id: string): Promise<RecordType | null>;
  save(record: RecordType): Promise<void>;
  delete(id: string): Promise<void>;
}

interface PlatformAdapter {
  readHostContext(): Promise<HostContext>;
  invokePlatformAction(action: PlatformAction): Promise<PlatformResult>;
}
```

## Command schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ExtensionCommand",
  "type": "object",
  "required": ["commandId", "type", "actor", "payload", "requestedAt"],
  "properties": {
    "commandId": { "type": "string" },
    "type": { "type": "string" },
    "actor": { "$ref": "#/definitions/ActorContext" },
    "payload": { "type": "object" },
    "requestedAt": { "type": "string", "format": "date-time" }
  },
  "definitions": {
    "ActorContext": {
      "type": "object",
      "required": ["actorId", "roles"],
      "properties": {
        "actorId": { "type": "string" },
        "roles": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

## Event schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ExtensionEvent",
  "type": "object",
  "required": ["eventId", "eventType", "occurredAt", "source", "data"],
  "properties": {
    "eventId": { "type": "string" },
    "eventType": { "type": "string" },
    "occurredAt": { "type": "string", "format": "date-time" },
    "source": { "type": "string" },
    "correlationId": { "type": "string" },
    "data": { "type": "object" }
  }
}
```

## Lifecycle pseudocode

```pseudo
function handleExtensionRequest(request, context): Result
    validate request shape
    actor = resolveActor(context)
    hostContext = platformAdapter.readHostContext()

    if not permissionPolicy.canExecute(request.action, actor, hostContext.resource):
        audit.logDeniedAttempt(actor, request.action, hostContext.resource)
        return ForbiddenResult()

    command = commandFactory.fromRequest(request, actor, hostContext)
    result = commandBus.dispatch(command)

    if result.success:
        eventBus.publish(result.domainEvents)
        telemetry.trackSuccess(command.type, result.metrics)
    else:
        telemetry.trackFailure(command.type, result.error)

    return presenter.format(result)
```

## Error model

```ts
type ExtensionError =
  | { kind: "ValidationError"; field: string; message: string }
  | { kind: "PermissionDenied"; action: string; resourceId?: string }
  | { kind: "ExternalDependencyFailure"; dependency: string; retryable: boolean }
  | { kind: "Conflict"; resourceId: string; currentVersion: string }
  | { kind: "UnexpectedError"; correlationId: string };
```