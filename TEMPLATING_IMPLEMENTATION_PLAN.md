# Website Templating Implementation Plan
## Migration to 11ty Static Site Generator

**Created**: 2025-11-12
**Status**: Planning Phase
**Estimated Effort**: 4-6 hours

---

## Executive Summary

Convert justinhenning.com from manually duplicated HTML files to an 11ty-based static site generator to eliminate template duplication across 35+ pages and establish a single source of truth for shared components.

**Current Pain Points:**
- Header duplicated across 35+ files (index, work, photography, archive, 31 project pages)
- Info page duplicated in 2 locations (index.html, work.html)
- Navigation duplicated with manual path adjustments per page
- Project data embedded in every project page (~200 lines of JS × 31 pages)
- 200-600 lines of inline CSS repeated per page
- Python scripts only generate project pages, main pages still manual

**Solution:**
Use 11ty (Eleventy) static site generator with Nunjucks templates to:
- Extract shared components (header, info, nav) → edit once, update everywhere
- Store project data in JSON → single source of truth
- Generate all pages from templates → consistent structure
- Maintain static HTML output → same deployment model

---

## Current State Analysis

### File Inventory

**Main Pages (4):**
- `/index.html` - Landing page (link-based navigation to work.html)
- `/work.html` - Main portfolio grid with video projects
- `/photography.html` - Photography gallery (20 images)
- `/archive.html` - Archive page

**Project Pages (31):**
- `/projects/*.html` - Individual project pages with Vimeo embeds
- Generated via Python script (`scripts/update-all-v2-pages.py`)

**Total Pages:** 35 HTML files

### Duplication Analysis

#### 1. Header Component
**Location:** All 35 pages
**Size:** ~200 lines HTML + CSS per page
**Contains:**
- Font-face declarations (Tonka font)
- Three-section layout: left nav, center title, right nav
- Mobile hamburger menu
- Responsive breakpoints
- Two-line title ("JUSTIN HENNING" / "CINEMATOGRAPHER")
- Info toggle (full/short text)

**Variation:** Mostly identical, minor path differences for relative links

#### 2. Information Overlay
**Location:** `index.html` (lines 746-797), `work.html` (lines 519-570)
**Size:** ~50 lines
**Contains:**
- Biography with image
- Contact details (US/WPA USA, UK/WPA London, Mexico/Latam, Personal)
- Footer with social links (Instagram, Archive)
- Tonka typeface credit

**Variation:** 100% identical duplication

#### 3. Side Navigation
**Location:** Most pages
**Contains:**
- Left: Filter links (ALL, FILM, COMMERCIAL, AUTOMOTIVE) or "RETURN TO MAIN PAGE"
- Right: PHOTOGRAPHY link

**Variation:** Different hrefs based on page location (relative vs absolute paths)

#### 4. Mobile Menu
**Location:** index.html, work.html, photography.html, archive.html
**Size:** ~50 lines per page
**Contains:**
- Hamburger toggle
- Filter options or page links
- Responsive display logic

**Variation:** Filter options vs page links depending on context

#### 5. Project Data Array
**Location:** All 31 project pages (embedded JavaScript)
**Size:** ~200 lines × 31 = 6,200 lines total
**Contains:**
- Full list of all projects with metadata
- Used for prev/next navigation
- Category filtering logic

**Variation:** Identical across all project pages

#### 6. Inline Styles
**Location:** Every page
**Size:** 200-600 lines per page
**Contains:**
- Font-face declarations (duplicated)
- Header styling (duplicated)
- Mobile responsive styles (duplicated)
- Component-specific styles (varies)

### Current Build Process

**Python Scripts in `/scripts/`:**
- `update-all-v2-pages.py` - Main project page generator
  - Contains hardcoded project data (140 lines of metadata)
  - Extracts styles from template file
  - Outputs complete HTML files
- `generate-v2-pages.py` - Similar generator (possibly older)
- `update-all-project-pages.py` - Another version
- `convert-index-to-v2.py` - Conversion utility

**Workflow:**
1. Edit project data in Python script
2. Run script to regenerate all 31 project pages
3. Manually edit main pages (index, work, photography, archive)
4. Copy-paste header changes across files
5. Manually sync info page between index.html and work.html

**Limitations:**
- No templating for main pages
- Must edit Python code to update project data
- Easy to miss files during updates
- No automatic rebuilds

---

## Recommended Solution: 11ty (Eleventy)

### Why 11ty?

**Pros:**
- JavaScript-based (familiar ecosystem)
- Minimal configuration (~10 lines)
- Supports multiple template engines (Nunjucks, Liquid, Handlebars)
- Zero client-side JS required (builds static HTML)
- Fast builds (< 1 second for 35 pages)
- Great for portfolios (used by photographers, designers)
- Active community and documentation
- Works with JSON data files (clean separation)

**Cons:**
- Requires Node.js/npm (already have based on repo)
- Learning curve for template syntax (~1 hour to learn basics)
- Adds build step to workflow (acceptable per user preference)

**Alternatives Considered:**
- Hugo (Go-based, faster but less flexible)
- Jekyll (Ruby-based, GitHub Pages default but slower)
- Next.js/Gatsby (overkill for static portfolio)
- Custom Node scripts (reinventing the wheel)

---

## Implementation Plan

### Phase 1: Setup & Configuration (30 mins)

**1.1 Install 11ty**
```bash
npm init -y
npm install --save-dev @11ty/eleventy
```

**1.2 Create `.eleventy.js` configuration**
```javascript
module.exports = function(eleventyConfig) {
  // Copy media files as-is
  eleventyConfig.addPassthroughCopy("src/media");
  eleventyConfig.addPassthroughCopy("src/style.css");
  eleventyConfig.addPassthroughCopy("src/photography-style.css");
  eleventyConfig.addPassthroughCopy("src/script.js");
  eleventyConfig.addPassthroughCopy("src/fonts");

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["njk", "html", "md"],
    htmlTemplateEngine: "njk"
  };
};
```

**1.3 Update `package.json` scripts**
```json
{
  "scripts": {
    "build": "eleventy",
    "start": "eleventy --serve",
    "clean": "rm -rf _site"
  }
}
```

**1.4 Create folder structure**
```bash
mkdir -p src/_includes/layouts
mkdir -p src/_includes/components
mkdir -p src/_data
mkdir -p src/projects
```

**1.5 Move existing files**
```bash
# Move media, styles, scripts (keep structure)
mv media src/
mv style.css src/
mv photography-style.css src/
mv script.js src/
mv fonts src/

# Main pages will be converted to templates (Phase 3)
# Project pages will be generated from data (Phase 4)
```

---

### Phase 2: Extract Components (1-2 hours)

#### 2.1 Create Base Layout (`src/_includes/layouts/base.njk`)

**Purpose:** Wrapper for all pages (HTML structure, head, body)

**Structure:**
```nunjucks
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title | default("JUSTIN HENNING - CINEMATOGRAPHER") }}</title>
  <link rel="stylesheet" href="{{ '/style.css' if isMainPage else '../style.css' }}">
  {% if hasPhotographyStyles %}
  <link rel="stylesheet" href="{{ '/photography-style.css' if isMainPage else '../photography-style.css' }}">
  {% endif %}
  {% block head %}{% endblock %}
</head>
<body>
  {% include "components/header.njk" %}

  <main>
    {{ content | safe }}
  </main>

  {% if hasInfoOverlay %}
    {% include "components/info.njk" %}
  {% endif %}

  {% block scripts %}{% endblock %}
</body>
</html>
```

**Key Variables:**
- `title` - Page title (SEO)
- `isMainPage` - Boolean for relative path handling
- `hasPhotographyStyles` - Include photography CSS
- `hasInfoOverlay` - Include info page component

**Source:** Extract from `index.html` lines 1-30, 800-end

---

#### 2.2 Create Header Component (`src/_includes/components/header.njk`)

**Purpose:** Site-wide navigation header

**Extract From:** Any page (e.g., `index.html` lines 35-250)

**Structure:**
```nunjucks
{# Font-face declarations #}
<style>
  @font-face {
    font-family: 'Tonka';
    src: url('{{ '/fonts/TonkaW00-Regular.woff2' if isMainPage else '../fonts/TonkaW00-Regular.woff2' }}') format('woff2'),
         url('{{ '/fonts/TonkaW00-Regular.woff' if isMainPage else '../fonts/TonkaW00-Regular.woff' }}') format('woff');
    font-weight: normal;
    font-style: normal;
  }
  {# Additional header styles... #}
</style>

<header>
  <div class="header-left">
    <a href="{{ '/' if isMainPage else '../index.html' }}" class="header-link">WORK</a>
    {% if hasFilters %}
      <a href="#all" class="filter-link active" data-filter="all">ALL</a>
      <a href="#film" class="filter-link" data-filter="film">FILM</a>
      <a href="#commercial" class="filter-link" data-filter="commercial">COMMERCIAL</a>
      <a href="#automotive" class="filter-link" data-filter="automotive">AUTOMOTIVE</a>
    {% else %}
      <a href="{{ '../work.html' if isProjectPage else '/work.html' }}" class="header-link">RETURN TO MAIN PAGE</a>
    {% endif %}
  </div>

  <div class="header-center">
    <h1 class="name-title">
      JUSTIN HENNING
      <span class="subtitle">CINEMATOGRAPHER</span>
    </h1>
  </div>

  <div class="header-right">
    <a href="{{ '/photography.html' if isMainPage else '../photography.html' }}" class="header-link">PHOTOGRAPHY</a>
    <a href="#" class="info-link">INFORMATION</a>
  </div>

  {# Mobile hamburger menu #}
  <div class="hamburger">
    <span></span>
    <span></span>
    <span></span>
  </div>
</header>

{# Mobile menu #}
<div class="mobile-menu">
  {% if hasFilters %}
    <a href="#all" class="filter-link active" data-filter="all">ALL</a>
    <a href="#film" class="filter-link" data-filter="film">FILM</a>
    <a href="#commercial" class="filter-link" data-filter="commercial">COMMERCIAL</a>
    <a href="#automotive" class="filter-link" data-filter="automotive">AUTOMOTIVE</a>
  {% else %}
    <a href="{{ '/' if isMainPage else '../index.html' }}">WORK</a>
  {% endif %}
  <a href="{{ '/photography.html' if isMainPage else '../photography.html' }}">PHOTOGRAPHY</a>
  <a href="#" class="info-link-mobile">INFORMATION</a>
</div>
```

**Key Variables:**
- `isMainPage` - Adjusts relative paths
- `isProjectPage` - Adjusts "RETURN TO MAIN PAGE" link
- `hasFilters` - Show category filters vs simple navigation

**Notes:**
- Path handling is critical (main pages vs project pages)
- Mobile menu structure mirrors desktop navigation

---

#### 2.3 Create Info Overlay Component (`src/_includes/components/info.njk`)

**Purpose:** Information page with biography and contacts

**Extract From:** `index.html` lines 746-797 or `work.html` lines 519-570

**Structure:**
```nunjucks
<div class="info-page">
  <button class="info-close">&times;</button>

  <div class="info-content">
    <div class="info-section">
      <div class="bio-section">
        <img src="{{ '/media/bio-photo.jpg' if isMainPage else '../media/bio-photo.jpg' }}" alt="Justin Henning" class="bio-photo">
        <div class="bio-text">
          <p class="info-full">
            Justin Henning is a Los Angeles based Cinematographer originally from Prince Edward Island, Canada...
          </p>
          <p class="info-short">
            Justin Henning is a Los Angeles based Cinematographer...
          </p>
        </div>
      </div>
    </div>

    <div class="info-section contacts-section">
      <div class="contact-column">
        <h3>US / WPA USA</h3>
        <p><a href="mailto:steven@wpausa.com">Steven</a></p>
        <p><a href="mailto:kristen@wpausa.com">Kristen Billings</a></p>
        <p><a href="mailto:louiza@wpausa.com">Louiza Vick</a></p>
      </div>

      <div class="contact-column">
        <h3>UK / WPA LONDON</h3>
        <p><a href="mailto:barnaby@wpalondondps.com">Barnaby Laws</a></p>
      </div>

      <div class="contact-column">
        <h3>MEXICO & LATAM / 9AM</h3>
        <p><a href="mailto:rodrigo@9-am.tv">Rodrigo Gavaldón</a></p>
      </div>

      <div class="contact-column">
        <h3>PERSONAL CONTACT</h3>
        <p><a href="mailto:henning.justin@gmail.com">henning.justin@gmail.com</a></p>
      </div>
    </div>

    <footer class="info-footer">
      <div class="footer-links">
        <a href="https://instagram.com/justinthenning" target="_blank">INSTAGRAM</a>
        <a href="{{ '/archive.html' if isMainPage else '../archive.html' }}">ARCHIVE</a>
      </div>
      <p class="footer-credit">Tonka typeface courtesy of <a href="https://www.shotbypersona.com" target="_blank">Todd Martin</a></p>
    </footer>
  </div>
</div>
```

**Key Variables:**
- `isMainPage` - Adjusts relative paths for images and links

**Notes:**
- This component was previously duplicated in index.html and work.html
- Now maintained in single location

---

#### 2.4 Extract Common CSS

**Current State:** 200-600 lines of inline `<style>` per page

**Strategy:**
1. **Keep in `style.css`:** Global styles (typography, colors, layout)
2. **Move to `style.css`:** Header styles (currently inline on every page)
3. **Move to `style.css`:** Info overlay styles
4. **Keep inline:** Page-specific styles (grid layouts, project-specific tweaks)

**Benefits:**
- Reduce page size
- Browser caching of shared styles
- Easier maintenance

**Note:** This can be done incrementally during Phase 3-4

---

### Phase 3: Create Data File (30 mins)

#### 3.1 Create `src/_data/projects.json`

**Purpose:** Single source of truth for all project metadata

**Extract From:** `scripts/update-all-v2-pages.py` lines 8-150 (approx)

**Structure:**
```json
{
  "projects": [
    {
      "id": 1,
      "slug": "your-lucky-day",
      "title": "YOUR LUCKY DAY",
      "subtitle": "Dir. Dan Brown",
      "category": "film",
      "vimeoId": "872749030",
      "thumbnailUrl": "media/thumbnails/your-lucky-day.jpg",
      "previewVideo": "media/previews/your-lucky-day.mp4",
      "hasLocalVideo": true,
      "description": "Feature film description...",
      "specs": {
        "camera": "ARRI ALEXA MINI",
        "lenses": "Cooke S4"
      },
      "large": false
    },
    {
      "id": 2,
      "slug": "woodford-reserve",
      "title": "WOODFORD RESERVE",
      "subtitle": "Dir. David Holm",
      "category": "commercial",
      "vimeoId": "898398761",
      "thumbnailUrl": "media/thumbnails/woodford-reserve.jpg",
      "previewVideo": "media/previews/woodford-reserve.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 3,
      "slug": "huawei",
      "title": "HUAWEI",
      "subtitle": "Agency Campaign",
      "category": "commercial",
      "vimeoId": "1046541141",
      "thumbnailUrl": "media/thumbnails/huawei.jpg",
      "previewVideo": "media/previews/huawei.mp4",
      "hasLocalVideo": true,
      "large": true
    }
    // ... 13 more projects (16 total, including photography card)
  ]
}
```

**Required Fields:**
- `id` - Unique numeric ID (for ordering)
- `slug` - URL-friendly identifier
- `title` - Display title
- `category` - "film", "commercial", "automotive", or "photography"
- `vimeoId` - Vimeo video ID (null for photography)
- `thumbnailUrl` - Path to JPG thumbnail
- `previewVideo` - Path to preview clip (null for photography)
- `hasLocalVideo` - Boolean (false for Gatorade, true for others)
- `large` - Boolean (spans 2x2 grid if true)

**Optional Fields:**
- `subtitle` - Director or agency
- `description` - Project details
- `specs` - Camera/lens info

**Photography Entry:**
```json
{
  "id": 14,
  "slug": "photography",
  "title": "PHOTOGRAPHY",
  "category": "photography",
  "vimeoId": null,
  "thumbnailUrl": "media/thumbnails/photography.jpg",
  "previewVideo": null,
  "hasLocalVideo": false,
  "large": false,
  "linkTo": "/photography.html"
}
```

**11ty Access:**
All templates can access this via `{{ projects }}` or loop through:
```nunjucks
{% for project in projects.projects %}
  {{ project.title }}
{% endfor %}
```

---

#### 3.2 Create Site Metadata (`src/_data/site.json`)

**Purpose:** Global site configuration

**Structure:**
```json
{
  "name": "Justin Henning",
  "title": "Cinematographer",
  "url": "https://justinhenning.com",
  "description": "Los Angeles based Cinematographer",
  "social": {
    "instagram": "https://instagram.com/justinthenning",
    "email": "henning.justin@gmail.com"
  },
  "contacts": {
    "us": {
      "name": "US / WPA USA",
      "people": [
        {"name": "Steven", "email": "steven@wpausa.com"},
        {"name": "Kristen Billings", "email": "kristen@wpausa.com"},
        {"name": "Louiza Vick", "email": "louiza@wpausa.com"}
      ]
    },
    "uk": {
      "name": "UK / WPA LONDON",
      "people": [
        {"name": "Barnaby Laws", "email": "barnaby@wpalondondps.com"}
      ]
    },
    "latam": {
      "name": "MEXICO & LATAM / 9AM",
      "people": [
        {"name": "Rodrigo Gavaldón", "email": "rodrigo@9-am.tv"}
      ]
    }
  }
}
```

**Usage:** Update info overlay to loop through contacts data instead of hardcoding

---

### Phase 4: Convert Main Pages (1 hour)

#### 4.1 Create `src/index.njk`

**Purpose:** Landing page (currently redirects to work.html)

**Structure:**
```nunjucks
---
layout: layouts/base.njk
title: Justin Henning - Cinematographer
isMainPage: true
hasInfoOverlay: true
---

{# Current index.html content - simplified if it's just a redirect #}
<div class="landing-page">
  {# If keeping as separate landing page, add content here #}
  {# Or implement redirect via meta tag or JavaScript #}
</div>

<script>
  // Redirect to work.html if that's the intended behavior
  // window.location.href = '/work.html';
</script>
```

**Decision Point:** Keep index.html as separate landing page or merge with work.html?

---

#### 4.2 Create `src/work.njk`

**Purpose:** Main portfolio grid with video projects

**Extract From:** `work.html`

**Structure:**
```nunjucks
---
layout: layouts/base.njk
title: Justin Henning - Cinematographer - Work
isMainPage: true
hasInfoOverlay: true
hasFilters: true
---

<div class="grid-container">
  {% for project in projects.projects %}
    <a
      href="/projects/{{ project.slug }}.html"
      class="project-card{% if project.large %} large{% endif %}"
      data-category="{{ project.category }}"
      style="background-image: url('{{ project.thumbnailUrl }}');"
    >
      {% if project.previewVideo %}
        <video
          class="preview-video"
          src="{{ project.previewVideo }}"
          muted
          loop
          playsinline
        ></video>
      {% endif %}

      <div class="project-overlay">
        <h2>{{ project.title }}</h2>
        {% if project.subtitle %}
          <p>{{ project.subtitle }}</p>
        {% endif %}
      </div>
    </a>
  {% endfor %}
</div>

<script src="/script.js"></script>
```

**Key Changes:**
- Loop through `projects.projects` instead of hardcoded HTML
- Dynamic href generation
- Conditional rendering for preview videos
- Keeps existing class structure for CSS compatibility

---

#### 4.3 Create `src/photography.njk`

**Purpose:** Photography gallery page

**Extract From:** `photography.html`

**Structure:**
```nunjucks
---
layout: layouts/base.njk
title: Justin Henning - Photography
isMainPage: true
hasInfoOverlay: false
hasPhotographyStyles: true
---

<div class="photography-gallery">
  {% for i in range(1, 21) %}
    <div class="photo-item">
      <img
        src="/media/photography/{{ '%03d' | format(i) }}.jpg"
        alt="Photography {{ i }}"
        loading="lazy"
      >
    </div>
  {% endfor %}
</div>

<style>
  {# Photography-specific styles (if not in photography-style.css) #}
</style>
```

**Note:** 20 images numbered 001.jpg - 020.jpg

---

#### 4.4 Create `src/archive.njk`

**Purpose:** Archive page

**Extract From:** `archive.html`

**Structure:**
```nunjucks
---
layout: layouts/base.njk
title: Justin Henning - Archive
isMainPage: true
hasInfoOverlay: false
---

<div class="archive-container">
  {# Archive content from archive.html #}
</div>
```

---

### Phase 5: Generate Project Pages (1-2 hours)

#### 5.1 Create Project Layout (`src/_includes/layouts/project.njk`)

**Purpose:** Template for all 31 project pages

**Extract From:** Any project page (e.g., `projects/huawei.html`)

**Structure:**
```nunjucks
---
layout: layouts/base.njk
---

<style>
  {# Project-specific styles #}
  body {
    background-color: #fff;
    color: #000;
  }

  .project-container {
    max-width: 1200px;
    margin: 120px auto 60px;
    padding: 0 40px;
  }

  {# Additional project page styles... #}
</style>

<div class="project-container">
  <h1 class="project-title">{{ title }}</h1>
  {% if subtitle %}
    <p class="project-subtitle">{{ subtitle }}</p>
  {% endif %}

  <div class="video-container">
    <div style="padding:56.25% 0 0 0;position:relative;">
      <iframe
        src="https://player.vimeo.com/video/{{ vimeoId }}?badge=0&autopause=0&player_id=0&app_id=58479"
        frameborder="0"
        allow="autoplay; fullscreen; picture-in-picture; clipboard-write"
        style="position:absolute;top:0;left:0;width:100%;height:100%;"
        title="{{ title }}"
      ></iframe>
    </div>
  </div>

  {% if specs %}
    <div class="project-specs">
      {% if specs.camera %}<p><strong>Camera:</strong> {{ specs.camera }}</p>{% endif %}
      {% if specs.lenses %}<p><strong>Lenses:</strong> {{ specs.lenses }}</p>{% endif %}
    </div>
  {% endif %}

  {% if description %}
    <div class="project-description">
      {{ description | safe }}
    </div>
  {% endif %}
</div>

<div class="navigation-wrapper">
  {# Previous project card #}
  {% if previousProject %}
    <a href="/projects/{{ previousProject.slug }}.html" class="nav-card prev-card">
      <div class="nav-card-content" style="background-image: url('/{{ previousProject.thumbnailUrl }}');">
        <div class="nav-overlay">
          <span class="nav-arrow">←</span>
          <h3>{{ previousProject.title }}</h3>
        </div>
      </div>
    </a>
  {% endif %}

  {# Next project card #}
  {% if nextProject %}
    <a href="/projects/{{ nextProject.slug }}.html" class="nav-card next-card">
      <div class="nav-card-content" style="background-image: url('/{{ nextProject.thumbnailUrl }}');">
        <div class="nav-overlay">
          <h3>{{ nextProject.title }}</h3>
          <span class="nav-arrow">→</span>
        </div>
      </div>
    </a>
  {% endif %}
</div>

<script src="https://player.vimeo.com/api/player.js"></script>
```

**Key Variables:**
- `title`, `subtitle`, `vimeoId`, `specs`, `description` - From project data
- `previousProject`, `nextProject` - For navigation (calculated in 5.2)

---

#### 5.2 Create Project Page Generator (`src/projects/projects.11tydata.js`)

**Purpose:** Generate 31 project pages from data

**Structure:**
```javascript
module.exports = {
  layout: "layouts/project.njk",
  isProjectPage: true,
  tags: "project",

  eleventyComputed: {
    // Calculate previous/next projects for navigation
    previousProject: (data) => {
      const projects = data.projects.projects.filter(p => p.category !== 'photography');
      const currentIndex = projects.findIndex(p => p.slug === data.slug);
      return currentIndex > 0 ? projects[currentIndex - 1] : null;
    },

    nextProject: (data) => {
      const projects = data.projects.projects.filter(p => p.category !== 'photography');
      const currentIndex = projects.findIndex(p => p.slug === data.slug);
      return currentIndex < projects.length - 1 ? projects[currentIndex + 1] : null;
    },

    // Generate permalink
    permalink: (data) => `/projects/${data.slug}.html`
  }
};
```

**Note:** This sets default layout and computes navigation for all project pages

---

#### 5.3 Create Project Pages Collection (`src/projects/projects.json`)

**Purpose:** Generate individual pages from project data

**Structure:**
```json
{
  "pagination": {
    "data": "projects.projects",
    "size": 1,
    "alias": "project",
    "filter": ["photography"]
  },
  "permalink": "/projects/{{ project.slug }}.html"
}
```

**OR use JavaScript for more control:**

**File:** `src/projects/projects.11ty.js`

```javascript
class ProjectPages {
  data() {
    return {
      pagination: {
        data: "projects.projects",
        size: 1,
        alias: "project",
        filter: ["photography"] // Exclude photography entry
      },
      layout: "layouts/project.njk",
      eleventyComputed: {
        title: data => data.project.title,
        subtitle: data => data.project.subtitle,
        vimeoId: data => data.project.vimeoId,
        specs: data => data.project.specs,
        description: data => data.project.description,
        slug: data => data.project.slug,
        isProjectPage: true
      }
    };
  }

  render(data) {
    // Return empty string - layout handles rendering
    return "";
  }
}

module.exports = ProjectPages;
```

**Result:** 11ty generates 31 HTML files in `_site/projects/` directory

---

### Phase 6: Update JavaScript (30 mins)

#### 6.1 Review `script.js`

**Current Functionality:**
- Video hover previews (play on hover)
- Category filtering
- Mobile menu toggle
- Info overlay toggle

**Required Changes:**
- Remove hardcoded `projects` array (now available from HTML/data attributes)
- Update selectors if DOM structure changed
- Ensure filter logic works with new HTML structure

**Key Decision:** Keep JavaScript mostly unchanged - HTML structure maintained for compatibility

---

#### 6.2 Project Page Navigation

**Current:** Embedded `projects` array in every project page

**New Approach:**
- Option A: Keep client-side navigation, load projects.json via fetch
- Option B: Generate navigation at build time (already done in project.njk layout)

**Recommendation:** Option B - prev/next links generated at build time (no JS needed)

---

### Phase 7: Build & Test (1 hour)

#### 7.1 Initial Build

```bash
npm run build
```

**Expected Output:**
```
_site/
├── index.html
├── work.html
├── photography.html
├── archive.html
├── projects/
│   ├── your-lucky-day.html
│   ├── woodford-reserve.html
│   ├── huawei.html
│   └── ... (28 more)
├── media/
│   ├── previews/
│   ├── thumbnails/
│   └── photography/
├── style.css
├── photography-style.css
├── script.js
└── fonts/
```

**Verification:**
- 35 HTML files generated
- All media files copied
- CSS/JS files copied

---

#### 7.2 Visual Regression Testing

**Manual Checks:**
1. Open `_site/work.html` in browser
2. Compare side-by-side with original `work.html`
3. Verify header looks identical
4. Verify video previews work (hover to play)
5. Test category filters (ALL, FILM, COMMERCIAL, AUTOMOTIVE)
6. Test mobile menu (responsive behavior)
7. Test info overlay (click INFORMATION)

**Project Page Checks:**
1. Open `_site/projects/huawei.html`
2. Verify Vimeo embed works
3. Verify prev/next navigation works
4. Check mobile responsiveness

**Photography Page:**
1. Open `_site/photography.html`
2. Verify all 20 images load
3. Check grid layout

---

#### 7.3 Automated Testing (Optional)

**Tools:**
- Playwright or Cypress for E2E testing
- Percy or Chromatic for visual regression
- Lighthouse for performance

**Test Cases:**
- All pages return 200 status
- No broken links (internal)
- Video previews load
- Filter functionality works
- Mobile menu toggles

---

### Phase 8: Deployment Strategy (30 mins)

#### 8.1 Update `.gitignore`

```gitignore
node_modules/
_site/
.DS_Store
```

**Note:** Commit source files (`src/`), not built output (`_site/`)

---

#### 8.2 Update Deployment Process

**Before (Current):**
1. Edit HTML files
2. Git commit
3. Push to hosting (Netlify/Vercel/etc.)

**After (New):**
1. Edit templates (`src/*.njk`) or data (`src/_data/projects.json`)
2. Run `npm run build` (generates `_site/`)
3. Git commit source files
4. Push to hosting (auto-builds or deploy `_site/`)

**Hosting Options:**

**Netlify:**
```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = "_site"
```

**Vercel:**
```json
// vercel.json
{
  "buildCommand": "npm run build",
  "outputDirectory": "_site"
}
```

**GitHub Pages:**
- Use GitHub Actions to build on push
- Deploy `_site/` directory

---

#### 8.3 Rollback Plan

**If something breaks:**
1. Current HTML files are preserved (not deleted during Phase 5)
2. Can revert git commits
3. Can deploy old HTML files manually
4. Keep `backup/` directory with original HTML before starting

**Create backup:**
```bash
mkdir backup
cp -r *.html projects/ backup/
```

---

### Phase 9: Update Documentation (15 mins)

#### 9.1 Update `CLAUDE.md`

**Add section:**
```markdown
## Build Process

This site uses 11ty (Eleventy) static site generator.

### Local Development
```bash
npm install          # First time only
npm start            # Serve at http://localhost:8080 with live reload
```

### Building for Production
```bash
npm run build        # Outputs to _site/
```

### Project Structure
```
src/
├── _includes/       # Templates and components
├── _data/           # Project data (JSON)
├── *.njk            # Page templates
├── projects/        # Project page generator
└── media/           # Static assets

_site/              # Built output (not committed)
```

### Adding New Projects
1. Add entry to `src/_data/projects.json`
2. Add thumbnail to `media/thumbnails/`
3. Generate preview: `./create_previews.sh` (if video available)
4. Run `npm run build`

### Editing Shared Components
- Header: `src/_includes/components/header.njk`
- Info overlay: `src/_includes/components/info.njk`
- Base layout: `src/_includes/layouts/base.njk`
```

---

#### 9.2 Create `MIGRATION_NOTES.md`

**Document:**
- What changed
- Before/after comparison
- Known issues
- Performance improvements
- Maintenance benefits

---

## Migration Checklist

Use this checklist when executing the plan:

### Pre-Migration
- [ ] Create backup of current site (`backup/` directory)
- [ ] Document current deployment process
- [ ] Test current site functionality (screenshots/recordings)
- [ ] Ensure `create_previews.sh` still works with new structure

### Phase 1: Setup
- [ ] Install 11ty (`npm install --save-dev @11ty/eleventy`)
- [ ] Create `.eleventy.js` configuration
- [ ] Update `package.json` scripts
- [ ] Create folder structure (`src/_includes`, `src/_data`, etc.)
- [ ] Move static assets to `src/`

### Phase 2: Components
- [ ] Create `base.njk` layout
- [ ] Create `header.njk` component
- [ ] Create `info.njk` component
- [ ] Extract common CSS to `style.css`
- [ ] Test component rendering in isolation

### Phase 3: Data
- [ ] Create `projects.json` with all 16 projects
- [ ] Create `site.json` with global config
- [ ] Validate JSON syntax
- [ ] Verify data structure matches template needs

### Phase 4: Main Pages
- [ ] Convert `index.html` → `index.njk`
- [ ] Convert `work.html` → `work.njk`
- [ ] Convert `photography.html` → `photography.njk`
- [ ] Convert `archive.html` → `archive.njk`
- [ ] Test each page builds correctly

### Phase 5: Project Pages
- [ ] Create `project.njk` layout
- [ ] Create `projects.11tydata.js` or `projects.11ty.js`
- [ ] Test project page generation
- [ ] Verify prev/next navigation
- [ ] Check Vimeo embeds

### Phase 6: JavaScript
- [ ] Review `script.js` for required changes
- [ ] Update selectors if needed
- [ ] Test video hover functionality
- [ ] Test category filtering
- [ ] Test mobile menu
- [ ] Test info overlay

### Phase 7: Build & Test
- [ ] Run `npm run build`
- [ ] Verify 35 HTML files generated
- [ ] Visual comparison: work.html
- [ ] Visual comparison: photography.html
- [ ] Visual comparison: sample project page
- [ ] Test all navigation links
- [ ] Test on mobile (responsive)
- [ ] Test video previews
- [ ] Test Vimeo embeds

### Phase 8: Deployment
- [ ] Update `.gitignore`
- [ ] Test build on fresh clone
- [ ] Configure hosting (Netlify/Vercel)
- [ ] Deploy to staging environment
- [ ] Test staging site
- [ ] Deploy to production
- [ ] Monitor for errors

### Phase 9: Documentation
- [ ] Update `CLAUDE.md`
- [ ] Create `MIGRATION_NOTES.md`
- [ ] Document known issues
- [ ] Update README if exists

### Post-Migration
- [ ] Monitor site for 24 hours
- [ ] Check analytics (if setup)
- [ ] Verify SEO (meta tags, titles)
- [ ] Delete old HTML files (after confirmation)
- [ ] Archive Python scripts (move to `scripts/archive/`)

---

## Troubleshooting Guide

### Build Fails

**Error: `Cannot find module '@11ty/eleventy'`**
- Solution: Run `npm install`

**Error: `Template render error`**
- Check Nunjucks syntax in templates
- Verify data structure matches template expectations
- Check for typos in variable names

### Visual Differences

**Header looks different:**
- Compare extracted CSS with original inline styles
- Check path variables (`isMainPage`, `isProjectPage`)
- Verify font files copied correctly

**Video previews not working:**
- Check `script.js` selectors match new HTML structure
- Verify preview video paths are correct
- Check console for JavaScript errors

**Filters not working:**
- Verify `data-category` attributes on project cards
- Check filter JavaScript in `script.js`
- Ensure category values match (lowercase)

### Navigation Issues

**Broken links:**
- Check `isMainPage` vs `isProjectPage` logic
- Verify relative paths in components
- Use browser DevTools to inspect href values

**Prev/next navigation broken:**
- Check `projects.11tydata.js` calculation logic
- Verify project order in `projects.json`
- Ensure photography entry excluded from navigation

### Performance Issues

**Build takes too long:**
- 11ty should build 35 pages in < 1 second
- Check for infinite loops in templates
- Verify media files aren't being processed unnecessarily

**Pages load slowly:**
- Check file sizes (should be similar to original)
- Verify media files copied correctly (not duplicated)
- Use browser DevTools to check network waterfall

---

## Success Criteria

The migration is successful when:

1. **Visual Parity:** Generated site looks identical to original
2. **Functional Parity:** All interactions work (filters, navigation, videos)
3. **Maintainability:** Header can be updated in one file, not 35
4. **Data-Driven:** Projects managed via JSON, not HTML/Python
5. **Fast Builds:** `npm run build` completes in < 2 seconds
6. **No Regressions:** No broken links, missing images, or JavaScript errors
7. **Documentation:** Team knows how to add projects and edit templates

---

## Future Enhancements

After successful migration, consider:

### Short-term (Low effort)
- [ ] Add sitemap.xml generation
- [ ] Add RSS feed for projects
- [ ] Optimize image loading (lazy load, responsive images)
- [ ] Add meta tags for SEO (Open Graph, Twitter Cards)

### Medium-term (Medium effort)
- [ ] Implement search functionality
- [ ] Add project filtering by year
- [ ] Create project detail pages with more content
- [ ] Add analytics tracking

### Long-term (High effort)
- [ ] Integrate headless CMS (Sanity, Contentful)
- [ ] Add admin interface for non-technical updates
- [ ] Implement A/B testing
- [ ] Add internationalization (i18n)

---

## Resources

### 11ty Documentation
- Official Docs: https://www.11ty.dev/docs/
- Nunjucks Syntax: https://mozilla.github.io/nunjucks/templating.html
- Data Files: https://www.11ty.dev/docs/data-global/
- Layouts: https://www.11ty.dev/docs/layouts/
- Collections: https://www.11ty.dev/docs/collections/

### Example Sites
- 11ty Starter Projects: https://www.11ty.dev/docs/starter/
- Portfolio Examples: Search GitHub for "11ty portfolio"

### Community
- 11ty Discord: https://www.11ty.dev/blog/discord/
- GitHub Discussions: https://github.com/11ty/eleventy/discussions

---

## Contact for Questions

When implementing this plan, refer back to:
- Current site structure (before migration)
- Python scripts in `scripts/` directory
- This document for step-by-step guidance

**Estimated Total Time:** 4-6 hours (excluding learning curve)

**Skill Level Required:** Intermediate (HTML/CSS/JS, basic command line)

---

## Appendix A: File Mapping

| Current File | New Template | Notes |
|--------------|--------------|-------|
| `index.html` | `src/index.njk` | Landing page |
| `work.html` | `src/work.njk` | Main grid page |
| `photography.html` | `src/photography.njk` | Gallery page |
| `archive.html` | `src/archive.njk` | Archive page |
| `projects/*.html` (31 files) | Generated from `src/projects/projects.11ty.js` + `src/_data/projects.json` | Project pages |
| N/A (duplicated) | `src/_includes/components/header.njk` | Shared header |
| N/A (duplicated) | `src/_includes/components/info.njk` | Shared info overlay |
| N/A (duplicated) | `src/_includes/layouts/base.njk` | Base HTML structure |
| N/A (duplicated) | `src/_includes/layouts/project.njk` | Project page structure |
| `scripts/update-all-v2-pages.py` | `src/_data/projects.json` + 11ty build | Data extracted, logic replaced |

---

## Appendix B: Data Structure Reference

### Complete `projects.json` Template

```json
{
  "projects": [
    {
      "id": 1,
      "slug": "your-lucky-day",
      "title": "YOUR LUCKY DAY",
      "subtitle": "Dir. Dan Brown",
      "category": "film",
      "vimeoId": "872749030",
      "thumbnailUrl": "media/thumbnails/your-lucky-day.jpg",
      "previewVideo": "media/previews/YourLuckyDay_TRL_h264.mp4",
      "hasLocalVideo": true,
      "large": false,
      "description": "",
      "specs": {}
    },
    {
      "id": 2,
      "slug": "woodford-reserve",
      "title": "WOODFORD RESERVE",
      "subtitle": "Dir. David Holm",
      "category": "commercial",
      "vimeoId": "898398761",
      "thumbnailUrl": "media/thumbnails/woodford-reserve.jpg",
      "previewVideo": "media/previews/woodford-reserve.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 3,
      "slug": "huawei",
      "title": "HUAWEI",
      "subtitle": "Agency Campaign",
      "category": "commercial",
      "vimeoId": "1046541141",
      "thumbnailUrl": "media/thumbnails/huawei.jpg",
      "previewVideo": "media/previews/huawei.mp4",
      "hasLocalVideo": true,
      "large": true
    },
    {
      "id": 4,
      "slug": "kia",
      "title": "KIA",
      "subtitle": "Dir. Brent Foster",
      "category": "automotive",
      "vimeoId": "913839989",
      "thumbnailUrl": "media/thumbnails/kia.jpg",
      "previewVideo": "media/previews/kia.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 5,
      "slug": "royal-bank-of-canada",
      "title": "ROYAL BANK OF CANADA",
      "subtitle": "Dir. David Holm",
      "category": "commercial",
      "vimeoId": "891284220",
      "thumbnailUrl": "media/thumbnails/rbc.jpg",
      "previewVideo": "media/previews/rbc.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 6,
      "slug": "k-n",
      "title": "K&N",
      "subtitle": "Dir. Miko Lim",
      "category": "automotive",
      "vimeoId": "523316278",
      "thumbnailUrl": "media/thumbnails/kn.jpg",
      "previewVideo": "media/previews/kn.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 7,
      "slug": "ram",
      "title": "RAM",
      "subtitle": "Dir. David Holm",
      "category": "automotive",
      "vimeoId": "930752804",
      "thumbnailUrl": "media/thumbnails/ram.jpg",
      "previewVideo": "media/previews/ram.mp4",
      "hasLocalVideo": true,
      "large": true
    },
    {
      "id": 8,
      "slug": "audi",
      "title": "AUDI",
      "subtitle": "Dir. David Holm",
      "category": "automotive",
      "vimeoId": "163036231",
      "thumbnailUrl": "media/thumbnails/audi.jpg",
      "previewVideo": "media/previews/audi.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 9,
      "slug": "jeep",
      "title": "JEEP",
      "subtitle": "Dir. David Holm",
      "category": "automotive",
      "vimeoId": "898405588",
      "thumbnailUrl": "media/thumbnails/jeep.jpg",
      "previewVideo": "media/previews/jeep.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 10,
      "slug": "ford",
      "title": "FORD",
      "subtitle": "Dir. Scott Weintrob",
      "category": "automotive",
      "vimeoId": "745033991",
      "thumbnailUrl": "media/thumbnails/ford.jpg",
      "previewVideo": "media/previews/ford.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 11,
      "slug": "american-outlaws",
      "title": "AMERICAN OUTLAWS",
      "subtitle": "Dir. Sean McEwen",
      "category": "film",
      "vimeoId": "797538936",
      "thumbnailUrl": "media/thumbnails/american-outlaws.jpg",
      "previewVideo": "media/previews/AO_TRL_MASTER_AFM.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 12,
      "slug": "pei",
      "title": "PRINCE EDWARD ISLAND",
      "subtitle": "Dir. Brent Foster",
      "category": "commercial",
      "vimeoId": "374024991",
      "thumbnailUrl": "media/thumbnails/pei.jpg",
      "previewVideo": "media/previews/pei.mp4",
      "hasLocalVideo": true,
      "large": true
    },
    {
      "id": 13,
      "slug": "lamborghini",
      "title": "LAMBORGHINI",
      "subtitle": "Dir. David Holm",
      "category": "automotive",
      "vimeoId": "242791079",
      "thumbnailUrl": "media/thumbnails/lamborghini.jpg",
      "previewVideo": "media/previews/lamborghini.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 14,
      "slug": "photography",
      "title": "PHOTOGRAPHY",
      "category": "photography",
      "vimeoId": null,
      "thumbnailUrl": "media/thumbnails/photography.jpg",
      "previewVideo": null,
      "hasLocalVideo": false,
      "large": false,
      "linkTo": "/photography.html"
    },
    {
      "id": 15,
      "slug": "ralph-lauren",
      "title": "RALPH LAUREN",
      "subtitle": "Polo Blue",
      "category": "commercial",
      "vimeoId": "261889797",
      "thumbnailUrl": "media/thumbnails/polo.jpg",
      "previewVideo": "media/previews/polo.mp4",
      "hasLocalVideo": true,
      "large": false
    },
    {
      "id": 16,
      "slug": "gatorade",
      "title": "GATORADE",
      "subtitle": "Commercial",
      "category": "commercial",
      "vimeoId": "1046557409",
      "thumbnailUrl": "media/thumbnails/gatorade.jpg",
      "previewVideo": null,
      "hasLocalVideo": false,
      "large": false
    }
  ]
}
```

---

## Appendix C: Quick Reference Commands

```bash
# Install dependencies
npm install

# Development server (with live reload)
npm start
# or
npx @11ty/eleventy --serve

# Build for production
npm run build
# or
npx @11ty/eleventy

# Clean build directory
npm run clean
# or
rm -rf _site

# Watch for changes (no server)
npx @11ty/eleventy --watch

# Debug build
DEBUG=Eleventy* npx @11ty/eleventy

# Serve built site (after build)
npx http-server _site
# or
python -m http.server 8000 --directory _site
```

---

**END OF DOCUMENT**

*This plan provides complete context for implementing 11ty templating in subsequent sessions. Follow phases sequentially and refer to appendices for detailed examples.*
