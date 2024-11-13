document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const toggleSidebar = document.getElementById("toggleSidebar");

    toogleSidebar.addEventListener("click", () => {
        sidebar.classList.toggle("-translate-x-full");
    });
});