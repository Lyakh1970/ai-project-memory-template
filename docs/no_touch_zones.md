# No-Touch Zones

Areas that agents must not modify, read, export, or upload unless explicitly instructed.

## Never commit

- Secrets, tokens, API keys, passwords, cookies, private keys.
- Raw production exports.
- Private media.
- Customer/client confidential data.
- Authentication state files.

## Project-specific forbidden paths

Add project-specific paths here after applying the template.

Example:

```text
data/private/
data/raw_exports/
media/private/
.env
```

## Risky operations requiring explicit human approval

- Database schema changes.
- Data migrations.
- Deletes or destructive cleanups.
- External service integration changes.
- Large refactors.
- Authentication/authorization changes.
- Changes involving money, billing, quotas, legal, or compliance responsibility.
