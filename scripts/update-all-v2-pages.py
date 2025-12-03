#!/usr/bin/env python3
"""
Update all v2 project pages to match the Your Lucky Day design
"""

import os
from pathlib import Path

# Read the Your Lucky Day template to extract the style section
template_path = Path("v2/projects/your-lucky-day.html")
with open(template_path, 'r') as f:
    template_content = f.read()

# Extract style section from Your Lucky Day
style_start = template_content.find('<style>') + 7
style_end = template_content.find('</style>')
template_style = template_content[style_start:style_end].strip()

# All project data with complete information
projects_data = [
    {"slug": "your-lucky-day", "title": "YOUR LUCKY DAY", "subtitle": "Feature Film", "category": "Film", "vimeoId": "872749030", "index": 0,
     "details_left": [
         ("Director", "Daniel Brown"),
         ("Synopsis", "A dispute over a winning lottery ticket escalates into a deadly hostage situation. The witnesses must decide how far they'll go—and how much blood they're willing to spill—for a cut of the $156 million prize."),
         ("Cast", "Angus Cloud, Elliot Knight, Jessica Garza, Sterling Beaumon, Mousa Hussein Kraish, Jason Wiles, Sebastian Sozzi, Spencer Garrett, Jason O'Mara")
     ],
     "details_right": [
         ("Premiere", "September 23, 2023 at Fantastic Fest"),
         ("Platform", "Netflix")
     ]},

    {"slug": "woodford-reserve", "title": "WOODFORD RESERVE", "subtitle": "The Derby", "category": "Commercial", "vimeoId": "898398761", "index": 1,
     "details_left": [("Director", "David Holm")], "details_right": []},

    {"slug": "huawei", "title": "HUAWEI", "subtitle": "Mate X6", "category": "Commercial", "vimeoId": "1046541141", "index": 2,
     "details_left": [("Director", "Zou")], "details_right": []},

    {"slug": "kia", "title": "KIA", "subtitle": "The Good Life", "category": "Automotive", "vimeoId": "913839989", "index": 3,
     "details_left": [("Director", "Brent Foster")], "details_right": []},

    {"slug": "royal-bank-of-canada", "title": "ROYAL BANK OF CANADA", "subtitle": "Windy", "category": "Commercial", "vimeoId": "891284220", "index": 4,
     "details_left": [
         ("Director", "David Holm"),
         ("Cast", "Sahith Theegala, Cameron Young, Sam Burns")
     ], "details_right": []},

    {"slug": "k-n", "title": "K&N", "subtitle": "", "category": "Automotive", "vimeoId": "523316278", "index": 5,
     "details_left": [], "details_right": []},

    {"slug": "ram", "title": "RAM", "subtitle": "Paramotor", "category": "Automotive", "vimeoId": "930752804", "index": 6,
     "details_left": [("Director", "David Holm")], "details_right": []},

    {"slug": "audi", "title": "AUDI", "subtitle": "Listen", "category": "Automotive", "vimeoId": "163036231", "index": 7,
     "details_left": [("Director", "David Holm")], "details_right": []},

    {"slug": "jeep", "title": "JEEP", "subtitle": "Hero's Journey", "category": "Automotive", "vimeoId": "898405588", "index": 8,
     "details_left": [("Director", "David Holm")], "details_right": []},

    {"slug": "ford", "title": "FORD", "subtitle": "Expedition", "category": "Automotive", "vimeoId": "745033991", "index": 9,
     "details_left": [("Director", "Scott Weintrob")], "details_right": []},

    {"slug": "american-outlaws", "title": "AMERICAN OUTLAWS", "subtitle": "Feature Film", "category": "Film", "vimeoId": "797538936", "index": 10,
     "details_left": [
         ("Director", "Sean McEwen"),
         ("Synopsis", "Three siblings embark on a cross-country crime spree while facing potential imprisonment and seeking an idealized freedom. Based on true events from Kathy Dobie's GQ article 'The Whole True Story of the Dougherty Gang.'"),
         ("Cast", "Emory Cohen, India Eisley, Sam Strike, Treat Williams, Tess Harper")
     ],
     "details_right": [
         ("Premiere", "2023 Santa Barbara International Film Festival")
     ]},

    {"slug": "ana-paula", "title": "ANA PAULA", "subtitle": "Short Film", "category": "Film", "vimeoId": "840254843", "index": 11,
     "details_left": [
         ("Director", "Leigh Marling"),
         ("Synopsis", "Filmed on location in Durango, Mexico with a non-professional local cast, ANA PAULA is the heartbreaking story of a young woman determined to escape her dark past and adopt her niece from a government orphanage. To meet the strict criteria for adoption, Ana is working at a local hotel, attending interviews at the orphanage, and trying to save money for an apartment. When a judge explains her case cannot proceed for lack of a 'suitable home', Ana employs desperate measures to find the necessary cash. An admiring co-worker - Fernando - sees her desperation and offers to help, but after Ana agrees she finds herself drawn into a tragic romance. Soon, Ana's past comes back to haunt her. She is pulled back into a toxic life of vice that brings her into direct conflict with Fernando, her own inner demons, and the ruthless criminals who seek to destroy any chance of Ana becoming a mother."),
         ("Awards", "Winner of Best Foreign Short at the Burbank International Film Festival and Best Short Feature Film at the Arizona International Film Festival in 2024")
     ], "details_right": []},

    {"slug": "la-lucha", "title": "LA LUCHA", "subtitle": "Documentary Short", "category": "Film", "vimeoId": "180678668", "index": 12,
     "details_left": [
         ("Director", "Justin Henning"),
         ("Synopsis", "In 1962, Fidel Castro banned all professional (for profit) sports in Cuba. For Cuba's top athletes this means a tough choice. Stay in Cuba, their home, or defect and follow their dreams. This is the story of two-time Olympic gold medalist Mario Kindelán Mesa."),
         ("Awards", "Vimeo Staff Pick"),
         ("Credits", "Produced by SOCIETY (society.tv) in association with EL CENTRAL producciones. Executive Producers: Harry Calbom & David Holm. Producers: Carlos Gómez & Reymel Delgado Rodriguez. Movi Operator: Ryan Haug. Editor: Nick Pezzillo. Colorist: Eric Rosen.")
     ], "details_right": []},

    {"slug": "pei", "title": "PEI", "subtitle": "Prince Edward Island", "category": "Commercial", "vimeoId": "374024991", "index": 13,
     "details_left": [("Director", "Brent Foster")], "details_right": []},

    {"slug": "lamborghini", "title": "LAMBORGHINI", "subtitle": "The Wind", "category": "Automotive", "vimeoId": "242791079", "index": 14,
     "details_left": [("Director", "David Holm")], "details_right": []},

    {"slug": "ralph-lauren", "title": "RALPH LAUREN", "subtitle": "Polo Blue", "category": "Commercial", "vimeoId": "261889797", "index": 16,
     "details_left": [], "details_right": []},

    {"slug": "gatorade", "title": "GATORADE", "subtitle": "", "category": "Commercial", "vimeoId": "1046557409", "index": 17,
     "details_left": [], "details_right": []},

    {"slug": "marriott", "title": "MARRIOTT", "subtitle": "", "category": "Commercial", "vimeoId": "124659863", "index": 18,
     "details_left": [], "details_right": []},

    {"slug": "nikon-clark-little", "title": "NIKON: CLARK LITTLE", "subtitle": "", "category": "Commercial", "vimeoId": "165219350", "index": 19,
     "details_left": [("Director", "David Holm")], "details_right": []},

    {"slug": "nikon-ivar", "title": "NIKON: IVAR", "subtitle": "", "category": "Commercial", "vimeoId": "155239464", "index": 20,
     "details_left": [], "details_right": []},

    {"slug": "chevrolet", "title": "CHEVROLET", "subtitle": "", "category": "Commercial", "vimeoId": "436669633", "index": 21,
     "details_left": [], "details_right": []},

    {"slug": "ichnusa", "title": "ICHNUSA", "subtitle": "", "category": "Commercial", "vimeoId": "222332910", "index": 22,
     "details_left": [], "details_right": []},

    {"slug": "miller-genuine-draft", "title": "MILLER GENUINE DRAFT", "subtitle": "", "category": "Commercial", "vimeoId": "405148244", "index": 23,
     "details_left": [], "details_right": []},

    {"slug": "adidas", "title": "ADIDAS", "subtitle": "", "category": "Commercial", "vimeoId": "374027701", "index": 24,
     "details_left": [], "details_right": []},

    {"slug": "usps", "title": "USPS", "subtitle": "", "category": "Commercial", "vimeoId": "917245566", "index": 25,
     "details_left": [], "details_right": []},

    {"slug": "ram-boneyard", "title": "RAM: BONEYARD", "subtitle": "", "category": "Automotive", "vimeoId": "222244036", "index": 26,
     "details_left": [("Director", "David Holm")], "details_right": []},

    {"slug": "bentley", "title": "BENTLEY", "subtitle": "", "category": "Automotive", "vimeoId": "805761043", "index": 27,
     "details_left": [], "details_right": []},

    {"slug": "alfa-romeo", "title": "ALFA ROMEO", "subtitle": "", "category": "Automotive", "vimeoId": "248727672", "index": 28,
     "details_left": [], "details_right": []},

    {"slug": "infiniti", "title": "INFINITI", "subtitle": "", "category": "Automotive", "vimeoId": "245654221", "index": 29,
     "details_left": [], "details_right": []},

    {"slug": "toyota", "title": "TOYOTA", "subtitle": "", "category": "Automotive", "vimeoId": "394801461", "index": 30,
     "details_left": [], "details_right": []},

    {"slug": "tesla", "title": "TESLA", "subtitle": "", "category": "Automotive", "vimeoId": "148737078", "index": 31,
     "details_left": [], "details_right": []},
]

def generate_project_html(project):
    """Generate HTML for a project page"""

    # Build details HTML
    details_left_html = ""
    for label, value in project.get("details_left", []):
        details_left_html += f'                <p><strong>{label}:</strong> {value}</p>\n\n'

    details_right_html = ""
    for label, value in project.get("details_right", []):
        details_right_html += f'                <p><strong>{label}:</strong> {value}</p>\n\n'

    # Remove trailing whitespace
    details_left_html = details_left_html.rstrip()
    details_right_html = details_right_html.rstrip()

    subtitle = project["subtitle"] if project["subtitle"] else ""

    html = f'''<!DOCTYPE html>
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
            <p class="project-subtitle">{subtitle}</p>
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
{details_left_html}
            </div>

            <div class="project-details-right">
{details_right_html}
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
            slug: "{project["slug"]}"
        }};

        // All projects array with thumbnail paths
        const projects = [
            {{ title: "YOUR LUCKY DAY", category: "Film", slug: "your-lucky-day", thumbnail: "../../media/thumbnails/your-lucky-day.jpg" }},
            {{ title: "WOODFORD RESERVE", category: "Commercial", slug: "woodford-reserve", thumbnail: "../../media/thumbnails/woodford-reserve.jpg" }},
            {{ title: "HUAWEI", category: "Commercial", slug: "huawei", thumbnail: "../../media/thumbnails/huawei.jpg" }},
            {{ title: "KIA", category: "Automotive", slug: "kia", thumbnail: "../../media/thumbnails/kia.jpg" }},
            {{ title: "ROYAL BANK OF CANADA", category: "Commercial", slug: "royal-bank-of-canada", thumbnail: "../../media/thumbnails/rbc.jpg" }},
            {{ title: "K&N", category: "Automotive", slug: "k-n", thumbnail: "../../media/thumbnails/kn.jpg" }},
            {{ title: "RAM", category: "Automotive", slug: "ram", thumbnail: "../../media/thumbnails/ram.jpg" }},
            {{ title: "AUDI", category: "Automotive", slug: "audi", thumbnail: "../../media/thumbnails/audi.jpg" }},
            {{ title: "JEEP", category: "Automotive", slug: "jeep", thumbnail: "../../media/thumbnails/jeep.jpg" }},
            {{ title: "FORD", category: "Automotive", slug: "ford", thumbnail: "../../media/thumbnails/ford.jpg" }},
            {{ title: "AMERICAN OUTLAWS", category: "Film", slug: "american-outlaws", thumbnail: "../../media/thumbnails/american-outlaws.jpg" }},
            {{ title: "ANA PAULA", category: "Film", slug: "ana-paula", thumbnail: "../../media/thumbnails/ana-paula.jpg" }},
            {{ title: "LA LUCHA", category: "Film", slug: "la-lucha", thumbnail: "../../media/thumbnails/la-lucha.jpg" }},
            {{ title: "PEI", category: "Commercial", slug: "pei", thumbnail: "../../media/thumbnails/pei.jpg" }},
            {{ title: "LAMBORGHINI", category: "Automotive", slug: "lamborghini", thumbnail: "../../media/thumbnails/lamborghini.jpg" }},
            {{ title: "RALPH LAUREN", category: "Commercial", slug: "ralph-lauren", thumbnail: "../../media/thumbnails/ralph-lauren.jpg" }},
            {{ title: "GATORADE", category: "Commercial", slug: "gatorade", thumbnail: "../../media/thumbnails/gatorade.jpg" }},
            {{ title: "MARRIOTT", category: "Commercial", slug: "marriott", thumbnail: "../../media/thumbnails/marriott.jpg" }},
            {{ title: "NIKON: CLARK LITTLE", category: "Commercial", slug: "nikon-clark-little", thumbnail: "../../media/thumbnails/nikon-clark.jpg" }},
            {{ title: "NIKON: IVAR", category: "Commercial", slug: "nikon-ivar", thumbnail: "../../media/thumbnails/nikon-ivar.jpg" }},
            {{ title: "CHEVROLET", category: "Commercial", slug: "chevrolet", thumbnail: "../../media/thumbnails/chevrolet.jpg" }},
            {{ title: "ICHNUSA", category: "Commercial", slug: "ichnusa", thumbnail: "../../media/thumbnails/ichnusa.jpg" }},
            {{ title: "MILLER GENUINE DRAFT", category: "Commercial", slug: "miller-genuine-draft", thumbnail: "../../media/thumbnails/miller.jpg" }},
            {{ title: "ADIDAS", category: "Commercial", slug: "adidas", thumbnail: "../../media/thumbnails/adidas.jpg" }},
            {{ title: "USPS", category: "Commercial", slug: "usps", thumbnail: "../../media/thumbnails/usps.jpg" }},
            {{ title: "RAM: BONEYARD", category: "Automotive", slug: "ram-boneyard", thumbnail: "../../media/thumbnails/ram-boneyard.jpg" }},
            {{ title: "BENTLEY", category: "Automotive", slug: "bentley", thumbnail: "../../media/thumbnails/bentley.jpg" }},
            {{ title: "ALFA ROMEO", category: "Automotive", slug: "alfa-romeo", thumbnail: "../../media/thumbnails/alfa-romeo.jpg" }},
            {{ title: "INFINITI", category: "Automotive", slug: "infiniti", thumbnail: "../../media/thumbnails/infiniti.jpg" }},
            {{ title: "TOYOTA", category: "Automotive", slug: "toyota", thumbnail: "../../media/thumbnails/toyota.jpg" }},
            {{ title: "TESLA", category: "Automotive", slug: "tesla", thumbnail: "../../media/thumbnails/tesla.jpg" }}
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
</html>'''

    return html

# Update all project pages
projects_dir = Path("v2/projects")
updated_count = 0

for project in projects_data:
    output_path = projects_dir / f"{project['slug']}.html"
    html_content = generate_project_html(project)

    with open(output_path, 'w') as f:
        f.write(html_content)

    updated_count += 1
    print(f"✅ Updated {project['slug']}")

print(f"\n✨ Done! Updated all {updated_count} project pages with the Your Lucky Day design.")
