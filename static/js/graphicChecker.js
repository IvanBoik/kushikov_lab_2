const status = sessionStorage.getItem("status")
const element = document.getElementById("graphic-image")

if (status !== "Выполнено") {
    element.style.visibility = "hidden"
}
else {
    element.style.visibility = "visible"
}