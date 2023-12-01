var current_copied = -1
window.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("copy1").addEventListener("click", function (e) {
        e.target.src = "static/checkmark.svg"
    }, false);
})