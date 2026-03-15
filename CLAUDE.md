# CLAUDE.md

Development rules for this project. Every rule here exists because omitting it causes mistakes.

---

## Tests

ALWAYS write the test file before the implementation file. This is non-negotiable.

```
auth.test.ts  ->  auth.ts       (correct)
auth.ts  ->  auth.test.ts       (never)
```

- Mirror source paths: `src/users/users.service.ts` -> `src/users/users.service.test.ts`
- Cover: happy path, edge cases, error cases
- Use `it('should ...')` phrasing — describe behavior, not implementation
- Run the single relevant test file, not the whole suite

---

## File size

No file exceeds 600 lines. If approaching 500, split now.

Split strategies:
- Multiple concerns in one file -> separate by responsibility (`.service`, `.repository`, `.validator`, `.types`)
- Long conditionals -> replace with a strategy map or registry
- Shared helpers growing large -> extract to a dedicated `utils/` sub-module

---

## Structure

```
src/
  <domain>/
    <domain>.service.ts       # business logic only
    <domain>.repository.ts    # data access only
    <domain>.controller.ts    # HTTP entry point only
    <domain>.types.ts         # interfaces, DTOs, enums
    <domain>.service.test.ts
    <domain>.repository.test.ts
    index.ts                  # public exports only
  shared/
    utils/
    errors/
    types/
```

Each `index.ts` exports the public API. Internal helpers are not exported.

---

## Functions

- Max 20 lines per function. Extract if longer.
- Max 3 parameters. Use an options object beyond that.
- Return early to avoid nesting.

```ts
// correct
function process(order: Order): Result {
  if (!order) return { error: 'missing order' };
  if (!order.items.length) return { error: 'empty order' };
  return fulfill(order);
}
```

---

## Naming

| Target | Convention |
|---|---|
| Files | `kebab-case.ts` |
| Classes / Types / Interfaces | `PascalCase` |
| Functions / variables | `camelCase` |
| Constants | `UPPER_SNAKE_CASE` |
| Booleans | `isX`, `hasX`, `canX`, `shouldX` |

No magic values. Name every constant.

```ts
// wrong
setTimeout(fn, 86400000);

// correct
const ONE_DAY_MS = 24 * 60 * 60 * 1000;
setTimeout(fn, ONE_DAY_MS);
```

---

## Documentation

Every file needs a header:
```ts
/**
 * @file users.service.ts
 * @description Business logic for user management.
 */
```

Every exported function needs JSDoc:
```ts
/**
 * Returns a user by ID, or null if not found.
 * @throws {DatabaseError} on query failure
 */
export async function getUserById(id: string): Promise<User | null> {}
```

Comments explain WHY, not WHAT:
```ts
// Retry 3x — provider returns 503 intermittently under load
for (let i = 0; i < 3; i++) { ... }
```

---

## Error handling

Never swallow errors silently. Always include context.

```ts
// correct
try {
  await processPayment(order);
} catch (error) {
  logger.error('Payment failed', { orderId: order.id, error });
  throw new PaymentError('Payment failed', { cause: error });
}

// wrong
try {
  await processPayment(order);
} catch (_) {}
```

---

## Git

- One logical change per commit.
- Format: `type(scope): description` — e.g. `feat(auth): add OAuth2 flow`
- Never commit commented-out code or debug logs.

---

## Pre-commit checklist

- [ ] Test file written before implementation
- [ ] All tests pass
- [ ] No file exceeds 500 lines
- [ ] All exports have JSDoc
- [ ] All files have a header comment
- [ ] No magic numbers or strings
- [ ] No silent error catches
- [ ] Module is exported from `index.ts`
