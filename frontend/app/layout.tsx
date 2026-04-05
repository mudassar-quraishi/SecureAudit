import "./globals.css";
import { Nav } from "@/components/nav";

export const metadata = {
  title: "SecureAudit",
  description: "Zero-trust GitHub security auditor",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Nav />
        <main className="mx-auto max-w-6xl px-5 py-8">{children}</main>
      </body>
    </html>
  );
}
