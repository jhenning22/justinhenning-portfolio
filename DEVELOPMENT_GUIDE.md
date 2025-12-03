# Development Guide - 11ty Migration

## 🎉 Migration Complete!

Your website has been successfully migrated to use 11ty (Eleventy) static site generator. The new system eliminates template duplication and provides a single source of truth for all project data.

## Quick Start

### Development Server (with live reload)
```bash
npm start
```
This starts a local server at **http://localhost:8080/** with automatic rebuilds when you save files.

### Build for Production
```bash
npm run build
```
Generates static HTML files in the `_site/` directory.

### Clean Build Directory
```bash
npm run clean
```
Removes the `_site/` directory.

---

## What Changed?

### Before (Old System)
- 35+ HTML files with duplicated headers, footers, and info overlays
- Project data scattered across Python scripts and HTML files
- Manual copy-paste required for any header/footer updates
- Python scripts to generate project pages

### After (New System)
- **Single source of truth** for all data in `src/_data/projects.json`
- **Reusable components** in `src/_includes/components/`
- **Dynamic page generation** - edit one template, update all pages
- **Fast builds** - rebuilds in < 0.2 seconds
- **Live reload** during development

---

## Project Structure

```
website updated/
├── src/                          # Source files (edit these)
│   ├── _data/                    # Data files
│   │   ├── projects.json        # All 31 project definitions
│   │   └── site.json            # Global site configuration
│   ├── _includes/               # Templates & components
│   │   ├── layouts/
│   │   │   └── base.njk         # Base HTML wrapper
│   │   └── components/
│   │       ├── header.njk       # Shared header
│   │       └── info.njk         # Info overlay
│   ├── projects/                # Project HTML pages
│   ├── media/                   # Images, videos
│   ├── fonts/                   # Tonka font files
│   ├── style.css               # Main stylesheet
│   ├── script.js               # JavaScript
│   ├── index.njk               # Homepage template
│   └── work.njk                # Work grid template
├── _site/                       # Built files (generated, don't edit)
├── backup/                      # Original HTML files
├── .eleventy.js                # 11ty configuration
└── package.json                # Dependencies & scripts
```

---

## How to Make Changes

### Update the Header (Edit Once, Updates Everywhere!)
1. Edit `src/_includes/components/header.njk`
2. Save the file
3. 11ty automatically rebuilds all pages with the new header

**Before:** Had to update header in 35+ files
**After:** Edit one file!

### Update Info Overlay
1. Edit `src/_includes/components/info.njk`
2. Save - automatically updates on all pages

### Add a New Project
1. Add project data to `src/_data/projects.json`:
   ```json
   {
     "id": 32,
     "slug": "new-project",
     "title": "NEW PROJECT",
     "subtitle": "Description",
     "category": "film",
     "vimeoId": "123456789",
     "thumbnail": "/media/thumbnails/new-project.jpg",
     "preview": "/media/previews/new-project.mp4",
     "active": true,
     "large": false,
     "detailsLeft": [["Director", "Name"]],
     "detailsRight": []
   }
   ```
2. Add thumbnail: `src/media/thumbnails/new-project.jpg`
3. Add preview video: `src/media/previews/new-project.mp4`
4. Create project page: `src/projects/new-project.html`
5. Build - new project appears on the grid automatically!

### Modify Work Grid Page
1. Edit `src/work.njk`
2. The grid is generated from `projects.json` data automatically

### Change Global Site Settings
Edit `src/_data/site.json` for site name, description, social links, etc.

---

## Build Output

After running `npm run build`, the `_site/` directory contains:

```
_site/
├── index.html              # Homepage
├── work.html               # Main work grid
├── projects/               # Project pages
│   ├── your-lucky-day/
│   │   └── index.html
│   ├── kia/
│   │   └── index.html
│   └── ... (31 total)
├── media/                  # Images & videos
├── fonts/                  # Fonts
├── style.css              # Stylesheets
└── script.js              # JavaScript
```

**Deploy the `_site/` directory** to your hosting provider.

---

## Deployment

### Option 1: Netlify (Recommended)
1. Connect your Git repository to Netlify
2. Build command: `npm run build`
3. Publish directory: `_site`
4. Netlify will auto-build on every push!

### Option 2: Vercel
1. Import your Git repository
2. Framework preset: Other
3. Build command: `npm run build`
4. Output directory: `_site`

### Option 3: Manual Deploy
1. Run `npm run build` locally
2. Upload contents of `_site/` to your web host

---

## Testing the New Site

**The development server is currently running at http://localhost:8080/**

### Test Checklist
- ✅ Homepage redirects to work.html
- ✅ Work grid displays all active projects
- ✅ Video hover previews work
- ✅ Category filters (ALL, FILM, COMMERCIAL, AUTOMOTIVE) work
- ✅ Mobile menu works
- ✅ Info overlay opens and displays correctly
- ✅ Project page links work
- ✅ Vimeo embeds play
- ✅ Project navigation (prev/next) works
- ✅ Responsive design works on mobile

---

## Current Status

### ✅ Completed
- 11ty setup and configuration
- Base layout template with shared components
- Header component (unified across all pages)
- Info overlay component (no more duplication!)
- Projects data file (single source of truth)
- Work grid page (dynamically generated from data)
- Homepage (redirects to work)
- All 31 project pages (preserved from original)
- Build system working
- Development server with live reload

### 📝 Future Enhancements (Optional)
- Convert project pages to use templates (currently using original HTML)
- Add photography.html and archive.html templates
- Create proper project layout template with data-driven pages
- Add sitemap.xml generation
- Add RSS feed
- Optimize images with responsive sizes
- Add Open Graph meta tags for social sharing

---

## Key Benefits

1. **No More Duplication**: Edit header once, updates everywhere
2. **Data-Driven**: All project info in one JSON file
3. **Fast Builds**: 33 pages built in < 0.2 seconds
4. **Live Reload**: See changes instantly during development
5. **Easy Maintenance**: Clear separation of content and templates
6. **Version Control**: All changes tracked in Git
7. **Future-Proof**: Easy to add new features and pages

---

## Troubleshooting

### Build fails
```bash
npm install        # Reinstall dependencies
npm run clean      # Clear build cache
npm run build      # Try building again
```

### Dev server not updating
- Check terminal for errors
- Stop server (Ctrl+C) and restart: `npm start`
- Clear browser cache

### CSS/JS not loading
- Check file paths in templates
- Verify files exist in `src/` directory
- Rebuild: `npm run build`

---

## Need Help?

- **11ty Documentation**: https://www.11ty.dev/docs/
- **Nunjucks Syntax**: https://mozilla.github.io/nunjucks/templating.html
- **Project Files**: All original HTML backed up in `backup/` directory
- **Original Site**: Still running at `/Users/justinhenning/code/website/`

---

## What to Do Next

1. **Test the site** at http://localhost:8080/
2. **Compare with original** at `/Users/justinhenning/code/website/`
3. **Try editing** the header component and see it update everywhere!
4. **When satisfied**, you can:
   - Replace your original website directory with this new system
   - Or deploy `_site/` to your hosting provider
   - Keep both for now and switch when ready!

---

**Congratulations! Your site is now templated and maintainable.** 🎊
