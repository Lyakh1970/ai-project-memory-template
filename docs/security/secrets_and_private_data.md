# Secrets and Private Data Policy

## Never commit

- Passwords
- API keys
- Access tokens
- Refresh tokens
- Cookies
- Private keys
- VPN configuration with credentials
- `.env` files
- Browser/session auth state
- Raw customer data
- Raw production exports
- Private media

## Redaction rule

If a secret-like value is needed for context, replace it with a placeholder:

```text
<REDACTED_API_KEY>
<REDACTED_PASSWORD>
<REDACTED_EMAIL>
<REDACTED_PHONE>
```

## Reporting rule

If Codex finds a secret-like value, it must report only:

- file path
- line number if safe
- type of finding

It must not print or copy the secret value.
