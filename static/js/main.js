(function ($) {
    "use strict";

    // ===============================
    // WOW Animation
    // ===============================
    new WOW().init();


    // ===============================
    // Premium Navbar Scroll Effect
    // ===============================
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.premium-navbar').addClass('scrolled');
        } else {
            $('.premium-navbar').removeClass('scrolled');
        }
    });


    // ===============================
    // Dropdown Hover (Desktop only)
    // ===============================
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";

    $(window).on("load resize", function () {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
                function () {
                    const $this = $(this);
                    $this.addClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "true");
                    $this.find($dropdownMenu).addClass(showClass);
                },
                function () {
                    const $this = $(this);
                    $this.removeClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "false");
                    $this.find($dropdownMenu).removeClass(showClass);
                }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });


    // ===============================
    // Back to Top
    // ===============================
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // ===============================
    // PREMIUM HERO CAROUSEL
    // (IMPORTANT: Updated selector)
    // ===============================
    $(".premium-hero-carousel").owlCarousel({
        autoplay: true,
        autoplayTimeout: 5000,
        smartSpeed: 1200,
        items: 1,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // ===============================
    // Testimonials Carousel
    // ===============================
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: false,
        nav: false,
        responsive: {
            0: { items: 1 },
            768: { items: 1 },
            992: { items: 3 }
        }
    });

    var reviewCount = $(".testimonial-carousel .testimonial-item").length;

    if (reviewCount <= 2) {
        $(".testimonial-carousel").owlCarousel('destroy');
        $(".testimonial-carousel").addClass("d-flex justify-content-center gap-4");
    }


    // ===============================
// Premium Assets Auto Slider
// ===============================
document.addEventListener("DOMContentLoaded", function () {

    const slider = document.getElementById("assetsSlider");
    if (!slider) return;

    const items = slider.querySelectorAll(".asset-slide");
    const itemCount = items.length;

    // If few items → center only (no auto scroll)
    if (itemCount <= 3) {
        slider.classList.remove("many-items");
        return;
    }

    // Many items → enable left alignment + auto scroll
    slider.classList.add("many-items");

    let scrollAmount = 0;

    setInterval(() => {
        scrollAmount += 360;

        if (scrollAmount >= slider.scrollWidth - slider.clientWidth) {
            scrollAmount = 0;
        }

        slider.scrollTo({
            left: scrollAmount,
            behavior: "smooth"
        });

    }, 3500); // slide every 3.5 sec

});

// ===============================
// Premium Ads Alignment Control
// ===============================
document.addEventListener("DOMContentLoaded", function () {

    const adsSlider = document.querySelector(".premium-ads-slider");
    if (!adsSlider) return;

    const ads = adsSlider.querySelectorAll(".premium-ad-slide");
    const adCount = ads.length;

    // If more than 2 ads → enable left scroll
    if (adCount > 2) {
        adsSlider.classList.add("many-ads");
    }
});



    // ===============================
// Premium Batch Alignment Control
// ===============================
document.addEventListener("DOMContentLoaded", function () {

    const batchSlider = document.querySelector(".premium-batch-slider");
    if (!batchSlider) return;

    const items = batchSlider.querySelectorAll(".batch-slide");
    const count = items.length;

    if (count > 3) {
        batchSlider.classList.add("many-items");
    }

});


// ===============================
// Successful Batches Auto Slider
// ===============================
document.addEventListener("DOMContentLoaded", function () {

    const slider = document.getElementById("batchesSlider");
    if (!slider) return;

    const items = slider.querySelectorAll(".asset-slide");
    const itemCount = items.length;

    // Few items → center only
    if (itemCount <= 3) {
        slider.classList.remove("many-items");
        return;
    }

    // Many items → left align + auto scroll
    slider.classList.add("many-items");

    let scrollAmount = 0;

    setInterval(() => {
        scrollAmount += 360;

        if (scrollAmount >= slider.scrollWidth - slider.clientWidth) {
            scrollAmount = 0;
        }

        slider.scrollTo({
            left: scrollAmount,
            behavior: "smooth"
        });

    }, 3500);

});

/* ======================================
   Mobile Navbar – Perfect Behavior
   Open / Close / Outside Click
====================================== */

document.addEventListener("DOMContentLoaded", function () {

    const navbar = document.getElementById("navbarCollapse");
    const toggler = document.querySelector(".navbar-toggler");
    const navLinks = document.querySelectorAll("#navbarCollapse .nav-link");

    if (!navbar || !toggler) return;

    // Get Bootstrap instance or create one
    let bsCollapse = bootstrap.Collapse.getInstance(navbar);
    if (!bsCollapse) {
        bsCollapse = new bootstrap.Collapse(navbar, { toggle: false });
    }

    // Toggle on icon click
    toggler.addEventListener("click", function (e) {
        e.stopPropagation();
        bsCollapse.toggle();
    });

    // Close when menu item clicked
    navLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            if (window.innerWidth < 992) {
                bsCollapse.hide();
            }
        });
    });

    // Close when clicking outside
    document.addEventListener("click", function (e) {
        if (
            window.innerWidth < 992 &&
            navbar.classList.contains("show") &&
            !navbar.contains(e.target) &&
            !toggler.contains(e.target)
        ) {
            bsCollapse.hide();
        }
    });

});


})(jQuery);

/* ===== Force Mobile Tap Close Fix ===== */
document.addEventListener("touchstart", function (e) {
    const closeBtn = e.target.closest(".btn-close");
    if (!closeBtn) return;

    const modalEl = closeBtn.closest(".modal");
    if (!modalEl) return;

    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) {
        modal.hide();
    }
}, { passive: true });