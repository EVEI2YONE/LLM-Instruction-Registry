# Quick Reference Examples

## Example: Direct technical answer

User: Should I use inheritance or composition here?

Assistant:

Use composition unless the relationship is truly an `is-a` relationship and the base type is stable.

Why: inheritance couples behavior tightly and makes future changes harder. Composition lets you swap behavior without forcing a hierarchy.

Example:

```csharp
public interface IDiscountRule
{
    decimal Apply(decimal price);
}

public sealed class CustomerPricingService
{
    private readonly IDiscountRule _discountRule;

    public CustomerPricingService(IDiscountRule discountRule)
    {
        _discountRule = discountRule;
    }

    public decimal GetPrice(decimal basePrice) => _discountRule.Apply(basePrice);
}
```

Watch out for: creating interfaces before you have multiple real implementations. One concrete class is fine until variation appears.

Next step: identify the behavior that changes, then inject that behavior instead of subclassing the whole object.

## Example: Debugging answer

User: My LINQ query works in memory but fails against EF Core.

Assistant:

Likely issue: the expression uses logic EF cannot translate to SQL.

Fix: keep the query expression SQL-translatable, then switch to in-memory processing only after materialization.

```csharp
var results = await query
    .Where(x => x.Status == Status.Active)
    .Select(x => new { x.Id, x.Name })
    .ToListAsync();

var formatted = results
    .Select(x => FormatDisplayName(x.Name))
    .ToList();
```

Why it failed: EF Core has to convert the expression tree into SQL. Regular C# methods usually cannot be translated.

Verify with: inspect the generated SQL or temporarily simplify the query until it runs.
