document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const toggleSidebar = document.getElementById("toggleSidebar");
    const mainContent = document.getElementById("mainContent");

    console.log("Script carregado");
    toggleSidebar.addEventListener("click", () => {
        console.log("Botão clicado");
        sidebar.classList.toggle("-translate-x-full");
        mainContent.classList.toggle("-ml-52");
        console.log("Classes da sidebar:", sidebar.classList);
    });
});