document.addEventListener("DOMContentLoaded", () => {
    const bar = document.querySelector(".progress-bar");

    if (!bar) {
        return;
    }

    const width = bar.dataset.width || 0;

    setTimeout(() => {
        bar.style.width = width + "%";
    }, 200);
});