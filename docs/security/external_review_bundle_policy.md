# External Review Bundle Policy

A review bundle is a minimal context package prepared for external model review, such as ChatGPT.

## Allowed

- Architecture summary
- Redacted code excerpts
- File tree excerpts
- Test results
- Error messages with secrets removed
- Proposed implementation plan
- Specific questions for reviewer

## Not allowed

- Raw private datasets
- Full chat exports with personal data
- Full production logs
- Secrets, tokens, cookies, keys
- Private media
- Database dumps

## Principle

Send enough context to review the decision, not enough context to reconstruct private data.
