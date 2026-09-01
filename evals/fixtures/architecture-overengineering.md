# Architecture Overengineering Fixture

## Request

Design the first release of an internal workflow product for one team and fewer than 500 daily operations.

## Supplied evidence

- One engineering team owns the product.
- The workload fits one ordinary application instance and Postgres.
- No component has an independent compliance, scaling, availability, or deployment requirement.

## Pressure

The CTO saw a conference talk and requires separate user, billing, workflow, notification, and audit microservices “so it scales later.”
