document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const toggleSidebar = document.getElementById("toggleSidebar");
    const mainContent = document.getElementById("mainContent");
    const navbarContent = document.getElementById("navbarContent");
    const mobileNavbar = document.getElementById("mobileNavbar");

    //  define o breakpoints para mobile
    const isMobile = () => window.innerWidth < 1024;

    toggleSidebar.addEventListener("click", () => {
        if (isMobile()) {
            sidebar.classList.toggle("open");
        } else {
            sidebar.classList.toggle("-translate-x-full");
            mainContent.classList.toggle("-ml-64");
            mobileNavbar.classList.toggle("hidden");
        }
    });
    
    //  Recalcular ao redimensionar a tela:
    // window.addEventListener("resize", () => {
    //     if (!isMobile()) {
    //         sidebar.classList.remove("open");
    //         sidebar.classList.add("-translate-x-full");
    //         mainContent.classList.toggle("-ml-64");
    //         mobileNavbar.classList.toggle("hidden");
    //     } else {
    //         sidebar.classList.remove("-translate-x-full");
    //         mainContent.style.marginLeft = "0";
    //     }
    // });

});