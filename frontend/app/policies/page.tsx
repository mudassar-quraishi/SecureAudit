export default function PoliciesPage() {
  return (
    <div className="space-y-6">
      <section className="card p-6">
        <h2 className="font-display text-2xl font-extrabold">Policy Editor</h2>
        <p className="mt-2 text-sand/80">
          Define file-level permissions and approval behavior for each risk tier.
        </p>
      </section>

      <section className="grid gap-4 md:grid-cols-2">
        <div className="card p-5">
          <h3 className="font-display text-lg font-bold">Path boundaries</h3>
          <ul className="mt-3 space-y-2 text-sand/85">
            <li>- Allow read: src/**, tests/**</li>
            <li>- Allow write: .github/ISSUE_TEMPLATE/**</li>
            <li>- Deny all: secrets/**, **/.env*</li>
          </ul>
        </div>

        <div className="card p-5">
          <h3 className="font-display text-lg font-bold">Approval rules</h3>
          <ul className="mt-3 space-y-2 text-sand/85">
            <li>- LOW and MEDIUM: auto-approve issue creation</li>
            <li>- HIGH and CRITICAL: require CIBA + MFA</li>
            <li>- Any repo write: always request explicit approval</li>
          </ul>
        </div>
      </section>
    </div>
  );
}
