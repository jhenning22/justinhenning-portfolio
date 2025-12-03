#!/usr/bin/env python3

"""
Generate V2 project pages from projects data
Run with: python3 generate-v2-pages.py
"""

import os
import re

# Project data (from script.js)
projects = [
    {
        "title": "YOUR LUCKY DAY",
        "subtitle": "Feature Film",
        "category": "Film",
        "vimeoId": "872749030",
        "director": "Daniel Brown",
        "synopsis": "A dispute over a winning lottery ticket escalates into a deadly hostage situation. The witnesses must decide how far they'll go—and how much blood they're willing to spill—for a cut of the $156 million prize.",
        "cast": "Angus Cloud, Elliot Knight, Jessica Garza, Sterling Beaumon, Mousa Hussein Kraish, Jason Wiles, Sebastian Sozzi, Spencer Garrett, Jason O'Mara",
        "premiere": "September 23, 2023 at Fantastic Fest",
        "platform": "Netflix"
    },
    {
        "title": "WOODFORD RESERVE",
        "subtitle": "The Derby",
        "category": "Commercial",
        "vimeoId": "898398761",
        "director": "David Holm"
    },
    {
        "title": "HUAWEI",
        "subtitle": "Mate X6",
        "category": "Commercial",
        "vimeoId": "1046541141",
        "director": "Zou",
        "startTime": 0.64
    },
    {
        "title": "KIA",
        "subtitle": "The Good Life",
        "category": "Automotive",
        "vimeoId": "913839989",
        "director": "Brent Foster"
    },
    {
        "title": "ROYAL BANK OF CANADA",
        "subtitle": "Windy",
        "category": "Commercial",
        "vimeoId": "891284220",
        "director": "David Holm",
        "cast": "Sahith Theegala, Cameron Young, Sam Burns"
    },
    {
        "title": "K&N",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "523316278"
    },
    {
        "title": "RAM",
        "subtitle": "Paramotor",
        "category": "Automotive",
        "vimeoId": "930752804",
        "director": "David Holm"
    },
    {
        "title": "AUDI",
        "subtitle": "Listen",
        "category": "Automotive",
        "vimeoId": "163036231",
        "director": "David Holm"
    },
    {
        "title": "JEEP",
        "subtitle": "Hero's Journey",
        "category": "Automotive",
        "vimeoId": "898405588",
        "director": "David Holm"
    },
    {
        "title": "FORD",
        "subtitle": "Expedition",
        "category": "Automotive",
        "vimeoId": "745033991",
        "director": "Scott Weintrob"
    },
    {
        "title": "AMERICAN OUTLAWS",
        "subtitle": "Feature Film",
        "category": "Film",
        "vimeoId": "797538936",
        "director": "Sean McEwen",
        "synopsis": "Three siblings embark on a cross-country crime spree while facing potential imprisonment and seeking an idealized freedom. Based on true events from Kathy Dobie's GQ article 'The Whole True Story of the Dougherty Gang.'",
        "cast": "Emory Cohen, India Eisley, Sam Strike, Treat Williams, Tess Harper",
        "premiere": "2023 Santa Barbara International Film Festival"
    },
    {
        "title": "ANA PAULA",
        "subtitle": "Short Film",
        "category": "Film",
        "vimeoId": "840254843",
        "director": "Leigh Marling",
        "synopsis": "Filmed on location in Durango, Mexico with a non-professional local cast, ANA PAULA is the heartbreaking story of a young woman determined to escape her dark past and adopt her niece from a government orphanage. To meet the strict criteria for adoption, Ana is working at a local hotel, attending interviews at the orphanage, and trying to save money for an apartment. When a judge explains her case cannot proceed for lack of a 'suitable home', Ana employs desperate measures to find the necessary cash. An admiring co-worker - Fernando - sees her desperation and offers to help, but after Ana agrees she finds herself drawn into a tragic romance. Soon, Ana's past comes back to haunt her. She is pulled back into a toxic life of vice that brings her into direct conflict with Fernando, her own inner demons, and the ruthless criminals who seek to destroy any chance of Ana becoming a mother.",
        "awards": "Winner of Best Foreign Short at the Burbank International Film Festival and Best Short Feature Film at the Arizona International Film Festival in 2024",
        "startTime": 0.32
    },
    {
        "title": "LA LUCHA",
        "subtitle": "Documentary Short",
        "category": "Film",
        "vimeoId": "180678668",
        "director": "Justin Henning",
        "synopsis": "In 1962, Fidel Castro banned all professional (for profit) sports in Cuba. For Cuba's top athletes this means a tough choice. Stay in Cuba, their home, or defect and follow their dreams. This is the story of two-time Olympic gold medalist Mario Kindelán Mesa.",
        "awards": "Vimeo Staff Pick",
        "credits": "Produced by SOCIETY (society.tv) in association with EL CENTRAL producciones. Executive Producers: Harry Calbom & David Holm. Producers: Carlos Gómez & Reymel Delgado Rodriguez. Movi Operator: Ryan Haug. Editor: Nick Pezzillo. Colorist: Eric Rosen.",
        "startTime": 0.6
    },
    {
        "title": "PEI",
        "subtitle": "Prince Edward Island",
        "category": "Commercial",
        "vimeoId": "374024991",
        "director": "Brent Foster"
    },
    {
        "title": "LAMBORGHINI",
        "subtitle": "The Wind",
        "category": "Automotive",
        "vimeoId": "242791079",
        "director": "David Holm"
    },
    {
        "title": "RALPH LAUREN",
        "subtitle": "Polo Blue",
        "category": "Commercial",
        "vimeoId": "261889797"
    },
    {
        "title": "GATORADE",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "1046557409",
        "startTime": 1.2
    },
    {
        "title": "MARRIOTT",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "124659863"
    },
    {
        "title": "NIKON: CLARK LITTLE",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "165219350"
    },
    {
        "title": "NIKON: IVAR",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "155239464"
    },
    {
        "title": "CHEVROLET",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "436669633"
    },
    {
        "title": "ICHNUSA",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "222332910"
    },
    {
        "title": "MILLER GENUINE DRAFT",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "405148244"
    },
    {
        "title": "ADIDAS",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "374027701"
    },
    {
        "title": "USPS",
        "subtitle": None,
        "category": "Commercial",
        "vimeoId": "917245566"
    },
    {
        "title": "RAM: BONEYARD",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "222244036",
        "director": "David Holm"
    },
    {
        "title": "BENTLEY",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "805761043"
    },
    {
        "title": "ALFA ROMEO",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "248727672"
    },
    {
        "title": "INFINITI",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "245654221"
    },
    {
        "title": "TOYOTA",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "394801461"
    },
    {
        "title": "TESLA",
        "subtitle": None,
        "category": "Automotive",
        "vimeoId": "148737078"
    }
]

def generate_slug(title):
    """Generate URL-friendly slug from title"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = re.sub(r'^-+|-+$', '', slug)
    return slug

def generate_project_page(project, index, all_projects):
    """Generate HTML for a single project page"""

    # Get prev/next projects (with wrapping)
    prev_index = (index - 1) if index > 0 else len(all_projects) - 1
    next_index = (index + 1) if index < len(all_projects) - 1 else 0

    prev_project = all_projects[prev_index]
    next_project = all_projects[next_index]

    # Build project details HTML
    details_parts = []

    if project.get('director'):
        details_parts.append(f"                <p><strong>Director:</strong> {project['director']}</p>")

    if project.get('synopsis'):
        details_parts.append(f"                <p><strong>Synopsis:</strong> {project['synopsis']}</p>")

    if project.get('cast'):
        details_parts.append(f"                <p><strong>Cast:</strong> {project['cast']}</p>")

    if project.get('premiere'):
        details_parts.append(f"                <p><strong>Premiere:</strong> {project['premiere']}</p>")

    if project.get('platform'):
        details_parts.append(f"                <p><strong>Platform:</strong> {project['platform']}</p>")

    if project.get('awards'):
        details_parts.append(f"                <p><strong>Awards:</strong> {project['awards']}</p>")

    if project.get('credits'):
        details_parts.append(f"                <p><strong>Credits:</strong> {project['credits']}</p>")

    details_html = '\n\n'.join(details_parts) if details_parts else ''

    # Vimeo URL with start time if specified
    start_time_param = f"#t={project['startTime']}" if project.get('startTime') else ''
    vimeo_url = f"https://player.vimeo.com/video/{project['vimeoId']}?autoplay=1&title=0&byline=0&portrait=0{start_time_param}"

    # Generate projects array for navigation JS
    projects_array_js = ',\n'.join([
        f"            {{ title: \"{p['title']}\", category: \"{p['category']}\", slug: \"{p['slug']}\" }}"
        for p in all_projects
    ])

    # Subtitle HTML
    subtitle_html = f"<p class=\"project-subtitle\">{project['subtitle']}</p>" if project.get('subtitle') else ''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project['title']} - Justin Henning</title>
    <link rel="stylesheet" href="../style.css?v=28">
    <style>
        /* Project page specific styles */
        body {{
            background: #000;
            color: #fff;
            overflow-x: hidden;
        }}

        .project-page-header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            padding: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            mix-blend-mode: difference;
        }}

        .back-link {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 0.875rem;
            font-weight: 300;
            letter-spacing: 0.15em;
            text-decoration: none;
            color: #fff;
            transition: opacity 0.3s ease;
        }}

        .back-link:hover {{
            opacity: 0.6;
        }}

        .project-container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 6rem 2rem 4rem;
        }}

        .video-wrapper {{
            position: relative;
            width: 100%;
            padding-bottom: 56.25%; /* 16:9 aspect ratio */
            margin-bottom: 3rem;
            background: #000;
        }}

        .video-wrapper iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }}

        .project-info {{
            max-width: 800px;
            margin: 0 auto 4rem;
        }}

        .project-title {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 2rem;
            font-weight: 300;
            letter-spacing: 0.2em;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }}

        .project-subtitle {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 1rem;
            font-weight: 300;
            letter-spacing: 0.1em;
            color: #999;
            margin-bottom: 2rem;
        }}

        .project-details {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 0.9rem;
            font-weight: 300;
            line-height: 1.8;
            color: #ccc;
        }}

        .project-details p {{
            margin-bottom: 1.5rem;
        }}

        .project-details strong {{
            color: #fff;
            font-weight: 400;
        }}

        .project-navigation {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
            border-top: 1px solid #333;
        }}

        .nav-button {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 0.875rem;
            font-weight: 300;
            letter-spacing: 0.15em;
            text-decoration: none;
            color: #fff;
            padding: 0.75rem 1.5rem;
            border: 1px solid #fff;
            transition: all 0.3s ease;
        }}

        .nav-button:hover {{
            background: #fff;
            color: #000;
        }}

        .nav-button:disabled {{
            opacity: 0.3;
            pointer-events: none;
        }}

        @media (max-width: 768px) {{
            .project-page-header {{
                padding: 1.5rem;
            }}

            .project-container {{
                padding: 5rem 1.5rem 2rem;
            }}

            .project-title {{
                font-size: 1.5rem;
            }}

            .project-navigation {{
                flex-direction: column;
                gap: 1rem;
            }}

            .nav-button {{
                width: 100%;
                text-align: center;
            }}
        }}
    </style>
</head>
<body>
    <!-- Header with back link -->
    <header class="project-page-header">
        <a href="../index.html" class="back-link" id="backLink">← BACK TO GRID</a>
        <a href="../index.html#info" class="back-link">INFORMATION</a>
    </header>

    <!-- Project Content -->
    <div class="project-container">
        <!-- Video Player -->
        <div class="video-wrapper">
            <iframe
                src="{vimeo_url}"
                frameborder="0"
                allow="autoplay; fullscreen; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>

        <!-- Project Information -->
        <div class="project-info">
            <h1 class="project-title">{project['title']}</h1>
            {subtitle_html}

            <div class="project-details">
{details_html}
            </div>
        </div>
    </div>

    <!-- Navigation -->
    <nav class="project-navigation">
        <a href="{prev_project['slug']}.html" class="nav-button" id="prevButton">← PREVIOUS</a>
        <a href="{next_project['slug']}.html" class="nav-button" id="nextButton">NEXT →</a>
    </nav>

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
            index: {index},
            title: "{project['title']}",
            category: "{project['category']}",
            slug: "{project['slug']}"
        }};

        // All projects array
        const projects = [
{projects_array_js}
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

            if (currentIndex > 0) {{
                const prevProject = filteredProjects[currentIndex - 1];
                prevButton.href = `${{prevProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
            }} else {{
                // Wrap to last
                const lastProject = filteredProjects[filteredProjects.length - 1];
                prevButton.href = `${{lastProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
            }}

            if (currentIndex < filteredProjects.length - 1) {{
                const nextProject = filteredProjects[currentIndex + 1];
                nextButton.href = `${{nextProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
            }} else {{
                // Wrap to first
                const firstProject = filteredProjects[0];
                nextButton.href = `${{firstProject.slug}}.html${{activeFilter !== 'all' ? `?filter=${{activeFilter}}` : ''}}`;
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
</html>"""

# Add slugs to all projects
for i, project in enumerate(projects):
    project['slug'] = generate_slug(project['title'])
    project['index'] = i

# Generate all pages
print('Generating V2 project pages...\n')

for i, project in enumerate(projects):
    html = generate_project_page(project, i, projects)
    filename = f"v2/projects/{project['slug']}.html"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✓ Generated: {filename}")

print(f"\n✅ Successfully generated {len(projects)} project pages!")
print('\nProject pages created in: v2/projects/')
print('\nNext steps:')
print('  1. Create v2/index.html with link-based navigation')
print('  2. Convert thumbnails to WebP')
print('  3. Test at http://localhost:8000/v2/')
