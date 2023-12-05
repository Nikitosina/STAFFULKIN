let defaultIcon = "http://localhost:8080/static/resources/copy.svg"
let checkmarkIcon = "http://localhost:8080/static/resources/checkmark.svg"
var current_copied = -1

function resetPasteIcons() {
    document.getElementById("copyEmail").src = defaultIcon
    document.getElementById("copyPhone").src = defaultIcon
    document.getElementById("copyMessenger").src = defaultIcon
}

window.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("copyEmail").addEventListener("click", function (e) {
        setTextInPasteboard("email")
        resetPasteIcons()
        e.target.src = checkmarkIcon
    }, false);
    document.getElementById("copyPhone").addEventListener("click", function (e) {
        setTextInPasteboard("phone")
        resetPasteIcons()
        e.target.src = checkmarkIcon
    }, false);
    document.getElementById("copyMessenger").addEventListener("click", function (e) {
        setTextInPasteboard("messenger")
        resetPasteIcons()
        e.target.src = checkmarkIcon
    }, false);
})