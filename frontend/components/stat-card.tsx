type StatCardProps = {
  label: string;
  value: string;
  hint: string;
};

export function StatCard({ label, value, hint }: StatCardProps) {
  return (
    <div className="card animate-rise p-5">
      <p className="text-xs uppercase tracking-[0.15em] text-sand/65">{label}</p>
      <p className="mt-2 font-display text-3xl font-bold text-sand">{value}</p>
      <p className="mt-3 text-sm text-sand/75">{hint}</p>
    </div>
  );
}
