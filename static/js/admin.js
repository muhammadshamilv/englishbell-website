document.addEventListener("DOMContentLoaded", function () {

    // ===============================
    // IMPORTANT:
    // Let Django handle login/logout/session
    // So DO NOT block form submission
    // ===============================

});


/* ===============================
   SHOW / HIDE PASSWORD
=============================== */
function togglePassword(id, icon) {
    const input = document.getElementById(id);

    if (input.type === "password") {
        input.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
    } else {
        input.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
}


/* ===============================
   SIDEBAR TOGGLE (Mobile)
=============================== */
function toggleSidebar() {
    const sidebar = document.getElementById("adminSidebar");
    if (!sidebar) return;

    sidebar.classList.toggle("active");

    if (sidebar.classList.contains("active")) {
        document.body.style.overflow = "hidden";
    } else {
        document.body.style.overflow = "";
    }
}

// Asset Preview Popup
document.addEventListener("click", function(e) {
    const preview = e.target.closest(".asset-click");
    if (!preview) return;

    const type = preview.getAttribute("data-type");
    const src = preview.getAttribute("data-src");

    const modal = document.getElementById("assetModal");
    const content = document.getElementById("assetModalContent");

    if (type === "image") {
        content.innerHTML = `<img src="${src}">`;
    } else {
        content.innerHTML = `
            <video controls autoplay>
                <source src="${src}">
            </video>
        `;
    }

    modal.style.display = "flex";
});

function closeAssetModal() {
    const modal = document.getElementById("assetModal");
    const content = document.getElementById("assetModalContent");

    modal.style.display = "none";
    content.innerHTML = "";
}

// Close on background click
document.getElementById("assetModal")?.addEventListener("click", function(e) {
    if (e.target.id === "assetModal") {
        closeAssetModal();
    }
});

/* ===============================
   MOBILE SIDEBAR – OUTSIDE CLICK CLOSE
=============================== */

document.addEventListener("click", function (e) {

    const sidebar = document.getElementById("adminSidebar");
    const toggleBtn = document.querySelector(".menu-toggle");

    if (!sidebar || window.innerWidth > 768) return;

    const isSidebarOpen = sidebar.classList.contains("active");
    const clickedInsideSidebar = sidebar.contains(e.target);
    const clickedToggle = toggleBtn && toggleBtn.contains(e.target);

    // If sidebar open and clicked outside → close
    if (isSidebarOpen && !clickedInsideSidebar && !clickedToggle) {
        sidebar.classList.remove("active");
    }

});