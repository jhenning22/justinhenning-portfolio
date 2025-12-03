// Project data with Vimeo IDs and local video files
const projects = [
    {
        title: "YOUR LUCKY DAY",
        subtitle: "Feature Film",
        category: "Film",
        vimeoId: "872749030",
        videoFile: "media/videos/your-lucky-day.mp4",
        director: "Dan Brown",
        synopsis: "A dispute over a winning lottery ticket escalates into a deadly hostage situation. The witnesses must decide how far they'll go—and how much blood they're willing to spill—for a cut of the $156 million prize.",
        cast: "Angus Cloud, Elliot Knight, Jessica Garza, Sterling Beaumon, Mousa Hussein Kraish, Jason Wiles, Sebastian Sozzi, Spencer Garrett, Jason O'Mara",
        premiere: "September 23, 2023 at Fantastic Fest",
        platform: "Netflix"
    },
    {
        title: "WOODFORD RESERVE",
        subtitle: "The Derby",
        category: "Commercial",
        vimeoId: "898398761",
        videoFile: "media/videos/woodford-reserve.mov",
        director: "David Holm"
    },
    {
        title: "KIA",
        subtitle: "The Good Life",
        category: "Automotive",
        vimeoId: "913839989",
        videoFile: "media/videos/kia.mp4",
        director: "Brent Foster"
    },
    {
        title: "ROYAL BANK OF CANADA",
        subtitle: "Windy",
        category: "Commercial",
        vimeoId: "891284220",
        videoFile: "media/videos/rbc.mov",
        director: "David Holm",
        cast: "Sahith Theegala, Cameron Young, Sam Burns"
    },
    {
        title: "K&N",
        subtitle: null,
        category: "Automotive",
        vimeoId: "523316278",
        videoFile: "media/videos/kn.mov",
        director: "Miko Lim"
    },
    {
        title: "RAM",
        subtitle: "Paramotor",
        category: "Automotive",
        vimeoId: "930752804",
        videoFile: "media/videos/ram.mov",
        director: "David Holm"
    },
    {
        title: "AUDI",
        subtitle: "Listen",
        category: "Automotive",
        vimeoId: "163036231",
        videoFile: "media/videos/audi.mp4",
        director: "David Holm"
    },
    {
        title: "JEEP",
        subtitle: "Hero's Journey",
        category: "Automotive",
        vimeoId: "898405588",
        videoFile: "media/videos/jeep.mp4",
        director: "David Holm"
    },
    {
        title: "FORD",
        subtitle: "Expedition",
        category: "Automotive",
        vimeoId: "745033991",
        videoFile: "media/videos/ford.mov",
        director: "Scott Weintrob"
    },
    {
        title: "AMERICAN OUTLAWS",
        subtitle: "Feature Film",
        category: "Film",
        vimeoId: "797538936",
        videoFile: "media/videos/american-outlaws.mp4",
        director: "Sean McEwen",
        synopsis: "Three siblings embark on a cross-country crime spree while facing potential imprisonment and seeking an idealized freedom. Based on true events from Kathy Dobie's GQ article 'The Whole True Story of the Dougherty Gang.'",
        cast: "Emory Cohen, India Eisley, Sam Strike, Treat Williams, Tess Harper",
        premiere: "2023 Santa Barbara International Film Festival"
    },
    {
        title: "ANA PAULA",
        subtitle: "Short Film",
        category: "Film",
        vimeoId: "840254843",
        videoFile: "media/videos/ana-paula.mp4",
        director: "Leigh Marling",
        synopsis: "Filmed on location in Durango, Mexico with a non-professional local cast, ANA PAULA is the heartbreaking story of a young woman determined to escape her dark past and adopt her niece from a government orphanage. To meet the strict criteria for adoption, Ana is working at a local hotel, attending interviews at the orphanage, and trying to save money for an apartment. When a judge explains her case cannot proceed for lack of a 'suitable home', Ana employs desperate measures to find the necessary cash. An admiring co-worker - Fernando - sees her desperation and offers to help, but after Ana agrees she finds herself drawn into a tragic romance. Soon, Ana's past comes back to haunt her. She is pulled back into a toxic life of vice that brings her into direct conflict with Fernando, her own inner demons, and the ruthless criminals who seek to destroy any chance of Ana becoming a mother.",
        awards: "Winner of Best Foreign Short at the Burbank International Film Festival and Best Short Feature Film at the Arizona International Film Festival in 2024",
        startTime: 0.32
    },
    {
        title: "LA LUCHA",
        subtitle: "Short Film",
        category: "Film",
        vimeoId: "180678668",
        videoFile: "media/videos/la-lucha.mp4",
        director: "Isaac Rodriguez"
    },
    {
        title: "PEI",
        subtitle: "Prince Edward Island",
        category: "Commercial",
        vimeoId: "374024991",
        videoFile: "media/videos/pei.mov",
        director: "Brent Foster"
    },
    {
        title: "LAMBORGHINI",
        subtitle: "The Wind",
        category: "Automotive",
        vimeoId: "242791079",
        videoFile: "media/videos/lamborghini.mov",
        director: "David Holm"
    },
    {
        title: "RALPH LAUREN",
        subtitle: "Polo Blue",
        category: "Commercial",
        vimeoId: "261889797",
        videoFile: "media/videos/ralph-lauren.mp4",
        director: "David Holm"
    },
    {
        title: "GATORADE",
        subtitle: null,
        category: "Commercial",
        vimeoId: "1046557409",
        videoFile: "media/videos/gatorade.mp4",
        director: "Christian Sorensen Hansen",
        startTime: 1.2
    },
    {
        title: "MARRIOTT",
        subtitle: null,
        category: "Commercial",
        vimeoId: "124659863",
        videoFile: "media/videos/marriott.mp4",
        director: "David Holm"
    },
    {
        title: "NIKON: CLARK LITTLE",
        subtitle: null,
        category: "Commercial",
        vimeoId: "165219350",
        videoFile: "media/videos/nikon-clark.mov",
        director: "David Holm"
    },
    {
        title: "NIKON: IVAR",
        subtitle: null,
        category: "Commercial",
        vimeoId: "155239464",
        videoFile: "media/videos/nikon-ivar.mov",
        director: "David Holm"
    },
    {
        title: "CHEVROLET",
        subtitle: null,
        category: "Commercial",
        vimeoId: "436669633",
        videoFile: "media/videos/chevrolet.mov",
        director: "David Holm"
    },
    {
        title: "ADIDAS",
        subtitle: null,
        category: "Commercial",
        vimeoId: "374027701",
        videoFile: "media/videos/adidas.mov",
        director: "John Merizalde"
    },
    {
        title: "RAM: BONEYARD",
        subtitle: null,
        category: "Automotive",
        vimeoId: "222244036",
        videoFile: "media/videos/ram-boneyard.mp4",
        director: "David Holm"
    },
    {
        title: "ALFA ROMEO",
        subtitle: null,
        category: "Automotive",
        vimeoId: "248727672",
        videoFile: "media/videos/alfa-romeo.mp4",
        director: "David Holm"
    },
    {
        title: "TESLA",
        subtitle: null,
        category: "Automotive",
        vimeoId: "148737078",
        videoFile: "media/videos/tesla.mp4",
        director: "David Holm"
    }
];

// State management
let currentProjectIndex = 0;
let filteredProjects = [...projects];

// Utility functions for URL slugs
function generateSlug(title) {
    return title
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')  // Replace non-alphanumeric with hyphens
        .replace(/^-+|-+$/g, '');      // Remove leading/trailing hyphens
}

function getProjectIndexBySlug(slug) {
    return projects.findIndex(project => generateSlug(project.title) === slug);
}

function getActiveFilter() {
    const activeFilterBtn = document.querySelector('.side-nav-btn.active');
    return activeFilterBtn ? activeFilterBtn.dataset.filter : 'all';
}

// DOM Elements
const infoLink = document.getElementById('infoLink');
const workLink = document.getElementById('workLink');
const headerTitleLink = document.getElementById('headerTitleLink');
const infoPage = document.getElementById('infoPage');
const mainContent = document.getElementById('mainContent');
const videoModal = document.getElementById('videoModal');
const vimeoPlayer = document.getElementById('vimeoPlayer');
const modalTitle = document.getElementById('modalTitle');
const modalCategory = document.getElementById('modalCategory');
const closeModal = document.getElementById('closeModal');
const prevProject = document.getElementById('prevProject');
const nextProject = document.getElementById('nextProject');
const projectCards = document.querySelectorAll('.project-card');
const filterBtns = document.querySelectorAll('.main-side-nav .side-nav-btn');

// Function to show info page
function showInfoPage() {
    mainContent.style.display = 'none';
    infoPage.classList.add('active');

    // Force header to black text on info page
    document.body.classList.remove('at-grid');
    document.body.classList.add('at-info');

    window.scrollTo(0, 0);

    // Update active states
    workLink.classList.remove('active');
    infoLink.classList.add('active');
}

// Function to show work page
function showWorkPage() {
    infoPage.classList.remove('active');
    mainContent.style.display = 'block';

    // Remove info page class, add grid class
    document.body.classList.remove('at-info');
    document.body.classList.add('at-grid');

    // Update active states
    infoLink.classList.remove('active');
    workLink.classList.add('active');

    // Scroll to top of the page
    // Use requestAnimationFrame to ensure DOM is ready (Chrome compatibility)
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    });
}

// Toggle Information Page
infoLink.addEventListener('click', (e) => {
    e.preventDefault();
    showInfoPage();
    history.pushState({ page: 'info' }, '', '#info');
});

// Close Information Page (WORK link)
workLink.addEventListener('click', (e) => {
    e.preventDefault();
    showWorkPage();
    // Use replaceState instead of pushState to not add extra history entry
    // Just remove the hash to show we're on the work page
    if (window.location.hash === '#info') {
        history.pushState({ page: 'work' }, '', window.location.pathname);
    }
});

// Header title link now navigates to landing.html (no JavaScript handling needed)

// Handle browser back/forward buttons
window.addEventListener('popstate', (e) => {
    const filterHashes = ['#all', '#film', '#commercial', '#automotive'];

    // Check if navigating to a filter
    if (window.location.hash && filterHashes.includes(window.location.hash)) {
        const filter = window.location.hash.substring(1);

        // Apply the filter
        filterBtns.forEach(btn => {
            if (btn.dataset.filter === filter) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Filter project cards
        projectCards.forEach(card => {
            const category = card.dataset.category;
            if (filter === 'all' || category === filter) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        });

        // Update filtered projects array
        if (filter === 'all') {
            filteredProjects = [...projects];
        } else {
            filteredProjects = projects.filter((project, index) => {
                const card = document.querySelector(`[data-project="${index}"]`);
                return card && card.dataset.category === filter;
            });
        }

        // Show work page if needed
        if (infoPage.classList.contains('active')) {
            showWorkPage();
        } else {
            // Scroll directly to grid
            window.scrollTo({
                top: window.innerHeight,
                behavior: 'smooth'
            });
        }
        return;
    }

    // Check if navigating to a video
    if (e.state && e.state.page === 'work' && e.state.videoIndex !== undefined) {
        // Restore filter state if present
        if (e.state.filter && e.state.filter !== getActiveFilter()) {
            const filterBtn = document.querySelector(`.side-nav-btn[data-filter="${e.state.filter}"]`);
            if (filterBtn) {
                filterBtn.click();
            }
        }
        // Open the video modal without updating history
        openVideoModal(e.state.videoIndex, false);
    }
    // Check if navigating back from video (work page with no video)
    else if (e.state && e.state.page === 'work' && e.state.videoIndex === undefined) {
        // Close modal if it's open
        if (!videoModal.classList.contains('hidden')) {
            videoModal.classList.add('hidden');
            document.body.style.overflow = 'auto';
            vimeoPlayer.src = '';
        }
        // Restore filter state if present
        if (e.state.filter && e.state.filter !== getActiveFilter()) {
            const filterBtn = document.querySelector(`.side-nav-btn[data-filter="${e.state.filter}"]`);
            if (filterBtn) {
                filterBtn.click();
            }
        }
        showWorkPage();
    }
    // Handle info page
    else if (e.state && e.state.page === 'info') {
        showInfoPage();
    } else if (window.location.hash === '#info') {
        showInfoPage();
    }
    // Check for video hash in URL (for direct links)
    else if (window.location.hash && window.location.hash.startsWith('#') && window.location.hash !== '#info') {
        const slug = window.location.hash.substring(1);
        const projectIndex = getProjectIndexBySlug(slug);
        if (projectIndex !== -1) {
            openVideoModal(projectIndex, false);
        } else {
            showWorkPage();
        }
    }
    else {
        showWorkPage();
    }
});

// Check for #info hash or video hash on page load
window.addEventListener('DOMContentLoaded', () => {
    const hash = window.location.hash;
    const filterHashes = ['#all', '#film', '#commercial', '#automotive'];

    // Check if URL has a filter hash
    if (filterHashes.includes(hash)) {
        const filter = hash.substring(1);

        // Ensure main content is visible
        if (infoPage) {
            infoPage.classList.remove('active');
        }
        if (mainContent) {
            mainContent.style.display = 'block';
        }

        // Apply the filter
        filterBtns.forEach(btn => {
            if (btn.dataset.filter === filter) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Filter project cards
        projectCards.forEach(card => {
            const category = card.dataset.category;
            if (filter === 'all' || category === filter) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        });

        // Update filtered projects array
        if (filter === 'all') {
            filteredProjects = [...projects];
        } else {
            filteredProjects = projects.filter((project, index) => {
                const card = document.querySelector(`[data-project="${index}"]`);
                return card && card.dataset.category === filter;
            });
        }

        // Scroll directly to grid
        window.scrollTo({
            top: window.innerHeight,
            behavior: 'smooth'
        });

        history.replaceState({ page: 'work', filter: filter }, '', window.location.href);
        return;
    }

    // Check if URL has a video hash
    if (hash && hash !== '#info') {
        const slug = hash.substring(1);
        const projectIndex = getProjectIndexBySlug(slug);

        // If valid project slug found, open that video
        if (projectIndex !== -1) {
            const currentFilter = getActiveFilter();
            history.replaceState(
                { page: 'work', videoIndex: projectIndex, filter: currentFilter },
                '',
                window.location.href
            );
            openVideoModal(projectIndex, false);
            return;
        }
    }

    // Replace current history state to track initial page
    const initialPage = hash === '#info' ? 'info' : 'work';
    history.replaceState({ page: initialPage }, '', window.location.href);

    if (hash === '#info') {
        showInfoPage();
    }
});

// Filter Projects
filterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        const filter = btn.dataset.filter;

        // If info page is active, show work page first
        if (infoPage.classList.contains('active')) {
            infoPage.classList.remove('active');
            mainContent.style.display = 'block';

            // Update navigation states
            infoLink.classList.remove('active');
            workLink.classList.add('active');
        }

        // Update active button
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Filter projects
        projectCards.forEach(card => {
            const category = card.dataset.category;
            if (filter === 'all' || category === filter) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        });

        // Update filtered projects array
        if (filter === 'all') {
            filteredProjects = [...projects];
        } else {
            filteredProjects = projects.filter((project, index) => {
                const card = document.querySelector(`[data-project="${index}"]`);
                return card && card.dataset.category === filter;
            });
        }

        // Update URL hash
        const hashValue = filter === 'all' ? '#all' : `#${filter}`;
        history.pushState({ page: 'work', filter: filter }, '', hashValue);

        // Scroll to top of grid
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

// Restructure project cards: move text above images
projectCards.forEach((card) => {
    const projectIndex = parseInt(card.dataset.project);
    const project = projects[projectIndex];

    // Skip if already restructured
    if (card.querySelector('.media-container')) {
        return;
    }

    const projectNumber = card.querySelector('.project-number');
    const projectImage = card.querySelector('.project-image');
    const projectVideo = card.querySelector('.project-video');
    const projectInfo = card.querySelector('.project-info');

    // Create caption with number and title
    const caption = document.createElement('div');
    caption.className = 'project-caption';

    // Add number inline with title
    if (projectNumber) {
        caption.appendChild(projectNumber);
    }

    // Add title
    const titleSpan = document.createElement('span');
    titleSpan.className = 'caption-title';
    titleSpan.textContent = project.title;
    caption.appendChild(titleSpan);

    // Add subtitle if exists
    if (project && project.subtitle) {
        const subtitleSpan = document.createElement('span');
        subtitleSpan.className = 'caption-subtitle';
        subtitleSpan.textContent = project.subtitle;
        caption.appendChild(subtitleSpan);
    }

    // Create media container
    const mediaContainer = document.createElement('div');
    mediaContainer.className = 'media-container';

    if (projectImage) {
        mediaContainer.appendChild(projectImage);
    }
    if (projectVideo) {
        mediaContainer.appendChild(projectVideo);
    }

    // Clear card and rebuild in correct order
    card.innerHTML = '';
    card.appendChild(caption);
    card.appendChild(mediaContainer);
});

// Lazy load videos when they come into viewport
const videoObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const video = entry.target;
            const source = video.querySelector('source');
            if (source && !video.src && source.dataset.src) {
                source.src = source.dataset.src;
                video.load();
                videoObserver.unobserve(video);
            }
        }
    });
}, {
    rootMargin: '200px' // Load videos 200px before they enter viewport
});

// Hover Video Preview
projectCards.forEach((card, index) => {
    const video = card.querySelector('.project-video');

    if (video) {
        const projectIndex = parseInt(card.dataset.project);
        const project = projects[projectIndex];
        const startTime = project?.startTime || 0;

        // Set preload to none for better initial load
        video.preload = 'none';

        // Observe video for lazy loading
        videoObserver.observe(video);

        // Play video on hover - load if not already loaded
        card.addEventListener('mouseenter', () => {
            const source = video.querySelector('source');
            if (source && !video.src && source.dataset.src) {
                source.src = source.dataset.src;
                video.load();
            }
            video.currentTime = startTime;
            video.play().then(() => {
                video.classList.add('loaded');
            }).catch(err => console.log('Video play prevented:', err));
        });

        // Pause and reset video when not hovering
        card.addEventListener('mouseleave', () => {
            video.pause();
            video.currentTime = startTime;
            video.classList.remove('loaded');
        });
    }

    // For v2: Skip click handlers for <a> tags - let them navigate naturally
    if (card.tagName === 'A') {
        return;
    }

    // Click to open full video in modal (only for non-link cards)
    card.addEventListener('click', () => {
        const projectIndex = parseInt(card.dataset.project);
        openVideoModal(projectIndex);
    });
});

function openVideoModal(index, updateHistory = true) {
    currentProjectIndex = index;
    const project = projects[index];

    // Update modal content
    modalTitle.textContent = project.title;
    modalCategory.textContent = project.category;

    // Set Vimeo embed URL with autoplay
    vimeoPlayer.src = `https://player.vimeo.com/video/${project.vimeoId}?autoplay=1&autopause=0&color=ffffff&title=0&byline=0&portrait=0`;

    // Update project details
    const modalDetails = document.getElementById('modalDetails');
    if (project.director || project.synopsis || project.cast || project.premiere || project.platform) {
        let detailsHTML = '<div class="details-grid">';

        if (project.director) {
            detailsHTML += `
                <div class="detail-item">
                    <h3>Director</h3>
                    <p>${project.director}</p>
                </div>
            `;
        }

        if (project.synopsis) {
            detailsHTML += `
                <div class="detail-item detail-full">
                    <h3>Synopsis</h3>
                    <p>${project.synopsis}</p>
                </div>
            `;
        }

        if (project.cast) {
            detailsHTML += `
                <div class="detail-item detail-full">
                    <h3>Cast</h3>
                    <p>${project.cast}</p>
                </div>
            `;
        }

        if (project.premiere) {
            detailsHTML += `
                <div class="detail-item">
                    <h3>Premiere</h3>
                    <p>${project.premiere}</p>
                </div>
            `;
        }

        if (project.platform) {
            detailsHTML += `
                <div class="detail-item">
                    <h3>Available On</h3>
                    <p>${project.platform}</p>
                </div>
            `;
        }

        if (project.awards) {
            detailsHTML += `
                <div class="detail-item detail-full">
                    <h3>Awards</h3>
                    <p>${project.awards}</p>
                </div>
            `;
        }

        if (project.credits) {
            detailsHTML += `
                <div class="detail-item detail-full">
                    <h3>Credits</h3>
                    <p>${project.credits}</p>
                </div>
            `;
        }

        detailsHTML += '</div>';
        modalDetails.innerHTML = detailsHTML;
        modalDetails.style.display = 'block';
    } else {
        modalDetails.innerHTML = '';
        modalDetails.style.display = 'none';
    }

    // Show modal
    videoModal.classList.remove('hidden');
    document.body.classList.add('modal-open');
    document.body.style.overflow = 'hidden';

    // Push history state with video slug
    if (updateHistory) {
        const slug = generateSlug(project.title);
        const currentFilter = getActiveFilter();
        history.pushState(
            { page: 'work', videoIndex: index, filter: currentFilter },
            '',
            `#${slug}`
        );
    }
}

// Close Video Modal (only if modal exists - v1 only)
if (closeModal) {
    closeModal.addEventListener('click', () => {
        closeVideoModal();
    });
}

function closeVideoModal() {
    videoModal.classList.add('hidden');
    document.body.classList.remove('modal-open');
    document.body.style.overflow = 'auto';
    // Clear the iframe src to stop the video
    vimeoPlayer.src = '';

    // Update URL to remove video hash
    if (window.location.hash && window.location.hash !== '#info') {
        const currentFilter = getActiveFilter();
        history.pushState(
            { page: 'work', filter: currentFilter },
            '',
            window.location.pathname
        );
    }
}

// Navigate to Previous Project (only if modal exists - v1 only)
if (prevProject) {
    prevProject.addEventListener('click', () => {
        currentProjectIndex = (currentProjectIndex - 1 + projects.length) % projects.length;
        openVideoModal(currentProjectIndex);
    });
}

// Navigate to Next Project (only if modal exists - v1 only)
if (nextProject) {
    nextProject.addEventListener('click', () => {
        currentProjectIndex = (currentProjectIndex + 1) % projects.length;
        openVideoModal(currentProjectIndex);
    });
}

// Keyboard Navigation
document.addEventListener('keydown', (e) => {
    // Modal keyboard nav (only if modal exists - v1 only)
    if (videoModal && !videoModal.classList.contains('hidden')) {
        if (e.key === 'Escape') {
            closeVideoModal();
        } else if (e.key === 'ArrowLeft') {
            prevProject.click();
        } else if (e.key === 'ArrowRight') {
            nextProject.click();
        }
    }

    // Close info page with Escape
    if (infoPage && infoPage.classList.contains('active') && e.key === 'Escape') {
        infoPage.classList.remove('active');
        mainContent.style.display = 'block';
        window.scrollTo(0, 0);
    }
});

// Close modal when clicking outside video (only if modal exists - v1 only)
if (videoModal) {
    videoModal.addEventListener('click', (e) => {
        if (e.target === videoModal) {
            closeVideoModal();
        }
    });
}

// Prevent video click from closing modal (only if modal exists - v1 only)
const videoContainer = document.querySelector('.video-container');
if (videoContainer) {
    videoContainer.addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

// Set grid state on page load
window.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('at-grid');
});

// Mobile Menu Functionality
const hamburgerBtn = document.getElementById('hamburgerBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileInfoLink = document.getElementById('mobileInfoLink');
const mobileFilterBtns = document.querySelectorAll('.mobile-menu-btn[data-filter]');

// Toggle mobile menu
hamburgerBtn.addEventListener('click', () => {
    const isOpening = !mobileMenu.classList.contains('active');
    mobileMenu.classList.toggle('active');
    hamburgerBtn.classList.toggle('active');
    document.body.classList.toggle('menu-open');

    // Prevent body scroll when menu is open
    if (isOpening) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
});

// Handle filter selection in mobile menu
mobileFilterBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.stopPropagation();

        // Get filter value
        const filter = btn.getAttribute('data-filter');

        // Close menu immediately
        mobileMenu.classList.remove('active');
        hamburgerBtn.classList.remove('active');
        document.body.classList.remove('menu-open');
        document.body.style.overflow = 'auto';

        // Let the hash change naturally (don't prevent default)
        // The existing hash change handlers will pick it up

        // Scroll to grid after a brief delay
        setTimeout(() => {
            const mainContent = document.getElementById('mainContent');
            if (mainContent) {
                mainContent.scrollIntoView({ behavior: 'smooth' });
            }
        }, 300);
    });
});

// Handle Info link in mobile menu
mobileInfoLink.addEventListener('click', (e) => {
    e.preventDefault();

    // Close mobile menu
    mobileMenu.classList.remove('active');
    hamburgerBtn.classList.remove('active');
    document.body.classList.remove('menu-open');
    document.body.style.overflow = 'auto';

    // Trigger info page
    infoLink.click();
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (mobileMenu.classList.contains('active') &&
        !mobileMenu.contains(e.target) &&
        !hamburgerBtn.contains(e.target)) {
        mobileMenu.classList.remove('active');
        hamburgerBtn.classList.remove('active');
        document.body.classList.remove('menu-open');
        document.body.style.overflow = 'auto';
    }
});

// Handle orientation change to restart videos on mobile
let orientationChangeTimeout;
window.addEventListener('orientationchange', () => {
    // Clear any existing timeout
    clearTimeout(orientationChangeTimeout);

    // Wait for the orientation change to complete and layout to settle
    orientationChangeTimeout = setTimeout(() => {
        // Find all visible project videos
        const projectCards = document.querySelectorAll('.project-card');

        projectCards.forEach(card => {
            const video = card.querySelector('.project-video');
            if (!video) return;

            const source = video.querySelector('source');
            const projectIndex = parseInt(card.dataset.project);
            const project = projects[projectIndex];
            const startTime = project?.startTime || 0;

            // Check if video is in viewport
            const rect = card.getBoundingClientRect();
            const isVisible = (
                rect.top < window.innerHeight &&
                rect.bottom > 0 &&
                rect.left < window.innerWidth &&
                rect.right > 0
            );

            if (isVisible) {
                // Load video source if not already loaded
                if (source && !video.src && source.dataset.src) {
                    source.src = source.dataset.src;
                    video.load();
                }

                // Try to play the video
                video.currentTime = startTime;
                video.play().then(() => {
                    video.classList.add('loaded');
                }).catch(err => {
                    // Mobile browsers may still block autoplay - that's okay
                    console.log('Video autoplay prevented after orientation change:', err);
                });
            }
        });
    }, 300); // Wait 300ms for orientation change to complete
});

// Also handle resize events (some browsers fire this instead of orientationchange)
let resizeTimeout;
window.addEventListener('resize', () => {
    // Only handle on mobile devices
    if (window.innerWidth > 768) return;

    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        // Trigger the same logic as orientation change
        const event = new Event('orientationchange');
        window.dispatchEvent(event);
    }, 300);
});

// Mobile header hide/show on scroll
let lastScrollTop = 0;
let scrollThreshold = 10; // Minimum scroll distance before hiding/showing

window.addEventListener('scroll', () => {
    // Only apply on mobile
    if (window.innerWidth > 768) return;

    const header = document.querySelector('header');
    const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    // Don't hide if at the top of the page
    if (currentScroll <= 0) {
        header.classList.remove('header-hidden');
        return;
    }

    // Check scroll direction
    if (Math.abs(currentScroll - lastScrollTop) < scrollThreshold) {
        return; // Not scrolled enough to trigger
    }

    if (currentScroll > lastScrollTop) {
        // Scrolling down - hide header
        header.classList.add('header-hidden');
    } else {
        // Scrolling up - show header
        header.classList.remove('header-hidden');
    }

    lastScrollTop = currentScroll;
}, { passive: true });
