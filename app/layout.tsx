import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Lux and Logic — Websites built to be reliable',
  description:
    'Lux and Logic builds fast, accessible, conversion-focused websites on a standardised stack — shipped through a written QA gate and maintained after launch.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="font-sans antialiased">
        <a className="skip-link" href="#main">Skip to main content</a>
        {children}
      </body>
    </html>
  );
}
