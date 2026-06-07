function updateClock() {
    const clock = document.getElementById("clock");

    if (!clock) {
        return;
    }

    const now = new Date();

    clock.innerText = now.toLocaleTimeString("pt-BR");
}

setInterval(updateClock, 1000);
updateClock();


document.querySelectorAll(".menu a").forEach(link => {
    if (link.href === window.location.href) {
        link.style.background = "#13244a";
        link.style.color = "#00d4ff";
    }
});