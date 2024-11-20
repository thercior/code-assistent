document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const toggleSidebar = document.getElementById("toggleSidebar");
    const mainContent = document.getElementById("mainContent");
    const navbarContent = document.getElementById("navbarContent");
    const mobileNavbar = document.getElementById("mobileNavbar");

    toggleSidebar.addEventListener("click", () => {
        sidebar.classList.toggle("-translate-x-full");
        mainContent.classList.toggle("-ml-64");
        mobileNavbar.classList.toggle("hidden");
    });

});