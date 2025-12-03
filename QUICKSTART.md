# Quick Start Guide

Your minimalistic cinematography portfolio is ready! Here's how to view it:

## View Your Website

### Option 1: Direct File (Easiest)
1. Open Finder
2. Navigate to `/Users/justinhenning/code/website/`
3. Double-click `index.html`
4. Your website will open in your default browser

### Option 2: Local Server (Recommended)
If videos don't work with Option 1, use a local server:

1. Open Terminal
2. Run these commands:
   ```bash
   cd /Users/justinhenning/code/website
   python3 -m http.server 8000
   ```
3. Open your browser and go to: `http://localhost:8000`
4. To stop the server, press `Ctrl+C` in Terminal

## What's Included

✅ **All 16 projects** from your current website with real thumbnails
✅ **All Vimeo videos** embedded and ready to play
✅ **Autoplay enabled** - videos play immediately when clicked
✅ **Easy navigation** - Previous/Next buttons and keyboard shortcuts
✅ **Category filtering** - Filter by Film, Automotive, Commercial, Photography
✅ **Contact information** - All your representation details
✅ **Mobile responsive** - Works perfectly on phones and tablets
✅ **Minimalistic dark design** - Inspired by ligthelm.work

## How to Use

- **Click any project thumbnail** → Video plays automatically in Vimeo player
- **Navigate videos**: Use Previous/Next buttons or arrow keys (← →)
- **Close video**: Click the X or press ESC
- **View contact info**: Click "INFORMATION" in the header
- **Filter projects**: Click the category buttons (ALL, FILM, AUTOMOTIVE, etc.)

## File Structure

```
website/
├── index.html              # Main website
├── style.css              # All styling
├── script.js              # Video player & interactions
├── media/
│   └── thumbnails/        # All 16 project thumbnails
├── README.md              # Detailed documentation
└── QUICKSTART.md          # This file
```

## Next Steps

### To Deploy Your Website:

1. **Netlify** (Easiest):
   - Go to https://www.netlify.com
   - Drag the entire `website` folder onto their site
   - Done! You'll get a URL like `yourname.netlify.app`

2. **Vercel**:
   - Go to https://vercel.com
   - Upload the folder
   - Deploy in one click

3. **Your Domain** (justinhenning.com):
   - Upload all files via FTP to your web host
   - Or use your hosting provider's file manager

## Features Working

✅ Vimeo video autoplay
✅ Keyboard shortcuts (ESC, ← →)
✅ Responsive grid layout
✅ Smooth transitions
✅ Project filtering
✅ Information page toggle
✅ Mobile-friendly design

## Need Help?

Everything should work out of the box. Just open `index.html` and start exploring!

If you want to customize anything, check the full `README.md` for details.
