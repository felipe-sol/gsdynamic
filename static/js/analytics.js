document.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/api/analytics");
    const data = await response.json();

    new Chart(document.getElementById("riskChart"), {
        type: "bar",
        data: {
            labels: data.names,
            datasets: [{
                label: "Nível de risco",
                data: data.risks
            }]
        }
    });

    new Chart(document.getElementById("typeChart"), {
        type: "doughnut",
        data: {
            labels: ["Satélites", "Detritos"],
            datasets: [{
                data: [data.satellites, data.debris]
            }]
        }
    });

    new Chart(document.getElementById("orbitChart"), {
        type: "pie",
        data: {
            labels: ["LEO", "MEO", "GEO"],
            datasets: [{
                data: [data.leo, data.meo, data.geo]
            }]
        }
    });
});