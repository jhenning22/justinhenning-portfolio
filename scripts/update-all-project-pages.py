#!/usr/bin/env python3
"""
Update all project pages to match the new design from your-lucky-day.html
"""

import os
import re
from pathlib import Path

# Read the template (your-lucky-day.html)
template_path = Path("v2/projects/your-lucky-day.html")
with open(template_path, 'r') as f:
    template = f.read()

# Extract the style section from template
style_match = re.search(r'<style>(.*?)</style>', template, re.DOTALL)
template_style = style_match.group(1) if style_match else ""

# Extract the body structure (everything after <body> and before the script that has project data)
body_match = re.search(r'<body>(.*?)<script>', template, re.DOTALL)
template_body_structure = body_match.group(1) if body_match else ""

# Project data mapping
projects_data = {
    "your-lucky-day": {
        "title": "YOUR LUCKY DAY",
        "subtitle": "Feature Film",
        "category": "Film",
        "vimeoId": "872749030",
        "index": 0,
        "details": {
            "left": [
                {"label": "Director", "value": "Daniel Brown"},
                {"label": "Synopsis", "value": "A dispute over a winning lottery ticket escalates into a deadly hostage situation. The witnesses must decide how far they'll go—and how much blood they're willing to spill—for a cut of the $156 million prize."},
                {"label": "Cast", "value": "Angus Cloud, Elliot Knight, Jessica Garza, Sterling Beaumon, Mousa Hussein Kraish, Jason Wiles, Sebastian Sozzi, Spencer Garrett, Jason O'Mara"}
            ],
            "right": [
                {"label": "Premiere", "value": "September 23, 2023 at Fantastic Fest"},
                {"label": "Platform", "value": "Netflix"}
            ]
        }
    },
    "woodford-reserve": {
        "title": "WOODFORD RESERVE",
        "subtitle": "The Derby",
        "category": "Commercial",
        "vimeoId": "898398761",
        "index": 1,
        "details": {
            "left": [
                {"label": "Director", "value": "David Holm"}
            ],
            "right": []
        }
    },
    "huawei": {
        "title": "HUAWEI",
        "subtitle": "Mate X6",
        "category": "Commercial",
        "vimeoId": "1046541141",
        "index": 2,
        "details": {
            "left": [
                {"label": "Director", "value": "Zou"}
            ],
            "right": []
        }
    },
    "kia": {
        "title": "KIA",
        "subtitle": "The Good Life",
        "category": "Automotive",
        "vimeoId": "913839989",
        "index": 3,
        "details": {
            "left": [
                {"label": "Director", "value": "Brent Foster"}
            ],
            "right": []
        }
    },
    "royal-bank-of-canada": {
        "title": "ROYAL BANK OF CANADA",
        "subtitle": "Windy",
        "category": "Commercial",
        "vimeoId": "891284220",
        "index": 4,
        "details": {
            "left": [
                {"label": "Director", "value": "David Holm"},
                {"label": "Cast", "value": "Sahith Theegala, Cameron Young, Sam Burns"}
            ],
            "right": []
        }
    },
    "k-n": {
        "title": "K&N",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "523316278",
        "index": 5,
        "details": {"left": [], "right": []}
    },
    "ram": {
        "title": "RAM",
        "subtitle": "Paramotor",
        "category": "Automotive",
        "vimeoId": "930752804",
        "index": 6,
        "details": {
            "left": [
                {"label": "Director", "value": "David Holm"}
            ],
            "right": []
        }
    },
    "audi": {
        "title": "AUDI",
        "subtitle": "Listen",
        "category": "Automotive",
        "vimeoId": "163036231",
        "index": 7,
        "details": {
            "left": [
                {"label": "Director", "value": "David Holm"}
            ],
            "right": []
        }
    },
    "jeep": {
        "title": "JEEP",
        "subtitle": "Hero's Journey",
        "category": "Automotive",
        "vimeoId": "898405588",
        "index": 8,
        "details": {
            "left": [
                {"label": "Director", "value": "David Holm"}
            ],
            "right": []
        }
    },
    "ford": {
        "title": "FORD",
        "subtitle": "Expedition",
        "category": "Automotive",
        "vimeoId": "745033991",
        "index": 9,
        "details": {
            "left": [
                {"label": "Director", "value": "Scott Weintrob"}
            ],
            "right": []
        }
    },
    "american-outlaws": {
        "title": "AMERICAN OUTLAWS",
        "subtitle": "Feature Film",
        "category": "Film",
        "vimeoId": "797538936",
        "index": 10,
        "details": {
            "left": [
                {"label": "Director", "value": "Sean McEwen"},
                {"label": "Synopsis", "value": "Three siblings embark on a cross-country crime spree while facing potential imprisonment and seeking an idealized freedom. Based on true events from Kathy Dobie's GQ article 'The Whole True Story of the Dougherty Gang.'"},
                {"label": "Cast", "value": "Emory Cohen, India Eisley, Sam Strike, Treat Williams, Tess Harper"}
            ],
            "right": [
                {"label": "Premiere", "value": "2023 Santa Barbara International Film Festival"}
            ]
        }
    },
    "pei": {
        "title": "PEI",
        "subtitle": "Tourism",
        "category": "Commercial",
        "vimeoId": "374024991",
        "index": 13,
        "details": {"left": [], "right": []}
    },
    "lamborghini": {
        "title": "LAMBORGHINI",
        "subtitle": "Wind",
        "category": "Automotive",
        "vimeoId": "242791079",
        "index": 14,
        "details": {
            "left": [
                {"label": "Director", "value": "David Holm"}
            ],
            "right": []
        }
    },
    "ralph-lauren": {
        "title": "RALPH LAUREN",
        "subtitle": "Blue",
        "category": "Commercial",
        "vimeoId": "261889797",
        "index": 15,
        "details": {"left": [], "right": []}
    },
    "gatorade": {
        "title": "GATORADE",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "1046557409",
        "index": 16,
        "details": {"left": [], "right": []}
    },
    "nikon-clark-little": {
        "title": "NIKON: CLARK LITTLE",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "242791079",
        "index": 18,
        "details": {
            "left": [
                {"label": "Director", "value": "David Holm"}
            ],
            "right": []
        }
    }
}

# Get all project HTML files
projects_dir = Path("v2/projects")
project_files = list(projects_dir.glob("*.html"))

print(f"Found {len(project_files)} project files")
print(f"Have detailed data for {len(projects_data)} projects")

# For projects without detailed data, use minimal info
for project_file in project_files:
    slug = project_file.stem

    if slug not in projects_data:
        print(f"⚠️  Skipping {slug} - no project data defined")
        continue

    project = projects_data[slug]

    # Read existing file to preserve Vimeo ID if not in our data
    with open(project_file, 'r') as f:
        existing_content = f.read()

    # Build the project details HTML
    details_left_html = ""
    for detail in project["details"]["left"]:
        details_left_html += f'                <p><strong>{detail["label"]}:</strong> {detail["value"]}</p>\n\n'

    details_right_html = ""
    for detail in project["details"]["right"]:
        details_right_html += f'                <p><strong>{detail["label"]}:</strong> {detail["value"]}</p>\n\n'

    subtitle_text = project["subtitle"] if project["subtitle"] else ""

    # Generate the new HTML
    new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project["title"]} - Justin Henning</title>
    <link rel="stylesheet" href="../style.css?v=4">
    <style>
        {template_style}
    </style>
</head>
<body>
    <!-- Vertical Side Navigation -->
    <nav class="side-nav main-side-nav">
        <a href="../index.html#all" class="side-nav-btn">ALL</a>
        <a href="../index.html#film" class="side-nav-btn">FILM</a>
        <a href="../index.html#commercial" class="side-nav-btn">COMMERCIAL</a>
        <a href="../index.html#automotive" class="side-nav-btn">AUTOMOTIVE</a>
    </nav>

    <!-- Right Side Navigation for Photography -->
    <nav class="side-nav-right">
        <a href="../photography.html" class="side-nav-btn">PHOTOGRAPHY</a>
    </nav>

    <!-- Header with back link -->
    <header class="project-page-header">
        <div class="header-left">
            <a href="../index.html" class="back-link" id="backLink">WORK</a>
        </div>
        <div class="header-center">
            <a href="../index.html" class="header-title-link">
                <h1>JUSTIN HENNING CINEMATOGRAPHER</h1>
            </a>
        </div>
        <div class="header-right">
            <a href="../index.html#info" class="back-link">INFORMATION</a>
        </div>
    </header>

    <!-- Project Content -->
    <div class="project-container">
        <!-- Title and Category Above Video -->
        <div class="project-header">
            <h1 class="project-title">{project["title"]}</h1>
            <p class="project-subtitle">{subtitle_text}</p>
        </div>

        <!-- Video Player -->
        <div class="video-wrapper">
            <iframe
                src="https://player.vimeo.com/video/{project["vimeoId"]}?autoplay=1&title=0&byline=0&portrait=0"
                frameborder="0"
                allow="autoplay; fullscreen; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>

        <!-- Project Details Below Video -->
        <div class="project-details">
            <div class="project-details-left">
{details_left_html.rstrip()}
            </div>

            <div class="project-details-right">
{details_right_html.rstrip()}
            </div>
        </div>
    </div>

    <!-- Navigation -->
    <div class="project-navigation-wrapper">
        <div class="project-navigation-divider"></div>
        <div class="more-projects-label">More Projects</div>
        <nav class="project-navigation">
            <a href="#" class="nav-card" id="prevButton">
                <div class="nav-caption">
                    <span class="nav-title" id="prevTitle"></span>
                    <span class="nav-subtitle" id="prevSubtitle"></span>
                </div>
                <div class="nav-thumbnail">
                    <div class="nav-thumbnail-image" id="prevThumbnail"></div>
                </div>
            </a>
            <a href="#" class="nav-card" id="nextButton">
                <div class="nav-caption">
                    <span class="nav-title" id="nextTitle"></span>
                    <span class="nav-subtitle" id="nextSubtitle"></span>
                </div>
                <div class="nav-thumbnail">
                    <div class="nav-thumbnail-image" id="nextThumbnail"></div>
                </div>
            </a>
        </nav>
    </div>

    <script>
        // Filter-aware navigation
        const urlParams = new URLSearchParams(window.location.search);
        const activeFilter = urlParams.get('filter') || 'all';

        // Update back link to preserve filter
        const backLink = document.getElementById('backLink');
        if (activeFilter && activeFilter !== 'all') {{
            backLink.href = `../index.html#${{activeFilter}}`;
        }}

        // Current project info
        const currentProject = {{
            index: {project["index"]},
            title: "{project["title"]}",
            category: "{project["category"]}",
            slug: "{slug}"
        }};

        // All projects array with thumbnail paths
        const projects = [
            {{ title: "YOUR LUCKY DAY", category: "Film", slug: "your-lucky-day", thumbnail: "../media/thumbnails-webp/your-lucky-day.jpg.webp" }},
            {{ title: "WOODFORD RESERVE", category: "Commercial", slug: "woodford-reserve", thumbnail: "../media/thumbnails-webp/woodford-reserve.jpg.webp" }},
            {{ title: "HUAWEI", category: "Commercial", slug: "huawei", thumbnail: "../media/thumbnails-webp/huawei.jpg.webp" }},
            {{ title: "KIA", category: "Automotive", slug: "kia", thumbnail: "../media/thumbnails-webp/kia.jpg.webp" }},
            {{ title: "ROYAL BANK OF CANADA", category: "Commercial", slug: "royal-bank-of-canada", thumbnail: "../media/thumbnails-webp/rbc.jpg.webp" }},
            {{ title: "K&N", category: "Automotive", slug: "k-n", thumbnail: "../media/thumbnails-webp/kn.jpg.webp" }},
            {{ title: "RAM", category: "Automotive", slug: "ram", thumbnail: "../media/thumbnails-webp/ram.jpg.webp" }},
            {{ title: "AUDI", category: "Automotive", slug: "audi", thumbnail: "../media/thumbnails-webp/audi.jpg.webp" }},
            {{ title: "JEEP", category: "Automotive", slug: "jeep", thumbnail: "../media/thumbnails-webp/jeep.jpg.webp" }},
            {{ title: "FORD", category: "Automotive", slug: "ford", thumbnail: "../media/thumbnails-webp/ford.jpg.webp" }},
            {{ title: "AMERICAN OUTLAWS", category: "Film", slug: "american-outlaws", thumbnail: "../media/thumbnails-webp/american-outlaws.jpg.webp" }},
            {{ title: "ANA PAULA", category: "Film", slug: "ana-paula", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "LA LUCHA", category: "Film", slug: "la-lucha", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "PEI", category: "Commercial", slug: "pei", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "LAMBORGHINI", category: "Automotive", slug: "lamborghini", thumbnail: "../media/thumbnails-webp/lamborghini.jpg.webp" }},
            {{ title: "RALPH LAUREN", category: "Commercial", slug: "ralph-lauren", thumbnail: "../media/thumbnails-webp/polo.jpg.webp" }},
            {{ title: "GATORADE", category: "Commercial", slug: "gatorade", thumbnail: "../media/thumbnails-webp/gatorade.jpg.webp" }},
            {{ title: "MARRIOTT", category: "Commercial", slug: "marriott", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "NIKON: CLARK LITTLE", category: "Commercial", slug: "nikon-clark-little", thumbnail: "../media/thumbnails-webp/nikon-clark-little.jpg.webp" }},
            {{ title: "NIKON: IVAR", category: "Commercial", slug: "nikon-ivar", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "CHEVROLET", category: "Commercial", slug: "chevrolet", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "ICHNUSA", category: "Commercial", slug: "ichnusa", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "MILLER GENUINE DRAFT", category: "Commercial", slug: "miller-genuine-draft", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "ADIDAS", category: "Commercial", slug: "adidas", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "USPS", category: "Commercial", slug: "usps", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "RAM: BONEYARD", category: "Automotive", slug: "ram-boneyard", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "BENTLEY", category: "Automotive", slug: "bentley", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "ALFA ROMEO", category: "Automotive", slug: "alfa-romeo", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "INFINITI", category: "Automotive", slug: "infiniti", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "TOYOTA", category: "Automotive", slug: "toyota", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }},
            {{ title: "TESLA", category: "Automotive", slug: "tesla", thumbnail: "../media/thumbnails-webp/pei.jpg.webp" }}
        ];

        // Filter projects based on active filter
        function getFilteredProjects() {{
            if (activeFilter === 'all') {{
                return projects;
            }}
            return projects.filter(p => p.category.toLowerCase() === activeFilter.toLowerCase());
        }}

        // Get prev/next project slugs
        function updateNavigation() {{
            const filteredProjects = getFilteredProjects();
            const currentIndex = filteredProjects.findIndex(p => p.slug === currentProject.slug);

            const prevButton = document.getElementById('prevButton');
            const nextButton = document.getElementById('nextButton');
            const prevThumbnail = document.getElementById('prevThumbnail');
            const nextThumbnail = document.getElementById('nextThumbnail');
            const prevTitle = document.getElementById('prevTitle');
            const nextTitle = document.getElementById('nextTitle');
            const prevSubtitle = document.getElementById('prevSubtitle');
            const nextSubtitle = document.getElementById('nextSubtitle');

            let prevProject, nextProject;

            if (currentIndex > 0) {{
                prevProject = filteredProjects[currentIndex - 1];
                prevButton.href = `${{prevProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
            }} else {{
                // Wrap to last
                prevProject = filteredProjects[filteredProjects.length - 1];
                prevButton.href = `${{prevProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
            }}

            if (currentIndex < filteredProjects.length - 1) {{
                nextProject = filteredProjects[currentIndex + 1];
                nextButton.href = `${{nextProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
            }} else {{
                // Wrap to first
                nextProject = filteredProjects[0];
                nextButton.href = `${{nextProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
            }}

            // Set thumbnail backgrounds and titles
            if (prevProject) {{
                if (prevProject.thumbnail) {{
                    prevThumbnail.style.backgroundImage = `url('${{prevProject.thumbnail}}')`;
                }}
                prevTitle.textContent = prevProject.title;
                prevSubtitle.textContent = prevProject.category;
            }}
            if (nextProject) {{
                if (nextProject.thumbnail) {{
                    nextThumbnail.style.backgroundImage = `url('${{nextProject.thumbnail}}')`;
                }}
                nextTitle.textContent = nextProject.title;
                nextSubtitle.textContent = nextProject.category;
            }}
        }}

        // Initialize navigation
        updateNavigation();

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowLeft') {{
                document.getElementById('prevButton').click();
            }} else if (e.key === 'ArrowRight') {{
                document.getElementById('nextButton').click();
            }} else if (e.key === 'Escape') {{
                window.location.href = document.getElementById('backLink').href;
            }}
        }});
    </script>
</body>
</html>
'''

    # Write the new file
    with open(project_file, 'w') as f:
        f.write(new_html)

    print(f"✅ Updated {slug}")

print("\n✨ Done! Updated all project pages with new design.")
