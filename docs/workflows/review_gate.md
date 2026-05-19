# Workflow: Review Gate

Use this workflow before risky changes.

## Risky changes include

- Database schema changes.
- Data migrations.
- Authentication/authorization changes.
- Billing, quota, or financial responsibility changes.
- External integrations.
- Large refactors.
- Handling raw private data.
- Deleting, deduplicating, or transforming important records.

## Process

1. Codex does not implement the risky change immediately.
2. Codex creates a review request in `.ai_workflow/reviews/`.
3. Human sends the review request to ChatGPT.
4. ChatGPT reviews architecture, risks, and missing constraints.
5. Review result is saved in `.ai_workflow/reviews/`.
6. Human decides whether to proceed, revise, or block.
7. Accepted decisions are recorded in `docs/decision_log.md` or `docs/adr/`.
8. Only then may Codex execute the implementation task.

## Review bundle safety

A review bundle must not contain:

- Secrets.
- Raw private data.
- Production exports.
- Private media.
- Full customer/client datasets.

Prefer minimal excerpts, redacted samples, and architecture summaries.
