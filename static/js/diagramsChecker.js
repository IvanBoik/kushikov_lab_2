const status = sessionStorage.getItem("status")

if (status !== "Выполнено") {
    document.getElementById("diagram-image").style.visibility = "hidden"
    document.getElementById("diagram2-image").style.visibility = "hidden"
    document.getElementById("diagram3-image").style.visibility = "hidden"
    document.getElementById("diagram4-image").style.visibility = "hidden"
    document.getElementById("diagram5-image").style.visibility = "hidden"
}
else {
    document.getElementById("diagram-image").style.visibility = "visible"
    document.getElementById("diagram2-image").style.visibility = "visible"
    document.getElementById("diagram3-image").style.visibility = "visible"
    document.getElementById("diagram4-image").style.visibility = "visible"
    document.getElementById("diagram5-image").style.visibility = "visible"
}