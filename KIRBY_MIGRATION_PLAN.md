# Kirby CMS Migration Plan
## Justin Henning Cinematography Portfolio

**Created**: 2025-11-12
**Status**: Planning Phase
**Estimated Duration**: 1-2 weeks
**Cost**: €99 Kirby license + hosting migration

---

## Executive Summary

This document outlines the complete migration plan from the current static HTML portfolio site to Kirby CMS. The migration maintains all existing functionality while adding a visual content management interface and improving code maintainability.

**Current Site**: 33 static HTML pages (index, photography, 31 project pages)
**Target**: Kirby 4 flat-file CMS with Panel interface
**Approach**: Preserve design, enhance management, maintain performance

---

## Table of Contents

1. [Current State Analysis](#current-state-analysis)
2. [Why Kirby CMS?](#why-kirby-cms)
3. [Target Kirby Architecture](#target-kirby-architecture)
4. [Complete Data Mapping](#complete-data-mapping)
5. [Implementation Phases](#implementation-phases)
6. [Blueprint Definitions](#blueprint-definitions)
7. [Template Code](#template-code)
8. [Configuration Files](#configuration-files)
9. [Media Migration Strategy](#media-migration-strategy)
10. [Testing Checklist](#testing-checklist)
11. [Deployment Guide](#deployment-guide)
12. [Rollback Plan](#rollback-plan)
13. [Resources](#resources)

---

## Current State Analysis

### Site Structure

```
/Users/justinhenning/code/website/
├── index.html                    # Main portfolio grid (home)
├── photography.html              # Photography gallery
├── projects/                     # 31 individual project pages
│   ├── your-lucky-day.html
│   ├── woodford-reserve.html
│   ├── huawei.html
│   ├── kia.html
│   ├── rbc.html
│   ├── kn.html
│   ├── ram.html
│   ├── audi.html
│   ├── jeep.html
│   ├── ford.html
│   ├── american-outlaws.html
│   ├── pei.html
│   ├── lamborghini.html
│   ├── nikon.html
│   ├── ralph-lauren.html
│   └── gatorade.html
├── media/
│   ├── previews/                 # 2.5MB - 16 video files (5sec clips)
│   ├── thumbnails/               # ~3MB - 16 JPG files
│   └── photography/              # ~7MB - 20 images (001.jpg-020.jpg)
├── style.css                     # Main stylesheet
├── photography-style.css         # Photography-specific styles
├── script.js                     # Grid filtering & hover logic
└── assets/                       # Additional CSS/JS
```

### Current Features

1. **Video Grid with Hover Previews**
   - Thumbnail images as backgrounds
   - 5-second preview videos on hover
   - Category filtering (Film, Commercial, Automotive, Photography)
   - Responsive grid layout (some cards 2x2 "large")

2. **Project Pages**
   - Embedded Vimeo players
   - Project details and credits
   - Prev/Next navigation
   - Category-aware navigation

3. **Photography Gallery**
   - 20 images in 3-column grid
   - Responsive layout

4. **Information Overlay**
   - Contact details
   - Representation info
   - Shared across all pages

### Technology Stack (Current)

- Pure HTML/CSS/JavaScript (no frameworks)
- Vanilla JS for filtering
- Local preview videos (media/previews/)
- Embedded Vimeo for full playback
- Static file hosting

### Performance Metrics (Current)

- **Total site size**: ~10MB (with all media)
- **Preview videos**: 41KB - 425KB each (avg 165KB)
- **Page load**: Instant (static HTML)
- **Hosting**: Any static host (GitHub Pages, Netlify, etc.)

---

## Why Kirby CMS?

### Advantages

1. **Content Management**
   - Visual Panel interface for editing
   - No HTML editing required for content updates
   - Structured fields prevent inconsistencies
   - Preview before publishing

2. **Code Maintainability**
   - One template serves all project pages (vs 31 duplicate HTML files)
   - Centralized structure changes
   - Separation of content and presentation

3. **Developer Experience**
   - Clean, organized content structure
   - Version control friendly (text files)
   - No build process required
   - Extensive plugin ecosystem

4. **Scalability**
   - Easy to add new projects
   - Built-in search if needed
   - Multi-language support available
   - REST API for external integrations

5. **Performance** (with caching)
   - Static cache plugin matches static HTML speed
   - Built-in image optimization
   - CDN-ready

### Trade-offs

1. **Complexity**: Requires PHP hosting (vs static file hosting)
2. **Cost**: €99 one-time license
3. **Learning curve**: Kirby conventions and PHP basics
4. **Hosting requirements**: PHP 8.0+ server

### Decision Factors

**Proceed with migration if**:
- Adding projects regularly (monthly/quarterly)
- Want easier content management
- Planning to scale portfolio significantly
- Want features like search or multi-language
- Interested in learning modern flat-file CMS

**Stay with static HTML if**:
- Updates are rare (few times per year)
- Comfortable with HTML editing
- Want maximum simplicity
- Don't want ongoing costs beyond hosting

---

## Target Kirby Architecture

### Directory Structure

```
/Users/justinhenning/code/website-kirby/
├── kirby/                        # Kirby core (4.5MB)
├── site/                         # Your custom code
│   ├── blueprints/               # Content structure definitions (YAML)
│   │   ├── site.yml              # Site-wide settings
│   │   ├── pages/
│   │   │   ├── home.yml          # Homepage/grid blueprint
│   │   │   ├── project.yml       # Project page blueprint
│   │   │   └── photography.yml   # Photography page blueprint
│   │   └── files/
│   │       ├── thumbnail.yml     # Thumbnail metadata
│   │       └── preview.yml       # Preview video metadata
│   ├── templates/                # PHP templates for rendering
│   │   ├── home.php              # Portfolio grid template
│   │   ├── project.php           # Individual project template
│   │   └── photography.php       # Photography gallery template
│   ├── snippets/                 # Reusable components
│   │   ├── header.php            # Site header
│   │   ├── footer.php            # Site footer
│   │   ├── info-overlay.php      # Information panel
│   │   └── project-navigation.php # Prev/Next navigation
│   ├── controllers/              # PHP logic (optional)
│   │   └── home.php              # Grid filtering logic
│   ├── config/
│   │   └── config.php            # Site configuration
│   └── plugins/                  # Custom plugins (if needed)
├── content/                      # All content and media
│   ├── site.txt                  # Site-wide content
│   ├── home/
│   │   └── home.txt              # Homepage settings
│   ├── projects/                 # Projects folder
│   │   ├── your-lucky-day/
│   │   │   ├── project.txt       # Project metadata
│   │   │   ├── thumbnail.jpg     # Thumbnail image
│   │   │   └── preview.mp4       # Preview video
│   │   ├── woodford-reserve/
│   │   │   ├── project.txt
│   │   │   ├── thumbnail.jpg
│   │   │   └── preview.mp4
│   │   └── [... 14 more projects]
│   └── photography/
│       ├── photography.txt
│       └── [001.jpg - 020.jpg]   # 20 photos
├── media/                        # Auto-generated (thumbnails cache)
├── assets/                       # CSS, JS, fonts
│   ├── css/
│   │   ├── style.css
│   │   └── photography.css
│   └── js/
│       └── script.js
└── index.php                     # Kirby entry point
```

### URL Structure

```
Current                           Kirby
--------------------------------------------------------------------------------------------------
/index.html                    →  / (or /home)
/projects/kia.html             →  /projects/kia
/photography.html              →  /photography

# With filtering
Current: /#automotive          →  Kirby: /projects/filter:automotive (or JS filtering)
```

### Content File Format

Kirby uses plain text files with a simple structure:

```
Title: Project Name
----
Field2: Value
----
Field3: Multiple
line
value
```

---

## Complete Data Mapping

### Project Metadata Extraction

From current `script.js` and project HTML files, here's the complete data for all 16 projects:

#### 1. Your Lucky Day
```yaml
Slug: your-lucky-day
Title: Your Lucky Day
Category: film
VimeoId: 872749030
Year: 2023
IsLarge: false
Description: |
  A tense thriller following a group of people caught in a convenience store after a lottery ticket dispute turns deadly.
Credits:
  - role: Director
    name: Dan Brown
  - role: DP
    name: Justin Henning
  - role: Production Company
    name: BuzzFeed Studios
```

#### 2. Woodford Reserve
```yaml
Slug: woodford-reserve
Title: Woodford Reserve
Category: commercial
VimeoId: 898398761
Year: 2023
IsLarge: false
Description: |
  Premium whiskey brand commercial showcasing craftsmanship and tradition.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
```

#### 3. Huawei
```yaml
Slug: huawei
Title: Huawei
Category: commercial
VimeoId: 1046541141
Year: 2024
IsLarge: true
Description: |
  Technology brand commercial highlighting innovation and connectivity.
Credits:
  - role: Director
    name: TBD
  - role: DP
    name: Justin Henning
```

#### 4. KIA
```yaml
Slug: kia
Title: KIA
Subtitle: Good Life
Category: automotive
VimeoId: 913839989
Year: 2023
IsLarge: false
Description: |
  Automotive commercial for KIA showcasing lifestyle and adventure.
Credits:
  - role: Director
    name: Brent Foster
  - role: DP
    name: Justin Henning
```

#### 5. Royal Bank of Canada
```yaml
Slug: rbc
Title: Royal Bank of Canada
Subtitle: WIND
Category: commercial
VimeoId: 891284220
Year: 2023
IsLarge: false
Description: |
  Financial services commercial for RBC.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
```

#### 6. K&N
```yaml
Slug: kn
Title: K&N
Category: automotive
VimeoId: 523316278
Year: 2020
IsLarge: false
Description: |
  Performance automotive parts commercial.
Credits:
  - role: Director
    name: Miko Lim
  - role: DP
    name: Justin Henning
```

#### 7. RAM
```yaml
Slug: ram
Title: RAM
Subtitle: Paraglider
Category: automotive
VimeoId: 930752804
Year: 2023
IsLarge: true
Description: |
  Automotive commercial for RAM trucks featuring extreme sports.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
```

#### 8. Audi
```yaml
Slug: audi
Title: Audi
Subtitle: Listen
Category: automotive
VimeoId: 163036231
Year: 2016
IsLarge: false
Description: |
  Premium automotive commercial for Audi.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
```

#### 9. Jeep
```yaml
Slug: jeep
Title: Jeep
Subtitle: Hero's Journey
Category: automotive
VimeoId: 898405588
Year: 2023
IsLarge: false
Description: |
  Adventure-focused automotive commercial for Jeep.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
```

#### 10. Ford
```yaml
Slug: ford
Title: Ford
Subtitle: Expedition
Category: automotive
VimeoId: 745033991
Year: 2022
IsLarge: false
Description: |
  Automotive commercial for Ford Expedition.
Credits:
  - role: Director
    name: Scott Weintrob
  - role: DP
    name: Justin Henning
```

#### 11. American Outlaws
```yaml
Slug: american-outlaws
Title: American Outlaws
Category: film
VimeoId: 797538936
Year: 2023
IsLarge: false
Description: |
  Action film trailer.
Credits:
  - role: Director
    name: TBD
  - role: DP
    name: Justin Henning
```

#### 12. PEI
```yaml
Slug: pei
Title: PEI
Category: commercial
VimeoId: 374024991
Year: 2019
IsLarge: true
Description: |
  Tourism commercial for Prince Edward Island.
Credits:
  - role: Director
    name: Brent Foster
  - role: DP
    name: Justin Henning
```

#### 13. Lamborghini
```yaml
Slug: lamborghini
Title: Lamborghini
Subtitle: Wind
Category: automotive
VimeoId: 242791079
Year: 2017
IsLarge: false
Description: |
  Luxury automotive commercial for Lamborghini.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
```

#### 14. Nikon
```yaml
Slug: nikon
Title: Nikon
Subtitle: Clark Little
Category: commercial
VimeoId: [UNKNOWN]
Year: [UNKNOWN]
IsLarge: false
Description: |
  Camera equipment commercial featuring photographer Clark Little.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
Note: Need to verify Vimeo ID from existing HTML
```

#### 15. Ralph Lauren
```yaml
Slug: ralph-lauren
Title: Ralph Lauren
Subtitle: Blue
Category: commercial
VimeoId: 261889797
Year: 2017
IsLarge: false
Description: |
  Fashion commercial for Ralph Lauren Polo Blue fragrance.
Credits:
  - role: Director
    name: David Holm
  - role: DP
    name: Justin Henning
```

#### 16. Gatorade
```yaml
Slug: gatorade
Title: Gatorade
Category: commercial
VimeoId: 1046557409
Year: 2024
IsLarge: false
Description: |
  Sports drink commercial.
Credits:
  - role: Director
    name: TBD
  - role: DP
    name: Justin Henning
Note: No local video file - Vimeo embed only
```

### Site-Wide Content

```yaml
# site.txt
Title: Justin Henning
Subtitle: Cinematographer
Email: henning.justin@gmail.com
Instagram: justinthenning
InstagramUrl: https://instagram.com/justinthenning

# Representation
RepUsaName: WPA USA
RepUsaContacts: Steven, Kristen Billings, Louiza Vick
RepUsaEmail: [if available]

RepUkName: WPA London
RepUkContact: Barnaby Laws
RepUkEmail: [if available]

RepLatamName: 9AM
RepLatamContact: Rodrigo Gavaldón
RepLatamEmail: [if available]
```

---

## Implementation Phases

### Phase 0: Setup & Preparation (1-2 hours)

**Objective**: Install Kirby locally and understand structure

1. **Download Kirby**
   ```bash
   # Create new directory
   mkdir ~/code/website-kirby
   cd ~/code/website-kirby

   # Download Kirby Starterkit
   curl -L https://github.com/getkirby/starterkit/archive/main.zip -o kirby.zip
   unzip kirby.zip
   mv starterkit-main/* .
   rm -rf starterkit-main kirby.zip
   ```

2. **Start local server**
   ```bash
   php -S localhost:8000
   # Visit http://localhost:8000/panel
   # Create admin account
   ```

3. **Explore Starterkit**
   - Browse /content folder structure
   - Open /site/blueprints examples
   - View /site/templates examples
   - Test Panel interface at /panel

4. **Version Control**
   ```bash
   git init
   git add .
   git commit -m "Initial Kirby installation"
   ```

**Deliverables**:
- ✅ Kirby installed and running locally
- ✅ Panel admin account created
- ✅ Basic structure understood
- ✅ Git repository initialized

---

### Phase 1: Site Structure & Blueprints (4-6 hours)

**Objective**: Define content structure and Panel interface

#### 1.1: Clean Starterkit Content

```bash
# Remove example content
rm -rf content/*

# Remove example blueprints
rm -rf site/blueprints/*

# Remove example templates (keep default.php as fallback)
rm -rf site/templates/*
```

#### 1.2: Create Site Blueprint

**File**: `site/blueprints/site.yml`

```yaml
title: Site Settings
icon: 🏠

fields:
  siteInfo:
    type: fields
    label: Site Information
    fields:
      title:
        type: text
        label: Site Title
        default: Justin Henning
      subtitle:
        type: text
        label: Subtitle
        default: Cinematographer

  contactInfo:
    type: fields
    label: Contact Information
    fields:
      email:
        type: email
        label: Email
      instagram:
        type: text
        label: Instagram Handle
        placeholder: "@username"
      instagramUrl:
        type: url
        label: Instagram URL

  representation:
    type: fields
    label: Representation
    fields:
      repUsa:
        type: structure
        label: USA Representation
        fields:
          name:
            type: text
            label: Company Name
          contacts:
            type: text
            label: Contacts
          email:
            type: email
            label: Email
      repUk:
        type: structure
        label: UK Representation
        fields:
          name:
            type: text
          contact:
            type: text
          email:
            type: email
      repLatam:
        type: structure
        label: Latin America Representation
        fields:
          name:
            type: text
          contact:
            type: text
          email:
            type: email
```

#### 1.3: Create Home Blueprint

**File**: `site/blueprints/pages/home.yml`

```yaml
title: Home / Portfolio Grid
icon: 📽️
preset: page

options:
  changeSlug: false
  changeStatus: false
  delete: false

columns:
  - width: 2/3
    fields:
      intro:
        type: textarea
        label: Introduction Text
        help: Optional intro text above the grid

      featuredProjects:
        type: pages
        label: Featured Projects
        query: page.siblings.filterBy('template', 'project')
        help: Leave empty to show all projects

  - width: 1/3
    fields:
      seo:
        type: fields
        label: SEO
        fields:
          metaTitle:
            type: text
            label: Meta Title
          metaDescription:
            type: textarea
            label: Meta Description
            maxlength: 160
```

#### 1.4: Create Project Blueprint

**File**: `site/blueprints/pages/project.yml`

```yaml
title: Project
icon: 🎬
num: zero

status:
  draft:
    label: Draft
    text: Project is in draft mode
  unlisted:
    label: Unlisted
    text: Project is unlisted
  listed:
    label: Published
    text: Project is published and visible

columns:
  main:
    width: 2/3
    fields:
      projectInfo:
        type: fields
        label: Project Information
        fields:
          title:
            type: text
            label: Title
            required: true

          subtitle:
            type: text
            label: Subtitle
            help: Optional subtitle (e.g., "Good Life" for KIA)

          category:
            type: select
            label: Category
            required: true
            options:
              film: Film
              commercial: Commercial
              automotive: Automotive

          year:
            type: number
            label: Year
            min: 2000
            max: 2030
            step: 1

          vimeoid:
            type: text
            label: Vimeo ID
            required: true
            help: Just the numeric ID (e.g., 913839989)

          description:
            type: textarea
            label: Description
            size: large

          islarge:
            type: toggle
            label: Large Grid Tile
            help: Display as 2x2 tile on homepage grid
            default: false

      credits:
        type: structure
        label: Credits
        fields:
          role:
            type: text
            label: Role
            placeholder: Director, DP, Producer, etc.
          name:
            type: text
            label: Name

  sidebar:
    width: 1/3
    fields:
      media:
        type: fields
        label: Media Files
        fields:
          thumbnail:
            type: files
            label: Thumbnail
            max: 1
            accept:
              - image/jpeg
              - image/png
              - image/webp
            help: Static thumbnail for grid (JPG recommended)

          preview:
            type: files
            label: Preview Video
            max: 1
            accept:
              - video/mp4
              - video/mov
            help: 5-second hover preview clip

      seo:
        type: fields
        label: SEO
        fields:
          metaTitle:
            type: text
            label: Meta Title
          metaDescription:
            type: textarea
            label: Meta Description
            maxlength: 160
```

#### 1.5: Create Photography Blueprint

**File**: `site/blueprints/pages/photography.yml`

```yaml
title: Photography
icon: 📷

options:
  changeSlug: false
  changeStatus: false
  delete: false

columns:
  - width: 2/3
    fields:
      intro:
        type: textarea
        label: Introduction
        help: Optional intro text

      images:
        type: files
        label: Gallery Images
        layout: cards
        size: small
        accept:
          - image/jpeg
          - image/png
          - image/webp

  - width: 1/3
    fields:
      seo:
        type: fields
        label: SEO
        fields:
          metaTitle:
            type: text
            label: Meta Title
          metaDescription:
            type: textarea
            label: Meta Description
```

#### 1.6: Create File Blueprints (Optional but Recommended)

**File**: `site/blueprints/files/thumbnail.yml`

```yaml
title: Thumbnail Image
accept:
  - image/jpeg
  - image/png
  - image/webp

fields:
  alt:
    type: text
    label: Alt Text
    help: Describe the image for accessibility
```

**File**: `site/blueprints/files/preview.yml`

```yaml
title: Preview Video
accept:
  - video/mp4
  - video/mov

fields:
  caption:
    type: text
    label: Caption
```

**Deliverables**:
- ✅ All blueprints created
- ✅ Panel interface structured
- ✅ Content types defined

---

### Phase 2: Content Migration (3-4 hours)

**Objective**: Migrate all projects and content to Kirby structure

#### 2.1: Create Content Structure

```bash
cd content

# Create main pages
mkdir home
mkdir photography
mkdir projects

# Create all project folders
mkdir projects/your-lucky-day
mkdir projects/woodford-reserve
mkdir projects/huawei
mkdir projects/kia
mkdir projects/rbc
mkdir projects/kn
mkdir projects/ram
mkdir projects/audi
mkdir projects/jeep
mkdir projects/ford
mkdir projects/american-outlaws
mkdir projects/pei
mkdir projects/lamborghini
mkdir projects/nikon
mkdir projects/ralph-lauren
mkdir projects/gatorade
```

#### 2.2: Create Site Content File

**File**: `content/site.txt`

```
Title: Justin Henning
----
Subtitle: Cinematographer
----
Email: henning.justin@gmail.com
----
Instagram: justinthenning
----
Instagramurl: https://instagram.com/justinthenning
----
Repusa:

-
  name: WPA USA
  contacts: Steven, Kristen Billings, Louiza Vick
  email:
----
Repuk:

-
  name: WPA London
  contact: Barnaby Laws
  email:
----
Replatam:

-
  name: 9AM
  contact: Rodrigo Gavaldón
  email:
```

#### 2.3: Create Home Page Content

**File**: `content/home/home.txt`

```
Title: Portfolio
----
Intro:
```

#### 2.4: Create Project Content Files

**Template for each project** (example: `content/projects/kia/project.txt`):

```
Title: KIA
----
Subtitle: Good Life
----
Category: automotive
----
Year: 2023
----
Vimeoid: 913839989
----
Description: Automotive commercial for KIA showcasing lifestyle and adventure.
----
Islarge: false
----
Credits:

-
  role: Director
  name: Brent Foster
-
  role: DP
  name: Justin Henning
```

**Migration Script** (to automate content file creation):

Create `scripts/create-kirby-content.py`:

```python
#!/usr/bin/env python3
"""
Generate Kirby content files from project data
"""

projects = [
    {
        "slug": "your-lucky-day",
        "title": "Your Lucky Day",
        "subtitle": "",
        "category": "film",
        "vimeoid": "872749030",
        "year": "2023",
        "islarge": "false",
        "description": "A tense thriller following a group of people caught in a convenience store after a lottery ticket dispute turns deadly.",
        "credits": [
            {"role": "Director", "name": "Dan Brown"},
            {"role": "DP", "name": "Justin Henning"},
            {"role": "Production Company", "name": "BuzzFeed Studios"}
        ]
    },
    {
        "slug": "woodford-reserve",
        "title": "Woodford Reserve",
        "subtitle": "",
        "category": "commercial",
        "vimeoid": "898398761",
        "year": "2023",
        "islarge": "false",
        "description": "Premium whiskey brand commercial showcasing craftsmanship and tradition.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "huawei",
        "title": "Huawei",
        "subtitle": "",
        "category": "commercial",
        "vimeoid": "1046541141",
        "year": "2024",
        "islarge": "true",
        "description": "Technology brand commercial highlighting innovation and connectivity.",
        "credits": [
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "kia",
        "title": "KIA",
        "subtitle": "Good Life",
        "category": "automotive",
        "vimeoid": "913839989",
        "year": "2023",
        "islarge": "false",
        "description": "Automotive commercial for KIA showcasing lifestyle and adventure.",
        "credits": [
            {"role": "Director", "name": "Brent Foster"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "rbc",
        "title": "Royal Bank of Canada",
        "subtitle": "WIND",
        "category": "commercial",
        "vimeoid": "891284220",
        "year": "2023",
        "islarge": "false",
        "description": "Financial services commercial for RBC.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "kn",
        "title": "K&N",
        "subtitle": "",
        "category": "automotive",
        "vimeoid": "523316278",
        "year": "2020",
        "islarge": "false",
        "description": "Performance automotive parts commercial.",
        "credits": [
            {"role": "Director", "name": "Miko Lim"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "ram",
        "title": "RAM",
        "subtitle": "Paraglider",
        "category": "automotive",
        "vimeoid": "930752804",
        "year": "2023",
        "islarge": "true",
        "description": "Automotive commercial for RAM trucks featuring extreme sports.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "audi",
        "title": "Audi",
        "subtitle": "Listen",
        "category": "automotive",
        "vimeoid": "163036231",
        "year": "2016",
        "islarge": "false",
        "description": "Premium automotive commercial for Audi.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "jeep",
        "title": "Jeep",
        "subtitle": "Hero's Journey",
        "category": "automotive",
        "vimeoid": "898405588",
        "year": "2023",
        "islarge": "false",
        "description": "Adventure-focused automotive commercial for Jeep.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "ford",
        "title": "Ford",
        "subtitle": "Expedition",
        "category": "automotive",
        "vimeoid": "745033991",
        "year": "2022",
        "islarge": "false",
        "description": "Automotive commercial for Ford Expedition.",
        "credits": [
            {"role": "Director", "name": "Scott Weintrob"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "american-outlaws",
        "title": "American Outlaws",
        "subtitle": "",
        "category": "film",
        "vimeoid": "797538936",
        "year": "2023",
        "islarge": "false",
        "description": "Action film trailer.",
        "credits": [
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "pei",
        "title": "PEI",
        "subtitle": "",
        "category": "commercial",
        "vimeoid": "374024991",
        "year": "2019",
        "islarge": "true",
        "description": "Tourism commercial for Prince Edward Island.",
        "credits": [
            {"role": "Director", "name": "Brent Foster"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "lamborghini",
        "title": "Lamborghini",
        "subtitle": "Wind",
        "category": "automotive",
        "vimeoid": "242791079",
        "year": "2017",
        "islarge": "false",
        "description": "Luxury automotive commercial for Lamborghini.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "nikon",
        "title": "Nikon",
        "subtitle": "Clark Little",
        "category": "commercial",
        "vimeoid": "VERIFY_FROM_HTML",
        "year": "VERIFY_FROM_HTML",
        "islarge": "false",
        "description": "Camera equipment commercial featuring photographer Clark Little.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "ralph-lauren",
        "title": "Ralph Lauren",
        "subtitle": "Blue",
        "category": "commercial",
        "vimeoid": "261889797",
        "year": "2017",
        "islarge": "false",
        "description": "Fashion commercial for Ralph Lauren Polo Blue fragrance.",
        "credits": [
            {"role": "Director", "name": "David Holm"},
            {"role": "DP", "name": "Justin Henning"}
        ]
    },
    {
        "slug": "gatorade",
        "title": "Gatorade",
        "subtitle": "",
        "category": "commercial",
        "vimeoid": "1046557409",
        "year": "2024",
        "islarge": "false",
        "description": "Sports drink commercial.",
        "credits": [
            {"role": "DP", "name": "Justin Henning"}
        ]
    }
]

def format_credits(credits):
    """Format credits as Kirby structure field"""
    if not credits:
        return ""

    lines = []
    for credit in credits:
        lines.append("- ")
        lines.append(f"  role: {credit['role']}")
        lines.append(f"  name: {credit['name']}")

    return "\n".join(lines)

def create_project_file(project):
    """Create a Kirby content file for a project"""
    content = f"""Title: {project['title']}
----
Subtitle: {project['subtitle']}
----
Category: {project['category']}
----
Year: {project['year']}
----
Vimeoid: {project['vimeoid']}
----
Description: {project['description']}
----
Islarge: {project['islarge']}
----
Credits:

{format_credits(project['credits'])}
"""

    filename = f"content/projects/{project['slug']}/project.txt"
    with open(filename, 'w') as f:
        f.write(content)

    print(f"✅ Created {filename}")

# Main execution
if __name__ == "__main__":
    import os

    # Ensure projects directory exists
    os.makedirs("content/projects", exist_ok=True)

    for project in projects:
        # Create project folder
        folder = f"content/projects/{project['slug']}"
        os.makedirs(folder, exist_ok=True)

        # Create content file
        create_project_file(project)

    print(f"\n✅ Created {len(projects)} project content files")
    print("\n⚠️  TODO: Verify Nikon project data from existing HTML")
    print("⚠️  TODO: Copy media files to project folders (next step)")
```

Run the script:
```bash
chmod +x scripts/create-kirby-content.py
python3 scripts/create-kirby-content.py
```

#### 2.5: Migrate Media Files

**Copy thumbnails and previews to project folders**:

```bash
#!/bin/bash
# scripts/migrate-media-files.sh

# Map of old filenames to project slugs
declare -A media_map=(
    ["your-lucky-day"]="your-lucky-day"
    ["woodford-reserve"]="woodford-reserve"
    ["huawei"]="huawei"
    ["kia"]="kia"
    ["rbc"]="rbc"
    ["kn"]="kn"
    ["ram"]="ram"
    ["audi"]="audi"
    ["jeep"]="jeep"
    ["ford"]="ford"
    ["american-outlaws"]="american-outlaws"
    ["pei"]="pei"
    ["lamborghini"]="lamborghini"
    ["nikon"]="nikon"
    ["ralph-lauren"]="ralph-lauren"
    ["gatorade"]="gatorade"
)

# Copy thumbnails
for slug in "${!media_map[@]}"; do
    if [ -f "../website/media/thumbnails/${slug}.jpg" ]; then
        cp "../website/media/thumbnails/${slug}.jpg" "content/projects/${slug}/thumbnail.jpg"
        echo "✅ Copied thumbnail for ${slug}"
    else
        echo "⚠️  Missing thumbnail for ${slug}"
    fi
done

# Copy preview videos
for slug in "${!media_map[@]}"; do
    if [ -f "../website/media/previews/${slug}.mp4" ]; then
        cp "../website/media/previews/${slug}.mp4" "content/projects/${slug}/preview.mp4"
        echo "✅ Copied preview for ${slug}"
    else
        echo "⚠️  Missing preview for ${slug}"
    fi
done

# Copy photography images
mkdir -p content/photography
cp ../website/media/photography/*.jpg content/photography/
echo "✅ Copied photography images"

echo ""
echo "Media migration complete!"
```

Run the script:
```bash
chmod +x scripts/migrate-media-files.sh
./scripts/migrate-media-files.sh
```

#### 2.6: Create Photography Content

**File**: `content/photography/photography.txt`

```
Title: Photography
----
Intro: A collection of personal photography work from New York City.
```

**Deliverables**:
- ✅ All content files created
- ✅ All media files migrated
- ✅ Site structure complete
- ✅ Panel interface populated

---

### Phase 3: Templates & Frontend (6-8 hours)

**Objective**: Build PHP templates matching current design

#### 3.1: Copy Assets

```bash
# Copy CSS and JS from current site
mkdir -p assets/css
mkdir -p assets/js

cp ../website/style.css assets/css/
cp ../website/photography-style.css assets/css/
cp ../website/script.js assets/js/
```

#### 3.2: Create Header Snippet

**File**: `site/snippets/header.php`

```php
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title><?= $page->isHomePage() ? $site->title() : $page->title() . ' | ' . $site->title() ?></title>

  <?php if($metaDescription = $page->metaDescription()->or($site->description())): ?>
  <meta name="description" content="<?= $metaDescription ?>">
  <?php endif ?>

  <?= css('assets/css/style.css') ?>
  <?php if($page->template() == 'photography'): ?>
    <?= css('assets/css/photography-style.css') ?>
  <?php endif ?>
</head>
<body>

  <header class="site-header">
    <a href="<?= $site->url() ?>" class="logo"><?= $site->title() ?></a>

    <button class="info-toggle" aria-label="Toggle information">i</button>
  </header>
```

#### 3.3: Create Footer Snippet

**File**: `site/snippets/footer.php`

```php
  <?php snippet('info-overlay') ?>

  <?= js('assets/js/script.js') ?>
</body>
</html>
```

#### 3.4: Create Info Overlay Snippet

**File**: `site/snippets/info-overlay.php`

```php
<div class="info-overlay" id="info-overlay">
  <div class="info-content">
    <button class="info-close" aria-label="Close">&times;</button>

    <h2><?= $site->title() ?></h2>
    <?php if($site->subtitle()->isNotEmpty()): ?>
      <p class="subtitle"><?= $site->subtitle() ?></p>
    <?php endif ?>

    <div class="info-section">
      <h3>Contact</h3>
      <p>
        <?php if($site->email()->isNotEmpty()): ?>
          <a href="mailto:<?= $site->email() ?>"><?= $site->email() ?></a><br>
        <?php endif ?>
        <?php if($site->instagramUrl()->isNotEmpty()): ?>
          <a href="<?= $site->instagramUrl() ?>" target="_blank"><?= $site->instagram() ?></a>
        <?php endif ?>
      </p>
    </div>

    <?php if($repUsa = $site->repUsa()->toStructure()->first()): ?>
    <div class="info-section">
      <h3>US Representation</h3>
      <p>
        <strong><?= $repUsa->name() ?></strong><br>
        <?= $repUsa->contacts() ?><br>
        <?php if($repUsa->email()->isNotEmpty()): ?>
          <a href="mailto:<?= $repUsa->email() ?>"><?= $repUsa->email() ?></a>
        <?php endif ?>
      </p>
    </div>
    <?php endif ?>

    <?php if($repUk = $site->repUk()->toStructure()->first()): ?>
    <div class="info-section">
      <h3>UK Representation</h3>
      <p>
        <strong><?= $repUk->name() ?></strong><br>
        <?= $repUk->contact() ?><br>
        <?php if($repUk->email()->isNotEmpty()): ?>
          <a href="mailto:<?= $repUk->email() ?>"><?= $repUk->email() ?></a>
        <?php endif ?>
      </p>
    </div>
    <?php endif ?>

    <?php if($repLatam = $site->repLatam()->toStructure()->first()): ?>
    <div class="info-section">
      <h3>Mexico & Latin America</h3>
      <p>
        <strong><?= $repLatam->name() ?></strong><br>
        <?= $repLatam->contact() ?><br>
        <?php if($repLatam->email()->isNotEmpty()): ?>
          <a href="mailto:<?= $repLatam->email() ?>"><?= $repLatam->email() ?></a>
        <?php endif ?>
      </p>
    </div>
    <?php endif ?>
  </div>
</div>
```

#### 3.5: Create Home Template

**File**: `site/templates/home.php`

```php
<?php snippet('header') ?>

<?php if($page->intro()->isNotEmpty()): ?>
  <div class="intro">
    <?= $page->intro()->kt() ?>
  </div>
<?php endif ?>

<div class="grid">
  <?php
  // Get all projects
  $projects = page('projects')->children()->listed()->sortBy('num', 'asc');

  foreach($projects as $project):
    $thumbnail = $project->images()->filterBy('filename', 'thumbnail')->first();
    $preview = $project->videos()->filterBy('filename', 'preview')->first();
    $largeClass = $project->islarge()->isTrue() ? ' large' : '';
  ?>

    <a href="<?= $project->url() ?>"
       class="project-card<?= $largeClass ?>"
       data-category="<?= $project->category() ?>"
       <?php if($thumbnail): ?>
       style="background-image: url('<?= $thumbnail->url() ?>')"
       <?php endif ?>>

      <?php if($preview): ?>
      <video
        src="<?= $preview->url() ?>"
        loop
        muted
        playsinline
        preload="none">
      </video>
      <?php endif ?>

      <div class="project-info">
        <h3><?= $project->title() ?></h3>
        <?php if($project->subtitle()->isNotEmpty()): ?>
          <span class="subtitle"><?= $project->subtitle() ?></span>
        <?php endif ?>
      </div>
    </a>

  <?php endforeach ?>

  <!-- Photography card -->
  <a href="<?= page('photography')->url() ?>"
     class="project-card"
     data-category="photography"
     style="background-image: url('<?= page('photography')->images()->first()->url() ?>')">
    <div class="project-info">
      <h3>Photography</h3>
    </div>
  </a>
</div>

<?php snippet('footer') ?>
```

#### 3.6: Create Project Template

**File**: `site/templates/project.php`

```php
<?php snippet('header') ?>

<div class="project-page">

  <div class="video-container">
    <?php if($page->vimeoid()->isNotEmpty()): ?>
      <iframe
        src="https://player.vimeo.com/video/<?= $page->vimeoid() ?>?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
        frameborder="0"
        allow="autoplay; fullscreen; picture-in-picture; clipboard-write"
        allowfullscreen
        title="<?= $page->title() ?>">
      </iframe>
    <?php endif ?>
  </div>

  <div class="project-details">
    <h1><?= $page->title() ?></h1>
    <?php if($page->subtitle()->isNotEmpty()): ?>
      <h2 class="subtitle"><?= $page->subtitle() ?></h2>
    <?php endif ?>

    <p class="category"><?= ucfirst($page->category()) ?></p>

    <?php if($page->year()->isNotEmpty()): ?>
      <p class="year"><?= $page->year() ?></p>
    <?php endif ?>

    <?php if($page->description()->isNotEmpty()): ?>
      <div class="description">
        <?= $page->description()->kt() ?>
      </div>
    <?php endif ?>

    <?php if($page->credits()->toStructure()->isNotEmpty()): ?>
      <div class="credits">
        <h3>Credits</h3>
        <?php foreach($page->credits()->toStructure() as $credit): ?>
          <p>
            <strong><?= $credit->role() ?>:</strong> <?= $credit->name() ?>
          </p>
        <?php endforeach ?>
      </div>
    <?php endif ?>
  </div>

  <?php snippet('project-navigation', ['project' => $page]) ?>

</div>

<?php snippet('footer') ?>
```

#### 3.7: Create Project Navigation Snippet

**File**: `site/snippets/project-navigation.php`

```php
<?php
// Get all projects
$projects = page('projects')->children()->listed()->sortBy('num', 'asc');

// Find current project index
$currentIndex = 0;
$total = $projects->count();

foreach($projects as $index => $p) {
  if($p->id() == $project->id()) {
    $currentIndex = $index;
    break;
  }
}

// Get prev/next
$prevProject = $currentIndex > 0 ? $projects->nth($currentIndex - 1) : $projects->last();
$nextProject = $currentIndex < $total - 1 ? $projects->nth($currentIndex + 1) : $projects->first();
?>

<nav class="project-navigation">
  <?php if($prevProject): ?>
    <a href="<?= $prevProject->url() ?>" class="nav-prev">
      ← Previous
      <span class="nav-title"><?= $prevProject->title() ?></span>
    </a>
  <?php endif ?>

  <a href="<?= page('home')->url() ?>" class="nav-home">
    Grid
  </a>

  <?php if($nextProject): ?>
    <a href="<?= $nextProject->url() ?>" class="nav-next">
      Next →
      <span class="nav-title"><?= $nextProject->title() ?></span>
    </a>
  <?php endif ?>
</nav>
```

#### 3.8: Create Photography Template

**File**: `site/templates/photography.php`

```php
<?php snippet('header') ?>

<div class="photography-page">

  <?php if($page->intro()->isNotEmpty()): ?>
    <div class="intro">
      <?= $page->intro()->kt() ?>
    </div>
  <?php endif ?>

  <div class="photography-grid">
    <?php foreach($page->images()->sortBy('filename', 'asc') as $image): ?>
      <div class="photo-item">
        <img
          src="<?= $image->url() ?>"
          alt="<?= $image->alt() ?>"
          loading="lazy">
      </div>
    <?php endforeach ?>
  </div>

  <div class="back-link">
    <a href="<?= page('home')->url() ?>">← Back to Portfolio</a>
  </div>

</div>

<?php snippet('footer') ?>
```

#### 3.9: Update JavaScript for Kirby

**File**: `assets/js/script.js`

Update any hard-coded selectors or paths if needed. The existing hover logic should work as-is since the HTML structure will be similar.

**Deliverables**:
- ✅ All templates created
- ✅ All snippets created
- ✅ Assets migrated
- ✅ Frontend matches current design

---

### Phase 4: Configuration & Routing (2-3 hours)

**Objective**: Configure Kirby and implement category filtering

#### 4.1: Create Main Config

**File**: `site/config/config.php`

```php
<?php

return [
    'debug' => true, // Set to false in production

    // Homepage routing
    'home' => 'home',

    // Panel settings
    'panel' => [
        'install' => true,
        'slug' => 'panel'
    ],

    // Cache settings
    'cache' => [
        'pages' => [
            'active' => true,
            'type' => 'file'
        ]
    ],

    // Thumbs settings for image processing
    'thumbs' => [
        'quality' => 85,
        'presets' => [
            'default' => ['width' => 1024, 'quality' => 85],
            'thumbnail' => ['width' => 640, 'height' => 360, 'crop' => true],
            'photography' => ['width' => 1200, 'quality' => 90]
        ]
    ],

    // Routes for filtering
    'routes' => [
        [
            'pattern' => '/',
            'action' => function() {
                return page('home');
            }
        ],
        [
            'pattern' => 'filter/(:any)',
            'action' => function($category) {
                $home = page('home');
                return $home->render([
                    'filter' => $category
                ]);
            }
        ]
    ]
];
```

#### 4.2: Create Home Controller (for filtering)

**File**: `site/controllers/home.php`

```php
<?php

return function($page, $kirby) {
    // Get filter from URL or query parameter
    $filter = $kirby->request()->get('filter') ?? get('filter');

    // Get all projects
    $projects = page('projects')->children()->listed();

    // Apply filter if set
    if($filter && $filter !== 'all') {
        $projects = $projects->filterBy('category', $filter);
    }

    // Get unique categories for filter buttons
    $categories = page('projects')
        ->children()
        ->listed()
        ->pluck('category', null, true);

    return [
        'projects' => $projects,
        'categories' => $categories,
        'currentFilter' => $filter ?? 'all'
    ];
};
```

#### 4.3: Update Home Template with Filter Buttons

Update `site/templates/home.php` to add filter controls:

```php
<?php snippet('header') ?>

<?php if($page->intro()->isNotEmpty()): ?>
  <div class="intro">
    <?= $page->intro()->kt() ?>
  </div>
<?php endif ?>

<!-- Category Filters -->
<nav class="category-filters">
  <button class="filter-btn <?= $currentFilter == 'all' ? 'active' : '' ?>"
          data-filter="all">
    All
  </button>
  <?php foreach($categories as $cat): ?>
    <button class="filter-btn <?= $currentFilter == $cat ? 'active' : '' ?>"
            data-filter="<?= $cat ?>">
      <?= ucfirst($cat) ?>
    </button>
  <?php endforeach ?>
  <button class="filter-btn <?= $currentFilter == 'photography' ? 'active' : '' ?>"
          data-filter="photography">
    Photography
  </button>
</nav>

<div class="grid">
  <?php foreach($projects as $project):
    $thumbnail = $project->images()->filterBy('filename', 'thumbnail')->first();
    $preview = $project->videos()->filterBy('filename', 'preview')->first();
    $largeClass = $project->islarge()->isTrue() ? ' large' : '';
  ?>

    <a href="<?= $project->url() ?>"
       class="project-card<?= $largeClass ?>"
       data-category="<?= $project->category() ?>"
       <?php if($thumbnail): ?>
       style="background-image: url('<?= $thumbnail->url() ?>')"
       <?php endif ?>>

      <?php if($preview): ?>
      <video
        src="<?= $preview->url() ?>"
        loop
        muted
        playsinline
        preload="none">
      </video>
      <?php endif ?>

      <div class="project-info">
        <h3><?= $project->title() ?></h3>
        <?php if($project->subtitle()->isNotEmpty()): ?>
          <span class="subtitle"><?= $project->subtitle() ?></span>
        <?php endif ?>
      </div>
    </a>

  <?php endforeach ?>

  <!-- Photography card -->
  <a href="<?= page('photography')->url() ?>"
     class="project-card"
     data-category="photography"
     style="background-image: url('<?= page('photography')->images()->first()->url() ?>')">
    <div class="project-info">
      <h3>Photography</h3>
    </div>
  </a>
</div>

<?php snippet('footer') ?>
```

#### 4.4: Update JavaScript for Client-Side Filtering

Add to `assets/js/script.js`:

```javascript
// Category filtering (client-side, instant)
document.addEventListener('DOMContentLoaded', function() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      const filter = this.dataset.filter;

      // Update active state
      filterButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');

      // Update URL hash
      window.location.hash = filter === 'all' ? '' : filter;

      // Filter cards
      projectCards.forEach(card => {
        const category = card.dataset.category;

        if(filter === 'all' || category === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // Apply filter from URL hash on load
  const hash = window.location.hash.substring(1);
  if(hash) {
    const filterBtn = document.querySelector(`[data-filter="${hash}"]`);
    if(filterBtn) filterBtn.click();
  }
});
```

#### 4.5: .htaccess for Clean URLs

**File**: `.htaccess`

```apache
# Kirby .htaccess

# Rewrite rules
<IfModule mod_rewrite.c>

RewriteEngine on

# Make site links work without trailing slash
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php [L]

</IfModule>

# Pass the Authorization header to PHP
SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1

# Compress text files
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/plain
  AddOutputFilterByType DEFLATE text/html
  AddOutputFilterByType DEFLATE text/xml
  AddOutputFilterByType DEFLATE text/css
  AddOutputFilterByType DEFLATE text/javascript
  AddOutputFilterByType DEFLATE application/xml
  AddOutputFilterByType DEFLATE application/xhtml+xml
  AddOutputFilterByType DEFLATE application/rss+xml
  AddOutputFilterByType DEFLATE application/javascript
  AddOutputFilterByType DEFLATE application/x-javascript
  AddOutputFilterByType DEFLATE image/svg+xml
</IfModule>

# Cache static files
<IfModule mod_expires.c>
  ExpiresActive on
  ExpiresDefault "access plus 1 month"
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType video/mp4 "access plus 1 year"
</IfModule>
```

**Deliverables**:
- ✅ Configuration complete
- ✅ Routing implemented
- ✅ Filtering working (client + server-side)
- ✅ Clean URLs enabled

---

### Phase 5: Testing & Optimization (3-4 hours)

**Objective**: Test all functionality and optimize performance

#### 5.1: Functional Testing Checklist

- [ ] **Homepage**
  - [ ] All projects display correctly
  - [ ] Thumbnails load
  - [ ] Preview videos play on hover
  - [ ] Large cards display as 2x2
  - [ ] Photography card appears
  - [ ] Grid is responsive (test mobile/tablet)

- [ ] **Filtering**
  - [ ] "All" shows all projects
  - [ ] "Film" shows only film projects
  - [ ] "Commercial" shows only commercial projects
  - [ ] "Automotive" shows only automotive projects
  - [ ] "Photography" shows only photography card
  - [ ] Filter persists in URL hash
  - [ ] Filter state restores on page load

- [ ] **Project Pages**
  - [ ] Vimeo player embeds correctly
  - [ ] All metadata displays (title, subtitle, category, year)
  - [ ] Description renders
  - [ ] Credits list displays
  - [ ] Prev/Next navigation works
  - [ ] Navigation loops at ends
  - [ ] Back to grid link works

- [ ] **Photography Page**
  - [ ] All 20 images display
  - [ ] 3-column grid layout
  - [ ] Images are lazy-loaded
  - [ ] Responsive layout (2-col tablet, 1-col mobile)
  - [ ] Back link works

- [ ] **Info Overlay**
  - [ ] Opens when clicking "i" button
  - [ ] Closes with X button
  - [ ] Closes when clicking outside
  - [ ] All contact info displays
  - [ ] All representation info displays
  - [ ] Links work (email, Instagram)

- [ ] **Panel Interface**
  - [ ] Login works at /panel
  - [ ] Can edit projects
  - [ ] Can upload new thumbnails
  - [ ] Can upload new preview videos
  - [ ] Changes save correctly
  - [ ] Changes appear on frontend

#### 5.2: Browser Testing

Test in:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

#### 5.3: Performance Optimization

**Install Caching Plugin**:

```bash
composer require getkirby/staticache
```

**Update config** (`site/config/config.php`):

```php
'cache' => [
    'pages' => [
        'active' => true,
        'type' => 'file',
        'ignore' => function ($page) {
            // Don't cache Panel pages
            return $page->kirby()->user() !== null;
        }
    ]
],

'staticache' => [
    'active' => true,
    'ignore' => [
        'panel/**',
        'sitemap.xml',
        '**.json',
        '**.xml'
    ]
]
```

**Test performance**:
```bash
# Without cache
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:8000/

# With cache (second request)
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:8000/
```

Create `curl-format.txt`:
```
    time_namelookup:  %{time_namelookup}\n
       time_connect:  %{time_connect}\n
    time_starttransfer:  %{time_starttransfer}\n
                      ----------\n
        time_total:  %{time_total}\n
```

#### 5.4: Image Optimization

Kirby's built-in thumb() method handles this, but verify settings:

```php
// In templates, use optimized images
<?= $image->thumb(['width' => 640, 'quality' => 85])->url() ?>
```

#### 5.5: SEO Optimization

Add meta tags to header snippet:

```php
<!-- site/snippets/header.php -->
<meta name="description" content="<?= $page->metaDescription()->or($site->description()) ?>">
<meta property="og:title" content="<?= $page->title() ?>">
<meta property="og:description" content="<?= $page->metaDescription()->or($site->description()) ?>">
<meta property="og:type" content="website">
<meta property="og:url" content="<?= $page->url() ?>">
<?php if($page->template() == 'project' && $thumb = $page->images()->first()): ?>
  <meta property="og:image" content="<?= $thumb->url() ?>">
<?php endif ?>
```

#### 5.6: Security Checklist

- [ ] Disable debug mode in production (`'debug' => false`)
- [ ] Use strong Panel password
- [ ] Set proper file permissions (755 dirs, 644 files)
- [ ] Keep Kirby updated
- [ ] Use HTTPS in production
- [ ] Set appropriate CSP headers

**Deliverables**:
- ✅ All features tested and working
- ✅ Performance optimized
- ✅ SEO configured
- ✅ Security hardened

---

### Phase 6: Deployment (2-3 hours)

**Objective**: Deploy to production hosting

#### 6.1: Choose Hosting

**Requirements**:
- PHP 8.0+
- Apache or Nginx
- SSL certificate
- ~50MB storage minimum

**Recommended hosts**:
- **Uberspace** - €5-10/month, excellent for Kirby
- **Digital Ocean** - $6/month droplet
- **Linode** - $5/month
- **Cloudways** - Managed hosting
- **Traditional shared hosting** with PHP 8+

#### 6.2: Pre-Deployment Checklist

- [ ] Update config for production
  ```php
  // site/config/config.php
  return [
      'debug' => false,
      'cache' => [
          'pages' => [
              'active' => true
          ]
      ]
  ];
  ```

- [ ] Set Panel email
  ```php
  'panel' => [
      'install' => false, // Disable installer after first use
      'slug' => 'panel'
  ]
  ```

- [ ] Create `.gitignore`
  ```
  .DS_Store
  /media
  /site/cache
  /site/sessions
  /site/config/config.localhost.php
  /site/accounts/*
  !/site/accounts/index.html
  ```

#### 6.3: Deployment Methods

**Option A: FTP/SFTP**

1. Export site from local
2. Upload entire directory via FTP
3. Set file permissions
4. Test in browser

**Option B: Git Deployment**

1. Push to GitHub/GitLab
   ```bash
   git init
   git add .
   git commit -m "Initial Kirby site"
   git remote add origin [repo-url]
   git push -u origin main
   ```

2. On server, clone repository
   ```bash
   cd /var/www/html
   git clone [repo-url] website
   ```

3. Set permissions
   ```bash
   chmod -R 755 content media site/cache site/sessions
   ```

**Option C: Automated Deployment (Deployer)**

Use Deployer for zero-downtime deployments:

```php
// deploy.php
<?php
namespace Deployer;

require 'recipe/kirby.php';

host('production')
    ->hostname('your-server.com')
    ->user('deploy')
    ->set('deploy_path', '/var/www/html');

set('repository', 'git@github.com:username/website-kirby.git');
```

#### 6.4: Post-Deployment

1. **Test site**
   - Visit homepage
   - Test all projects
   - Test filtering
   - Test Panel login

2. **Configure SSL**
   ```bash
   # With Let's Encrypt
   sudo certbot --apache -d yourdomain.com -d www.yourdomain.com
   ```

3. **Configure Domain**
   - Point A record to server IP
   - Set up www redirect if desired

4. **Monitor Performance**
   - Check page load times
   - Verify caching works
   - Test mobile performance

5. **Backup Strategy**
   - Backup content folder regularly
   - Backup site/accounts folder
   - Database not needed (flat-file)

#### 6.5: Maintenance

**Regular tasks**:
- Update Kirby core when new versions release
- Backup content folder monthly
- Monitor disk space
- Check SSL certificate expiry

**Update Kirby**:
```bash
composer update getkirby/cms
```

Or manually download and replace /kirby folder.

**Deliverables**:
- ✅ Site deployed to production
- ✅ Domain configured
- ✅ SSL enabled
- ✅ Backups configured

---

## Configuration Files

### Complete config.php

**File**: `site/config/config.php`

```php
<?php

return [
    // Debug mode (disable in production)
    'debug' => false,

    // Homepage
    'home' => 'home',

    // Panel settings
    'panel' => [
        'install' => false,
        'slug' => 'panel',
        'css' => 'assets/css/panel.css' // Optional custom panel CSS
    ],

    // Cache settings
    'cache' => [
        'pages' => [
            'active' => true,
            'type' => 'file',
            'ignore' => function ($page) {
                return $page->kirby()->user() !== null;
            }
        ]
    ],

    // Thumbs settings
    'thumbs' => [
        'quality' => 85,
        'srcsets' => [
            'default' => [
                '400w' => ['width' => 400, 'quality' => 80],
                '800w' => ['width' => 800, 'quality' => 85],
                '1200w' => ['width' => 1200, 'quality' => 85],
                '1600w' => ['width' => 1600, 'quality' => 80]
            ]
        ],
        'presets' => [
            'thumbnail' => ['width' => 640, 'height' => 360, 'crop' => true],
            'photography' => ['width' => 1200, 'quality' => 90]
        ]
    ],

    // Routes
    'routes' => [
        [
            'pattern' => '/',
            'action' => function() {
                return page('home');
            }
        ],
        [
            'pattern' => 'filter/(:any)',
            'action' => function($category) {
                return page('home')->render([
                    'filter' => $category
                ]);
            }
        ]
    ],

    // Smartypants for better typography
    'smartypants' => true,

    // Languages (if needed in future)
    'languages' => false,

    // API settings (disable if not needed)
    'api' => [
        'basicAuth' => true,
        'allowInsecure' => false
    ]
];
```

### Environment-Specific Config

**Local development**: `site/config/config.localhost.php`

```php
<?php

return [
    'debug' => true,

    'panel' => [
        'install' => true
    ],

    'cache' => [
        'pages' => [
            'active' => false // Disable for easier dev
        ]
    ]
];
```

This file is automatically loaded when hostname is "localhost".

---

## Media Migration Strategy

### File Organization

**Current structure**:
```
media/
├── previews/          # 16 MP4 files (41KB-425KB each)
├── thumbnails/        # 16 JPG files (~200KB each)
└── photography/       # 20 JPG files
```

**Target Kirby structure**:
```
content/
├── projects/
│   ├── kia/
│   │   ├── project.txt
│   │   ├── thumbnail.jpg      ← from media/thumbnails/kia.jpg
│   │   └── preview.mp4        ← from media/previews/kia.mp4
│   └── [15 more project folders...]
└── photography/
    ├── photography.txt
    ├── 001.jpg                ← from media/photography/001.jpg
    └── [19 more photos...]
```

### File Naming Conventions

**Option 1: Descriptive names**
```
kia-thumbnail.jpg
kia-preview.mp4
```

**Option 2: Generic names** (recommended)
```
thumbnail.jpg
preview.mp4
```

Generic names are simpler and work well with Kirby's file templates.

### Migration Script

See Phase 2.5 for complete bash script to copy files.

### File Templates (Blueprints)

Using file templates allows metadata per file:

```yaml
# site/blueprints/files/thumbnail.yml
title: Thumbnail
accept:
  - image/jpeg
  - image/png

fields:
  alt:
    type: text
    label: Alt Text
```

Then reference in Panel:
```php
$project->images()->template('thumbnail')->first()
```

---

## Testing Checklist

### Pre-Launch Testing

**Functionality**:
- [ ] All 16 projects display on homepage
- [ ] Hover previews play smoothly
- [ ] Category filtering works (all categories)
- [ ] Photography card links correctly
- [ ] All project pages render
- [ ] Vimeo embeds play
- [ ] Prev/Next navigation cycles correctly
- [ ] Photography gallery displays all 20 images
- [ ] Info overlay opens/closes
- [ ] All links work (email, Instagram, etc.)

**Content Accuracy**:
- [ ] All project titles correct
- [ ] All Vimeo IDs correct (videos play)
- [ ] All categories assigned correctly
- [ ] All credits display
- [ ] No missing thumbnails
- [ ] No missing previews (except Gatorade if applicable)

**Responsive Design**:
- [ ] Desktop (1920px+): Full grid
- [ ] Laptop (1280px): Adjusted grid
- [ ] Tablet (768px): 2-column grid
- [ ] Mobile (375px): 1-column grid
- [ ] Touch interactions work (hover → tap)

**Performance**:
- [ ] Page load < 2 seconds
- [ ] Preview videos load quickly
- [ ] No layout shifts (CLS)
- [ ] Images lazy-load
- [ ] No console errors

**SEO**:
- [ ] Meta titles present
- [ ] Meta descriptions present
- [ ] OG tags for social sharing
- [ ] Sitemap generated (if plugin installed)
- [ ] Robots.txt configured

**Accessibility**:
- [ ] All images have alt text
- [ ] Keyboard navigation works
- [ ] Focus states visible
- [ ] ARIA labels on buttons
- [ ] Color contrast sufficient

**Cross-Browser**:
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge
- [ ] Mobile Safari
- [ ] Chrome Mobile

**Panel**:
- [ ] Login works
- [ ] Can edit projects
- [ ] Can upload files
- [ ] Changes save
- [ ] Changes appear on frontend
- [ ] File size limits appropriate

### Post-Launch Monitoring

**Week 1**:
- Check analytics for errors
- Monitor server logs
- Test from different locations
- Verify email links work
- Check SSL certificate

**Monthly**:
- Backup content folder
- Check for Kirby updates
- Review performance metrics
- Test all forms/links

---

## Deployment Guide

### Hosting Setup

#### Requirements

- **PHP**: 8.0 or higher
- **Web Server**: Apache or Nginx
- **SSL Certificate**: Let's Encrypt (free)
- **Disk Space**: ~50MB minimum (more if adding many projects)
- **Memory**: 128MB minimum (256MB recommended)

#### Recommended Hosts

1. **Uberspace** (€5-10/month)
   - Excellent for Kirby
   - German hosting
   - SSH access
   - Free SSL

2. **Digital Ocean** ($6/month)
   - Full control
   - Requires server management
   - Scalable

3. **Cloudways** ($10+/month)
   - Managed hosting
   - Easy deployment
   - Good performance

### Deployment Steps

#### Step 1: Prepare for Production

```bash
# Set production mode
# Edit site/config/config.php
'debug' => false,
'cache' => ['pages' => ['active' => true]]
```

#### Step 2: Transfer Files

**Via Git**:
```bash
# On server
cd /var/www/html
git clone [your-repo] website-kirby
cd website-kirby
composer install --no-dev
```

**Via SFTP**:
- Upload entire directory
- Use FileZilla or Cyberduck

#### Step 3: Set Permissions

```bash
# Make writable directories
chmod -R 755 content
chmod -R 755 media
chmod -R 755 site/cache
chmod -R 755 site/sessions
chmod -R 755 site/accounts

# Secure config
chmod 644 site/config/config.php
```

#### Step 4: Configure Web Server

**Apache** (`.htaccess` already included):
```apache
<VirtualHost *:80>
    ServerName justinhenning.com
    DocumentRoot /var/www/html/website-kirby

    <Directory /var/www/html/website-kirby>
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

**Nginx**:
```nginx
server {
    listen 80;
    server_name justinhenning.com;
    root /var/www/html/website-kirby;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.0-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```

#### Step 5: SSL Certificate

```bash
# Install Certbot
sudo apt install certbot python3-certbot-apache

# Get certificate
sudo certbot --apache -d justinhenning.com -d www.justinhenning.com

# Auto-renewal (runs automatically)
sudo certbot renew --dry-run
```

#### Step 6: Final Checks

1. Visit site: `https://justinhenning.com`
2. Test all pages
3. Login to Panel: `https://justinhenning.com/panel`
4. Verify SSL (green padlock)

### Deployment Automation

**Using Deployer**:

```bash
composer require deployer/deployer --dev
```

Create `deploy.php`:
```php
<?php
namespace Deployer;

require 'recipe/common.php';

set('application', 'Justin Henning Portfolio');
set('repository', 'git@github.com:username/website-kirby.git');
set('keep_releases', 3);

host('production')
    ->hostname('justinhenning.com')
    ->user('deploy')
    ->set('deploy_path', '/var/www/html');

// Tasks
task('deploy', [
    'deploy:prepare',
    'deploy:vendors',
    'deploy:publish'
]);
```

Deploy with:
```bash
dep deploy production
```

---

## Rollback Plan

### If Migration Has Issues

#### Option 1: Quick Rollback

Keep current static site running until Kirby is fully tested:

1. Deploy Kirby to subdomain: `new.justinhenning.com`
2. Test thoroughly
3. When ready, swap DNS

#### Option 2: Dual Hosting

Run both sites in parallel:
- **Static**: `justinhenning.com`
- **Kirby**: `kirby.justinhenning.com`

Gradually migrate traffic.

#### Option 3: Full Revert

If needed to completely revert:

1. **Restore static site**
   ```bash
   cd /var/www/html
   rm -rf website-kirby
   git clone [static-site-repo] website
   ```

2. **Update DNS** if changed

3. **Keep Kirby backup** for future attempt
   ```bash
   mv website-kirby website-kirby-backup
   ```

### Data Preservation

Even if reverting, you keep:
- All Kirby content files (easy to migrate again)
- Media files (organized per project)
- Panel configuration

**No data loss** - Kirby is flat-file, everything is in text files.

---

## Resources

### Official Documentation

- **Kirby Docs**: https://getkirby.com/docs
- **Getting Started**: https://getkirby.com/docs/guide
- **Cookbook**: https://getkirby.com/docs/cookbook
- **Reference**: https://getkirby.com/docs/reference

### Key Pages for Migration

- **Installation**: https://getkirby.com/docs/guide/quickstart
- **Content Structure**: https://getkirby.com/docs/guide/content/introduction
- **Blueprints**: https://getkirby.com/docs/guide/blueprints/introduction
- **Templates**: https://getkirby.com/docs/guide/templates/basics
- **Routing**: https://getkirby.com/docs/guide/routing

### Community

- **Forum**: https://forum.getkirby.com
- **Discord**: https://chat.getkirby.com
- **GitHub**: https://github.com/getkirby

### Plugins

- **Staticache** (performance): https://github.com/getkirby/staticache
- **SEO** (meta tags): https://github.com/tobimori/kirby-seo
- **Embed** (Vimeo): https://github.com/distantnative/kirby-embed

### Tools

- **Kirby CLI**: https://github.com/getkirby/cli
- **Panel**: Built-in at `/panel`
- **Deployer**: https://deployer.org

### Example Sites

- **Starterkit**: https://github.com/getkirby/starterkit
- **Portfolio Examples**: https://getkirby.com/love

---

## Next Steps

### Immediate Actions

1. **Review this document** completely
2. **Decide**: Proceed with migration or stay with static?
3. **Budget time**: Block out 1-2 weeks for implementation
4. **Purchase license**: €99 at getkirby.com (when ready)

### Phase-by-Phase Approach

**Week 1**:
- Phase 0: Setup (1-2 hours)
- Phase 1: Blueprints (4-6 hours)
- Phase 2: Content migration (3-4 hours)

**Week 2**:
- Phase 3: Templates (6-8 hours)
- Phase 4: Configuration (2-3 hours)
- Phase 5: Testing (3-4 hours)
- Phase 6: Deployment (2-3 hours)

### Questions to Consider

Before starting:

1. **Frequency**: How often do you add new projects?
   - Monthly+ → Kirby makes sense
   - Annually → Static might suffice

2. **Team size**: Will others edit content?
   - Yes → Kirby Panel is valuable
   - Just you → Static is fine

3. **Future plans**: Will the site grow significantly?
   - Yes → Kirby scales better
   - No → Current structure works

4. **Time investment**: Can you dedicate 1-2 weeks?
   - Yes → Proceed with migration
   - No → Stay with current site

### Support

For questions during implementation:
- Reference this document
- Check Kirby docs
- Ask on Kirby forum
- Contact via Discord

---

## Conclusion

This migration plan provides everything needed to move your static portfolio to Kirby CMS. The estimated 1-2 week timeline assumes working a few hours per day. With focused effort, it could be completed faster.

**Key Takeaway**: The migration is straightforward because your current structure already resembles how Kirby organizes content. You're essentially translating HTML pages into content files and templates.

**Biggest Benefit**: Future content updates become trivial - just use the Panel instead of editing HTML.

**Biggest Risk**: Time investment for potentially modest benefit given your current site's simplicity.

Make the decision based on your specific needs and future plans for the portfolio.

---

**Document Version**: 1.0
**Last Updated**: 2025-11-12
**Author**: Migration plan generated for Justin Henning portfolio
**Status**: Ready for implementation
