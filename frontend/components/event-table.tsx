type EventItem = {
  timestamp: string;
  agent: string;
  action: string;
  repo: string;
};

type EventTableProps = {
  items: EventItem[];
};

export function EventTable({ items }: EventTableProps) {
  return (
    <div className="card overflow-hidden">
      <table className="w-full border-collapse text-left text-sm">
        <thead className="bg-white/5 text-sand/80">
          <tr>
            <th className="px-4 py-3">Timestamp</th>
            <th className="px-4 py-3">Agent</th>
            <th className="px-4 py-3">Action</th>
            <th className="px-4 py-3">Repo</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={`${item.timestamp}-${index}`} className="border-t border-white/10">
              <td className="px-4 py-3 text-sand/70">{new Date(item.timestamp).toLocaleString()}</td>
              <td className="px-4 py-3 font-semibold">{item.agent}</td>
              <td className="px-4 py-3 text-mint">{item.action}</td>
              <td className="px-4 py-3">{item.repo}</td>
            </tr>
          ))}
          {items.length === 0 && (
            <tr>
              <td className="px-4 py-8 text-center text-sand/65" colSpan={4}>
                No events yet. Run a scan to populate the audit trail.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
