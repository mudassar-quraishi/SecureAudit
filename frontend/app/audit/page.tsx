import { EventTable } from "@/components/event-table";

const sampleEvents = [
  {
    timestamp: new Date().toISOString(),
    agent: "parser",
    action: "READ",
    repo: "acme/payments-service",
  },
  {
    timestamp: new Date(Date.now() - 20_000).toISOString(),
    agent: "detector",
    action: "ANALYZE",
    repo: "acme/payments-service",
  },
  {
    timestamp: new Date(Date.now() - 40_000).toISOString(),
    agent: "verifier",
    action: "APPROVAL_REQUEST",
    repo: "acme/payments-service",
  },
];

export default function AuditPage() {
  return (
    <div className="space-y-6">
      <section className="card p-6">
        <h2 className="font-display text-2xl font-extrabold">Immutable Audit Trail</h2>
        <p className="mt-2 text-sand/80">
          Every action is logged with actor identity, permission scope, and action metadata.
        </p>
      </section>
      <EventTable items={sampleEvents} />
    </div>
  );
}
