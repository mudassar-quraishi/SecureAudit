# Building SecureAudit: Zero-Trust GitHub Automation with Token Vault

## The challenge
AI agents are becoming operational coworkers, but most are built on a fragile trust model: long-lived tokens in app runtime and broad scopes that are hard to monitor. In security tooling, this is especially dangerous because a compromised agent can become a privileged attacker.

## The pattern: capability without custody
SecureAudit adopts a stronger architecture where agents can perform useful work without custody of user credentials. Auth0 Token Vault stores GitHub connected-account tokens. The agent runtime never receives a refresh token. Instead, it exchanges a signed assertion for a short-lived access token with narrow scope and immediate expiry.

## Why CIBA changed the product
Write actions are where risk concentrates. We used CIBA to gate these actions asynchronously. The agent requests approval, the user approves on a second factor device, and only then can execution continue. This keeps autonomous flow while preserving explicit human authority.

## Fine-grained authorization in practice
OpenFGA policies let users define what the system can touch:
- Read from source directories.
- Never access secret material.
- Auto-approve low-risk operations.
- Escalate high-risk writes for approval.

This policy layer turned vague trust settings into concrete, testable rules.

## Takeaways
- Token Vault reduces blast radius by design.
- Multi-agent systems need per-agent permission boundaries.
- Async approval is critical for balancing autonomy and control.
- Transparent audit logs are required for real trust.

SecureAudit demonstrates a practical model for secure AI action, not just secure AI analysis.
