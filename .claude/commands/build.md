---
description: Build the Eleventy site (src/ → _site/)
---

Run the Eleventy build process to regenerate the `_site/` directory from `src/` templates.

This command:
1. Compiles all `.njk` templates in `src/`
2. Copies static assets (CSS, JS, media)
3. Generates final HTML files in `_site/`
4. Shows build output and any errors

**When to use:** After editing any files in `src/` directory before serving or deploying.

**Equivalent to:** `npm run build`
