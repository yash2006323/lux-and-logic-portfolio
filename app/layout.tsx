import type { Metadata } from 'next';
import './globals.css';

const SITE = 'https://yash2006323.github.io/lux-and-Logic.github.io';
const TITLE = 'Lux and Logic — Websites that ship on time, load fast, and convert';
const DESCRIPTION =
  'Fast, accessible websites on one standardised stack, with a written QA gate. First site ₹25,000 payable on handover — nothing upfront, no lock-in.';

export const metadata: Metadata = {
  metadataBase: new URL('https://yash2006323.github.io'),
  title: TITLE,
  description: DESCRIPTION,
  openGraph: {
    type: 'website',
    siteName: 'Lux and Logic',
    url: `${SITE}/`,
    title: TITLE,
    description: DESCRIPTION,
    images: [{ url: `${SITE}/og/home.png`, width: 1200, height: 630, alt: TITLE }],
  },
  twitter: {
    card: 'summary_large_image',
    title: TITLE,
    description: DESCRIPTION,
    images: [{ url: `${SITE}/og/home.png`, alt: TITLE }],
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/lux-and-Logic.github.io/favicon.svg" type="image/svg+xml" />
      </head>
      <body className="font-sans antialiased">
        <a className="skip-link" href="#main">Skip to main content</a>
        {children}
      </body>
    </html>
  );
}
