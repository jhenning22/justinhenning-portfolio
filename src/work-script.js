// Work page script - hover video previews
// No modals - uses link navigation to individual project pages

// Mobile Menu Functionality
const hamburgerBtn = document.getElementById('hamburgerBtn');
const mobileMenu = document.getElementById('mobileMenu');

if (hamburgerBtn && mobileMenu) {
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
}

// Mobile header hide/show on scroll
let lastScrollTop = 0;
let scrollThreshold = 10;

window.addEventListener('scroll', () => {
    if (window.innerWidth > 768) return;

    const header = document.querySelector('header');
    const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll <= 0) {
        header.classList.remove('header-hidden');
        return;
    }

    if (Math.abs(currentScroll - lastScrollTop) < scrollThreshold) {
        return;
    }

    if (currentScroll > lastScrollTop) {
        header.classList.add('header-hidden');
    } else {
        header.classList.remove('header-hidden');
    }

    lastScrollTop = currentScroll;
}, { passive: true });

// Intersection Observer for lazy loading thumbnails
const thumbnailObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            if (img.dataset.src && !img.src) {
                // Load the image
                img.src = img.dataset.src;

                // Load WebP source if available
                const picture = img.parentElement;
                const webpSource = picture.querySelector('source[type="image/webp"]');
                if (webpSource && webpSource.dataset.srcset) {
                    webpSource.srcset = webpSource.dataset.srcset;
                }

                // Add loaded class for fade-in effect
                img.onload = () => {
                    img.classList.add('loaded');
                };

                thumbnailObserver.unobserve(img);
            }
        }
    });
}, {
    rootMargin: '100px' // Load thumbnails 100px before they enter viewport
});

// Intersection Observer for lazy loading videos
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
document.addEventListener('DOMContentLoaded', () => {
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach((card) => {
        // Lazy load thumbnails
        const thumbnail = card.querySelector('.thumbnail-img');
        if (thumbnail) {
            thumbnailObserver.observe(thumbnail);
        }

        // Lazy load and handle video previews
        const video = card.querySelector('.project-video');

        if (video) {
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
                video.play().then(() => {
                    video.classList.add('loaded');
                }).catch(err => console.log('Video play prevented:', err));
            });

            // Pause and reset video when not hovering
            card.addEventListener('mouseleave', () => {
                video.pause();
                video.currentTime = 0;
                video.classList.remove('loaded');
            });
        }
    });

    // Filter functionality
    const filterBtns = document.querySelectorAll('.main-side-nav .side-nav-btn');
    const mobileFilterBtns = document.querySelectorAll('.mobile-menu-filters .mobile-menu-btn[data-filter]');
    const projectGrid = document.querySelector('.project-grid');

    // Function to apply filter
    function applyFilter(filter) {
        // Update side nav active state
        filterBtns.forEach(b => {
            if (b.dataset.filter === filter) {
                b.classList.add('active');
            } else {
                b.classList.remove('active');
            }
        });

        // Filter projects
        projectCards.forEach(card => {
            const category = card.dataset.category;
            if (filter === 'all' || category === filter) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    }

    if (filterBtns.length > 0 && projectGrid) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const filter = btn.dataset.filter;
                applyFilter(filter);
                window.location.hash = filter;
            });
        });

        // Mobile filter button handlers
        mobileFilterBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const filter = btn.dataset.filter;

                // Close mobile menu
                const mobileMenu = document.getElementById('mobileMenu');
                const hamburgerBtn = document.getElementById('hamburgerBtn');
                if (mobileMenu) mobileMenu.classList.remove('active');
                if (hamburgerBtn) hamburgerBtn.classList.remove('active');
                document.body.classList.remove('menu-open');
                document.body.style.overflow = 'auto';

                // Apply filter
                applyFilter(filter);
                window.location.hash = filter;
            });
        });

        // Handle initial hash on page load
        const hash = window.location.hash.replace('#', '');
        if (hash && hash !== 'info') {
            applyFilter(hash);
        }
    }
});
