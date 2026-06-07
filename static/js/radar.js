function showObjectInfo(element) {
    const name = element.dataset.name;
    const type = element.dataset.type;
    const altitude = element.dataset.altitude;
    const risk = element.dataset.risk;

    document.getElementById("info-name").innerText = name;
    document.getElementById("info-type").innerText =
        type === "satellite" ? "Satélite" : "Detrito";
    document.getElementById("info-altitude").innerText = altitude + " km";
    document.getElementById("info-risk").innerText = risk;

    document.querySelectorAll(".radar-object").forEach(obj => {
        obj.classList.remove("selected-object");
    });

    element.classList.add("selected-object");
}


function filterObjects(type) {
    const objects = document.querySelectorAll(".radar-object");

    objects.forEach(obj => {
        if (type === "all") {
            obj.style.display = "block";
        } else if (obj.classList.contains(type)) {
            obj.style.display = "block";
        } else {
            obj.style.display = "none";
        }
    });
}