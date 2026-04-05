import Link from "next/link";

const items = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/policies", label: "Policies" },
  { href: "/audit", label: "Audit" },
];

export function Nav() {
  return (
    <header className="sticky top-0 z-30 border-b border-white/10 bg-ink/80 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-5 py-4">
        <Link href="/" className="font-display text-xl font-extrabold tracking-wide text-sand">
          SecureAudit
        </Link>
        <nav className="flex items-center gap-2">
          {items.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="rounded-full border border-white/15 px-4 py-2 text-sm font-semibold text-sand transition hover:border-mint hover:text-mint"
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
