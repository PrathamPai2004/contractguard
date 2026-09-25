# ContractGuard

ContractGuard is a developer tool for **FastAPI applications** that helps you detect and manage API contract changes.

It generates your application's OpenAPI schema, stores a baseline contract, and compares future changes against that baseline so you can identify breaking API changes before they reach production.

## Why ContractGuard?

APIs evolve constantly.

You add a new endpoint, rename a response field, change a parameter, modify a request body, or remove an endpoint.

The problem is that some of these changes can silently break existing clients.

ContractGuard helps you answer:

> "Did my API contract change?"

and more importantly:

> "Did I accidentally introduce a breaking change?"

---

## Features

- Generate OpenAPI schema from a FastAPI application
- Initialize an API contract baseline
- Compare the current API schema with the stored contract
- Detect API contract changes
- Check contracts from the command line
- Update the stored contract after intentional changes
- Generate API documentation
- Designed specifically for FastAPI projects
- Simple CLI workflow

---

-- TO BE LAUNCHED SOON
