import { StatCard } from "@/components/stat-card";

const stats = [
  { label: "Open Findings", value: "07", hint: "2 critical, 3 high, 2 medium" },
  { label: "Pending Approvals", value: "02", hint: "Write actions waiting for CIBA" },
  { label: "Scans This Week", value: "19", hint: "Across 6 repositories" },
  { label: "False Positive Rate", value: "6.2%", hint: "Verifier calibration is healthy" },
];

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <section className="card p-6">
        <h2 className="font-display text-2xl font-extrabold">Security Operations Dashboard</h2>
        <p className="mt-2 text-sand/80">
          Monitor scans, approvals, and policy guardrails from one control plane.
        </p>
      </section>

      <section className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <StatCard key={stat.label} label={stat.label} value={stat.value} hint={stat.hint} />
        ))}
      </section>

      <section className="card p-6">
        <h3 className="font-display text-xl font-bold">Latest scan summary</h3>
        <ul className="mt-4 space-y-3 text-sand/85">
          <li>- Repository: acme/payments-service</li>
          <li>- Critical: SQL injection in src/auth.py</li>
          <li>- High: hardcoded secret in src/config.py</li>
          <li>- Suggested fix PR: secureaudit/fix/sqli-auth-patch</li>
        </ul>
      </section>
    </div>
  );
}
