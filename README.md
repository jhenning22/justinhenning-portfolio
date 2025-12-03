# Justin Henning - Cinematography Portfolio

A minimalistic portfolio website inspired by ligthelm.work, designed to showcase cinematography work with an elegant dark theme and smooth interactions.

## Features

- **Minimalistic Dark Design**: Clean black background with white typography
- **Responsive Grid Layout**: 4-column grid on desktop, 2-column on mobile
- **Video Autoplay**: Videos automatically play when you click on project thumbnails
- **Easy Navigation**: Previous/Next buttons and keyboard shortcuts (arrow keys, ESC)
- **Category Filtering**: Filter projects by Film, Automotive, Commercial, Photography
- **Mobile Friendly**: Fully responsive design optimized for all devices
- **Information Page**: Contact details and representation information

## Getting Started

### Adding Your Videos and Images

1. **Create a media folder** in the website directory:
   ```bash
   mkdir media
   mkdir media/videos
   mkdir media/thumbnails
   ```

2. **Add your video files** to the `media/videos` folder

3. **Add thumbnail images** for each project to the `media/thumbnails` folder

4. **Update the `script.js` file** with your actual video URLs and thumbnails:
   - Open `script.js`
   - Find the `projects` array at the top
   - Replace `"path/to/video.mp4"` with your actual video paths
   - Replace `"path/to/thumbnail.jpg"` with your actual thumbnail paths

   Example:
   ```javascript
   {
       title: "YOUR LUCKY DAY",
       category: "Film",
       videoUrl: "media/videos/your-lucky-day.mp4",
       thumbnail: "media/thumbnails/your-lucky-day.jpg"
   }
   ```

5. **Update thumbnail backgrounds in `index.html`**:
   - Find each `.project-card` element
   - Replace the placeholder background-image URLs with your thumbnail paths

   Example:
   ```html
   <div class="project-image" style="background-image: url('media/thumbnails/your-lucky-day.jpg')"></div>
   ```

### Running the Website Locally

Simply open `index.html` in your web browser, or use a local server:

```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js (if you have http-server installed)
npx http-server
```

Then visit `http://localhost:8000` in your browser.

## Keyboard Shortcuts

When viewing a video:
- **ESC**: Close video modal
- **← Left Arrow**: Previous project
- **→ Right Arrow**: Next project

## Customization

### Changing Colors
Edit `style.css` to customize colors:
- Background: `#000` (black)
- Text: `#fff` (white)
- Hover states: Adjust opacity values

### Adding More Projects
1. Add a new project card in `index.html` following the existing pattern
2. Add the project data to the `projects` array in `script.js`
3. Make sure the `data-project` attribute matches the array index

### Adjusting Grid Layout
In `style.css`, modify the `.project-grid` settings:
- Desktop: `grid-template-columns: repeat(4, 1fr);`
- Tablet: `grid-template-columns: repeat(3, 1fr);`
- Mobile: `grid-template-columns: repeat(2, 1fr);`

### Large Project Cards
To make a project card span 2x2 spaces, add the `large` class:
```html
<div class="project-card large" data-category="automotive" data-project="6">
```

## File Structure

```
website/
├── index.html          # Main HTML structure
├── style.css           # All styling and responsive design
├── script.js           # Video player and interactivity
├── README.md           # This file
└── media/             # Your videos and images (create this)
    ├── videos/
    └── thumbnails/
```

## Browser Support

Works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Deployment

To deploy to a hosting service:

1. **Netlify/Vercel**: Simply drag and drop the entire folder
2. **GitHub Pages**: Push to a GitHub repo and enable Pages in settings
3. **Traditional hosting**: Upload all files via FTP to your web host

## Video Format Recommendations

- **Format**: MP4 (H.264 codec)
- **Resolution**: 1920x1080 (Full HD) or higher
- **Compression**: Use a tool like HandBrake to optimize file sizes
- **Thumbnails**: JPG format, 800x600px minimum

## Need Help?

If you need to customize anything further or add additional features, just let me know!
