# Validation Tables

## Architecture validation

| Check | Required | Pass/Fail | Notes |
|---|---:|---|---|
| Module responsibilities are distinct | Yes |  |  |
| Domain/application logic depends on abstractions | Yes |  |  |
| External SDKs/APIs are isolated behind adapters | Yes |  |  |
| Interfaces are not overly broad | Yes |  |  |
| Extension points avoid direct modification of core logic | Yes |  |  |
| Error handling and retries are defined | Yes |  |  |

## Delivery validation

| Check | Required | Pass/Fail | Notes |
|---|---:|---|---|
| TPM can convert plan to epics and milestones | Yes |  |  |
| Engineering can identify implementation modules | Yes |  |  |
| Dependencies and sequencing are clear | Yes |  |  |
| Acceptance criteria are measurable | Yes |  |  |
| Risks have mitigation or owners | Yes |  |  |
| Open questions are separated from tasks | Yes |  |  |

## Self-heal validation

| Check | Required | Pass/Fail | Notes |
|---|---:|---|---|
| Dedicated self-heal instructions exist | Yes |  |  |
| Compiled instructions mention self-heal | Yes |  |  |
| Manifest records self-heal status | Yes |  |  |
| Final output validates handoff readiness | Yes |  |  |