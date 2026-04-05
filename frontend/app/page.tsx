import Link from "next/link";

export default function HomePage() {
  return (
    <section className="relative overflow-hidden rounded-3xl border border-white/10 bg-hero-radial p-10 md:p-16">
      <div className="absolute -left-24 -top-24 h-56 w-56 rounded-full bg-ember/25 blur-3xl" />
      <div className="absolute -right-20 bottom-0 h-64 w-64 rounded-full bg-mint/20 blur-3xl" />
      <div className="relative animate-rise">
        <p className="font-display text-xs uppercase tracking-[0.2em] text-mint">Authorized to Act Blueprint</p>
        <h1 className="mt-4 max-w-3xl font-display text-4xl font-extrabold leading-tight text-sand md:text-6xl">
          Secure GitHub automation with capability without custody.
        </h1>
        <p className="mt-5 max-w-2xl text-base text-sand/85 md:text-lg">
          SecureAudit scans repositories, verifies findings, and proposes fixes while Auth0 Token Vault keeps credentials out of agent runtime.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Link href="/dashboard" className="rounded-full bg-ember px-6 py-3 font-bold text-white shadow-glow transition hover:translate-y-[-1px]">
            Launch Dashboard
          </Link>
          <Link href="/policies" className="rounded-full border border-white/20 px-6 py-3 font-bold text-sand transition hover:border-mint hover:text-mint">
            Configure Policies
          </Link>
        </div>
      </div>
    </section>
  );
}
