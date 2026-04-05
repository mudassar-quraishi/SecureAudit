# SecureAudit 3-Minute Demo Script

## 0:00 - 0:30: Problem
- Most AI agents use long-lived tokens in environment files.
- If leaked, attackers gain broad repository access.
- Users cannot see or control what the agent is doing.

## 0:30 - 1:00: Architecture
- SecureAudit uses Auth0 Token Vault as the credential custody layer.
- The agent requests short-lived scoped tokens only for specific actions.
- Any write operation is blocked behind CIBA step-up approval.

## 1:00 - 1:45: Live scan
- Open dashboard and run a scan for a sample repo.
- Show parser, detector, verifier pipeline output.
- Highlight a critical finding and generated patch proposal.

## 1:45 - 2:15: Approval
- Trigger issue or PR creation from a finding.
- Show pending approval state.
- Approve from mobile push, then continue execution.

## 2:15 - 2:45: Audit trail
- Open audit page.
- Show read, analyze, approval_request, and write events in sequence.
- Explain each action is tied to user identity and policy boundary.

## 2:45 - 3:00: Close
- Emphasize capability without custody, explicit user control, and full transparency.
- Mention portability to finance, health, and legal AI agents.
