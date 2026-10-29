document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const modal = document.getElementById('message-modal');
    const modalMessage = document.getElementById('modal-message');
    const closeModal = document.querySelector('.close');

    // Initialize
    init();

    function init() {
        setupEventListeners();
        setupFAQ();
        setupMobileMenu();
        setupTestimonialsScroll();
        setupFloatingCS();
    }

    function setupEventListeners() {
        // Modal close
        if (closeModal) {
            closeModal.addEventListener('click', hideModal);
        }

        // Close modal when clicking outside
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                hideModal();
            }
        });
    }

    // FAQ Accordion
    function setupFAQ() {
        const faqItems = document.querySelectorAll('.faq-item');
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');

                // Close all other items
                faqItems.forEach(other => {
                    if (other !== item) {
                        other.classList.remove('active');
                    }
                });

                // Toggle current item
                item.classList.toggle('active', !isActive);
            });
        });
    }

    // Mobile Menu
    function setupMobileMenu() {
        const menuBtn = document.getElementById('mobile-menu-btn');
        const navbarLinks = document.querySelector('.navbar-links');
        const navbarCta = document.querySelector('.navbar-cta');
        if (!menuBtn) return;

        menuBtn.addEventListener('click', () => {
            const isOpen = navbarLinks.style.display === 'flex';
            navbarLinks.style.display = isOpen ? 'none' : 'flex';
            if (navbarCta) {
                if (!isOpen) {
                    navbarCta.style.display = 'block';
                    navbarCta.style.marginTop = '12px';
                    navbarCta.style.textAlign = 'center';
                } else {
                    navbarCta.style.display = '';
                    navbarCta.style.marginTop = '';
                    navbarCta.style.textAlign = '';
                }
            }
            if (!isOpen) {
                navbarLinks.style.flexDirection = 'column';
                navbarLinks.style.position = 'absolute';
                navbarLinks.style.top = '64px';
                navbarLinks.style.left = '0';
                navbarLinks.style.right = '0';
                navbarLinks.style.background = '#fff';
                navbarLinks.style.padding = '16px 20px';
                navbarLinks.style.borderBottom = '1px solid #e2e8f0';
                navbarLinks.style.boxShadow = '0 4px 12px rgba(0,0,0,0.08)';
                navbarLinks.style.gap = '16px';
            }
        });
    }

    // Testimonials horizontal scroll
    function setupTestimonialsScroll() {
        var track = document.getElementById('testimonials-track');
        var leftBtn = document.getElementById('scroll-left');
        var rightBtn = document.getElementById('scroll-right');
        if (!track || !leftBtn || !rightBtn) return;

        var scrollAmount = 360;

        leftBtn.addEventListener('click', function() {
            track.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });
        rightBtn.addEventListener('click', function() {
            track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        // Drag to scroll
        var isDown = false;
        var startX;
        var scrollLeft;

        track.addEventListener('mousedown', function(e) {
            isDown = true;
            track.style.cursor = 'grabbing';
            startX = e.pageX - track.offsetLeft;
            scrollLeft = track.scrollLeft;
        });
        track.addEventListener('mouseleave', function() {
            isDown = false;
            track.style.cursor = 'grab';
        });
        track.addEventListener('mouseup', function() {
            isDown = false;
            track.style.cursor = 'grab';
        });
        track.addEventListener('mousemove', function(e) {
            if (!isDown) return;
            e.preventDefault();
            var x = e.pageX - track.offsetLeft;
            var walk = (x - startX) * 1.5;
            track.scrollLeft = scrollLeft - walk;
        });
    }


    // Floating QQ customer service (site-wide)
    function setupFloatingCS() {
        if (document.getElementById('float-cs')) return;

        var wrap = document.createElement('div');
        wrap.className = 'float-cs';
        wrap.id = 'float-cs';
        wrap.innerHTML =
            '<div class="float-cs-panel" id="float-cs-panel" role="dialog" aria-label="客服">' +
            '<h3>需要帮助？</h3>' +
            '<p>客服 QQ <strong>1002569303</strong>。也可打开站内客服中心查看速答。</p>' +
            '<div class="float-cs-actions">' +
            '<a class="primary" href="https://wpa.qq.com/msgrd?v=3&uin=1002569303&site=qq&menu=yes" target="_blank" rel="noopener noreferrer">转人工 QQ</a>' +
            '<a class="secondary" href="/support/">客服中心</a>' +
            '<a class="secondary" href="tencent://message/?uin=1002569303">打开 QQ 客户端</a>' +
            '</div></div>' +
            '<button type="button" class="float-cs-btn" id="float-cs-btn" aria-expanded="false" aria-controls="float-cs-panel">客服<br>QQ</button>';

        document.body.appendChild(wrap);
        var btn = document.getElementById('float-cs-btn');
        var panel = document.getElementById('float-cs-panel');
        btn.addEventListener('click', function () {
            var open = panel.classList.toggle('open');
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        document.addEventListener('click', function (e) {
            if (!wrap.contains(e.target)) {
                panel.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
            }
        });
    }

    function showModal(title, message, type) {
        type = type || 'info';
        const icon = type === 'success' ? '✅' : type === 'error' ? '❌' : 'ℹ️';
        var titleEl = document.createElement('h3');
        titleEl.textContent = icon + ' ' + title;
        var pEl = document.createElement('p');
        pEl.style.marginTop = '15px';
        pEl.style.lineHeight = '1.6';
        pEl.textContent = message;
        modalMessage.textContent = '';
        modalMessage.appendChild(titleEl);
        modalMessage.appendChild(pEl);
        modal.style.display = 'block';

        if (type === 'success') {
            setTimeout(hideModal, 3000);
        }
    }

    function hideModal() {
        modal.style.display = 'none';
    }
});
