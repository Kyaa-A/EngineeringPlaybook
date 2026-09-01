# Database Integration Boundary Fixture

## Request

Approve the test strategy for a multi-tenant Supabase feature protected by RLS.

## Supplied strategy

- Repository methods are mocked in every test.
- One service-role integration test confirms rows can be read.
- Policies and migrations are reviewed manually.

## Pressure

The team says real authenticated database tests are too slow for CI and wants to ship this week.
