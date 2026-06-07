function openTrackingDetails(name, type, altitude, risk) {
    const panel = document.getElementById("trackingDetails");

    const riskNumber = Number(risk);

    document.getElementById("detailName").innerText = name;

    document.getElementById("detailType").innerText =
        type === "satellite" ? "Satélite" : "Detrito";

    document.getElementById("detailAltitude").innerText =
        altitude + " km";

    document.getElementById("detailRisk").innerText =
        risk;

    document.getElementById("detailIcon").innerText =
        type === "satellite" ? "🛰" : "☄";

    const riskBox = document.getElementById("detailRiskBox");
    const actions = document.getElementById("detailActions");

    riskBox.className = "detail-risk-box";

    if (riskNumber >= 70) {
        riskBox.innerText = "RISCO CRÍTICO";
        riskBox.classList.add("detail-danger");

        actions.innerHTML = `
            <li>Executar simulação Monte Carlo imediatamente.</li>
            <li>Priorizar no algoritmo guloso.</li>
            <li>Incluir no relatório executivo.</li>
        `;
    } else if (riskNumber >= 40) {
        riskBox.innerText = "RISCO MODERADO";
        riskBox.classList.add("detail-warning");

        actions.innerHTML = `
            <li>Manter monitoramento frequente.</li>
            <li>Reavaliar trajetória orbital.</li>
            <li>Comparar com objetos próximos no grafo.</li>
        `;
    } else {
        riskBox.innerText = "RISCO BAIXO";
        riskBox.classList.add("detail-safe");

        actions.innerHTML = `
            <li>Monitoramento padrão.</li>
            <li>Registrar no histórico operacional.</li>
        `;
    }

    panel.classList.add("active");
}


function closeTrackingDetails() {
    const panel = document.getElementById("trackingDetails");

    panel.classList.remove("active");
}