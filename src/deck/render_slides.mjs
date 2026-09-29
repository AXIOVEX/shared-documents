// Render every slide in index.html to validate/page-NN.png at 2x scale.
// Requires: node or bun, the `playwright` package, and a Chromium executable.
// Run from this directory:  node render_slides.mjs
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const dir = path.dirname(new URL(import.meta.url).pathname);
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 2 });
await page.goto(pathToFileURL(path.join(dir, 'index.html')).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
const ids = await page.evaluate(() => [...document.querySelectorAll('section.slide')].map(s => s.id));
console.log('slides:', ids.length, ids.join(','));
for (let i = 0; i < ids.length; i++) {
  const num = String(i + 1).padStart(2, '0');
  await page.locator(`#${ids[i]}`).screenshot({ path: path.join(dir, 'validate', `page-${num}.png`) });
}
await browser.close();
console.log('rendered all');
