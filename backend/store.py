from collections import defaultdict
from typing import Any

from models import AuditEvent


SCANS: dict[str, dict[str, Any]] = {}
POLICIES: dict[str, dict[str, Any]] = defaultdict(dict)
AUDIT_LOG: list[AuditEvent] = []
APPROVALS: dict[str, dict[str, Any]] = {}
