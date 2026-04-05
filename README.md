# SecureAudit: Zero-Trust GitHub Security Auditor

SecureAudit is an autonomous, human-controlled GitHub security auditor built for the Auth0 Authorized to Act challenge. It uses Auth0 Token Vault for credential custody, CIBA for step-up approval, and OpenFGA for fine-grained policy enforcement.

## Why this architecture wins

- Capability without custody: the agent never stores or sees long-lived GitHub tokens.
- Human in the loop: every write operation is blocked behind explicit user approval.
- Complete auditability: every action is logged with actor, scope, result, and trace id.
- Bounded autonomy: agents are specialized by role and permission boundary.

## Monorepo structure

- frontend: Next.js dashboard, policy editor, audit viewer
- backend: FastAPI API, auth integration layer, LangGraph workflow
- prisma: database schema for audit logs, policies, scans, findings
- docs: demo script, blog outline, judging matrix

## Quick start

### 1) Prerequisites

- Node.js 20+
- Python 3.11+
- PostgreSQL 15+
- Auth0 tenant configured for AI Agent features

### 2) Copy environment files

- Copy .env.example to .env
- Copy backend/.env.example to backend/.env
- Copy frontend/.env.example to frontend/.env.local

### 3) Start local dependencies

Use Docker if desired:

- docker compose up -d

### 4) Backend setup

- cd backend
- python -m venv .venv
- .venv\\Scripts\\activate
- pip install -r requirements.txt
- uvicorn main:app --reload --port 8000

### 5) Frontend setup

- cd frontend
- npm install
- npm run dev

Open http://localhost:3000

## Core flows

### Scan flow

1. User triggers scan for a repo.
2. Parser agent fetches repository tree and file snapshots.
3. Detector agent finds vulnerabilities and logic bugs.
4. Verifier agent validates findings and filters false positives.
5. Fixer agent creates patches for approved findings.
6. Write actions require CIBA approval before issue or PR creation.

### Approval flow (CIBA)

1. Agent submits action payload for approval.
2. User gets a push prompt with action details.
3. User approves or denies with MFA.
4. Backend receives authorization result and proceeds or aborts.

### Token flow (Token Vault)

1. Agent signs client assertion with private key.
2. Backend exchanges assertion and user subject for short-lived token.
3. Agent executes one API call with least-privilege scope.
4. Token is discarded immediately after use.

## What is implemented in this starter

- FastAPI endpoints for scans, policies, audit logs, and approvals.
- LangGraph-style state pipeline with parser, detector, verifier, fixer nodes.
- Auth modules for token exchange, CIBA request, and FGA check interfaces.
- Next.js dashboard pages for scans, policy controls, and immutable audit feed UI.
- Prisma schema for users, connected accounts, findings, approvals, and audit events.

## What to build next

- Wire real Auth0 tenant values and Token Vault exchange endpoint.
- Replace mock detector with Groq and Gemini model adapters.
- Add GitHub App or OAuth connected-account onboarding flow.
- Implement branch creation, patch apply, and PR creation with approval gating.
- Add signed immutable audit storage and tamper-evidence strategy.

## Submission checklist

- Public repository with setup and architecture docs
- 3-minute demo video showing scan -> approval -> PR
- Live deployed frontend and backend
- Blog post on Token Vault lessons and architecture trade-offs
