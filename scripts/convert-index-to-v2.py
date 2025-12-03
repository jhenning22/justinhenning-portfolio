#!/usr/bin/env python3

"""
Convert index.html to v2/index.html with link-based navigation
"""

import re

# Read the original index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Projects mapping (title to slug)
project_mapping = [
    ("YOUR LUCKY DAY", "your-lucky-day"),
    ("WOODFORD RESERVE", "woodford-reserve"),
    ("HUAWEI", "huawei"),
    ("KIA", "kia"),
    ("ROYAL BANK OF CANADA", "royal-bank-of-canada"),
    ("K&N", "k-n"),
    ("RAM", "ram"),
    ("AUDI", "audi"),
    ("JEEP", "jeep"),
    ("FORD", "ford"),
    ("AMERICAN OUTLAWS", "american-outlaws"),
    ("ANA PAULA", "ana-paula"),
    ("LA LUCHA", "la-lucha"),
    ("PEI", "pei"),
    ("LAMBORGHINI", "lamborghini"),
    ("", ""), # Skip 15 (Nikon photography - removed from main list)
    ("RALPH LAUREN", "ralph-lauren"),
    ("GATORADE", "gatorade"),
    ("MARRIOTT", "marriott"),
    ("NIKON: CLARK LITTLE", "nikon-clark-little"),
    ("NIKON: IVAR", "nikon-ivar"),
    ("CHEVROLET", "chevrolet"),
    ("ICHNUSA", "ichnusa"),
    ("MILLER GENUINE DRAFT", "miller-genuine-draft"),
    ("ADIDAS", "adidas"),
    ("USPS", "usps"),
    ("RAM: BONEYARD", "ram-boneyard"),
    ("BENTLEY", "bentley"),
    ("ALFA ROMEO", "alfa-romeo"),
    ("INFINITI", "infiniti"),
    ("TOYOTA", "toyota"),
    ("TESLA", "tesla"),
]

# Convert each project card from div to anchor
for i, (title, slug) in enumerate(project_mapping):
    if not slug:  # Skip empty entries
        continue

    # Pattern to match the project card div
    # Looking for: <div class="project-card" data-category="..." data-project="N">
    pattern = f'<div class="project-card" data-category="([^"]+)" data-project="{i}">'
    replacement = f'<a href="projects/{slug}.html" class="project-card" data-category="\\1" data-project="{i}">'
    html = html.replace(pattern, replacement)

    # Close the anchor tag (replace closing </div> at end of project-card)
    # This is tricky - we need to find the closing div for each project card
    # Since structure is consistent, we can replace the pattern more carefully

# Actually, let's use a more robust approach - replace all project-card divs with anchors
# Find all project card blocks and convert them

def convert_project_card(match):
    """Convert a project card div to an anchor"""
    category = match.group(1)
    project_num = int(match.group(2))

    # Get slug for this project number
    if project_num < len(project_mapping):
        title, slug = project_mapping[project_num]
        if slug:
            return f'<a href="projects/{slug}.html" class="project-card" data-category="{category}" data-project="{project_num}">'

    # Fallback - keep as div if no mapping
    return match.group(0)

# Replace project-card divs with anchors
html = re.sub(
    r'<div class="project-card" data-category="([^"]+)" data-project="(\d+)">',
    convert_project_card,
    html
)

# Replace the closing </div> after </div> (project-info closing) for each project card
# More robust: replace pattern of project-info closing + card closing
html = re.sub(
    r'(</div>\s*<!-- Project Info -->\s*)</div>(\s*\n\s*<!-- )',
    r'\1</a>\2',
    html
)

# Also handle the last project card (Tesla) which doesn't have a comment after
html = re.sub(
    r'(</div>\s*</div>\s*</div>\s*<!-- Tesla -->)',
    lambda m: m.group(0).replace('</div>\n            </div>', '</div>\n            </a>'),
    html,
    count=1
)

# Actually, let's be more precise. Each project card ends with:
# </div> (project-info)
# </div> (project-card)
# We need to replace the second one with </a>

# Let's use a different approach - split and rejoin
lines = html.split('\n')
new_lines = []
in_project_card = False
project_card_depth = 0

for i, line in enumerate(lines):
    # Check if this line opens a project card
    if '<a href="projects/' in line and 'class="project-card"' in line:
        in_project_card = True
        project_card_depth = 0
        new_lines.append(line)
        continue

    # Track div depth within project card
    if in_project_card:
        if '<div' in line:
            project_card_depth += line.count('<div')
        if '</div>' in line:
            project_card_depth -= line.count('</div>')

            # If we're back to -1, we've closed the project card
            if project_card_depth < 0:
                new_lines.append(line.replace('</div>', '</a>', 1))
                in_project_card = False
                project_card_depth = 0
                continue

    new_lines.append(line)

html = '\n'.join(new_lines)

# Remove the video modal section (lines 561-582)
html = re.sub(
    r'\s*<!-- Video Modal -->.*?</div>\s*</div>\s*\n',
    '\n',
    html,
    flags=re.DOTALL
)

# Update CSS and JS paths to point to parent directory
html = html.replace('href="style.css', 'href="../style.css')
html = html.replace('src="script.js', 'src="../script.js')
html = html.replace('href="photography.html"', 'href="../photography.html"')

# Update version number
html = html.replace('style.css?v=27', 'style.css?v=28')
html = html.replace('script.js?v=6', 'script.js?v=7')

# Write to v2/index.html
with open('v2/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('✅ Successfully converted index.html to v2/index.html')
print('   - Converted project cards from <div> to <a> tags')
print('   - Removed video modal section')
print('   - Updated asset paths for v2 directory structure')
