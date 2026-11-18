/** @type {import('next').NextConfig} */
const nextConfig = {
  // Static export for free GitHub Pages hosting (project site: /lux-and-logic-portfolio/).
  output: 'export',
  basePath: '/lux-and-logic-portfolio',
  images: { unoptimized: true },
  trailingSlash: true,
};
export default nextConfig;
