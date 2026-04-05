# Judging Criteria Mapping

## Security model
- Token Vault exchange with short-lived scoped tokens.
- CIBA step-up for write operations.
- FGA policy checks before file and repo actions.

## User control
- Policy editor for path/action boundaries.
- Explicit approval prompts with action context.
- Immutable audit timeline per user and repo.

## Technical execution
- FastAPI backend with modular auth and agent layers.
- Structured scan pipeline with parser, detector, verifier, fixer.
- Database schema for scans, findings, approvals, and audit events.

## Design
- Distinct dashboard UI with scan summary, policy controls, and audit views.
- Responsive app structure suitable for demo and production expansion.

## Potential impact
- Reduces security review toil.
- Encourages safer default architecture for all AI agents.
- Transfers to high-trust domains beyond software security.

## Insight value
- Documents architecture shifts introduced by token custody separation.
- Highlights practical trade-offs in multi-agent authorization.
