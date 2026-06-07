from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import csv
import csv
from io import StringIO, BytesIO
from flask import Response, send_file
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment



from services.dynamic_programming import optimize_fuel
from services.data_service import get_objects
from services.graph_service import build_graph
from services.dijkstra_service import find_best_route
from services.montecarlo_service import collision_probability
from services.alert_service import get_alerts
from services.prediction_service import predict_collisions
from services.greedy_service import greedy_priority

app = Flask(__name__)


@app.route("/")
def dashboard():

    objects = get_objects()

    satellites = len(
        [o for o in objects
         if o["type"] == "satellite"]
    )

    debris = len(
        [o for o in objects
         if o["type"] == "debris"]
    )

    return render_template(
        "dashboard.html",
        satellites=satellites,
        debris=debris
    )

@app.route("/greedy")
def greedy():
    priorities = greedy_priority()

    return render_template(
        "greedy.html",
        priorities=priorities
    )

@app.route("/radar")
def radar():
    objects = get_objects()
    return render_template(
        "radar.html",
        objects=objects
    )

@app.route("/prediction")
def prediction():

    predictions = predict_collisions()

    return render_template(
        "prediction.html",
        predictions=predictions
    )

@app.route("/history")
def history():

    events = [

        "STARLINK-1001 realizou manobra evasiva.",

        "DEBRIS-A entrou em zona crítica.",

        "ISS alterou altitude orbital.",

        "Risco reduzido após correção orbital."

    ]

    return render_template(
        "history.html",
        events=events
    )

@app.route("/control-center")
def control_center():
    objects = get_objects()

    satellites = len([o for o in objects if o["type"] == "satellite"])
    debris = len([o for o in objects if o["type"] == "debris"])
    critical = len([o for o in objects if o["risk"] >= 70])

    return render_template(
        "control_center.html",
        satellites=satellites,
        debris=debris,
        critical=critical
    )

@app.route("/map")
def orbital_map():
    objects = get_objects()

    leo = len([o for o in objects if o["altitude"] <= 2000])
    meo = len([o for o in objects if 2000 < o["altitude"] <= 35786])
    geo = len([o for o in objects if o["altitude"] > 35786])

    return render_template(
        "map.html",
        objects=objects,
        leo=leo,
        meo=meo,
        geo=geo
    )

@app.route("/alerts")
def alerts():

    alerts = get_alerts()

    return render_template(
        "alerts.html",
        alerts=alerts
    )

@app.route("/tracking")
def tracking():

    objects = get_objects()

    search = request.args.get(
        "search",
        ""
    ).lower()

    obj_type = request.args.get(
        "type",
        ""
    )

    filtered = []

    for obj in objects:

        matches_search = (
            search in obj["name"].lower()
        )

        matches_type = (
            not obj_type
            or obj["type"] == obj_type
        )

        if matches_search and matches_type:

            filtered.append(obj)

    return render_template(
        "tracking.html",
        objects=filtered,
        total=len(filtered)
    )


@app.route("/graph")
def graph():

    graph = build_graph()

    nodes = list(graph.nodes())

    edges = list(graph.edges(data=True))

    return render_template(
        "graph.html",
        nodes=nodes,
        edges=edges
    )

@app.route("/analytics")
def analytics():

    objects = get_objects()

    satellites = len([
        obj for obj in objects
        if obj["type"] == "satellite"
    ])

    debris = len([
        obj for obj in objects
        if obj["type"] == "debris"
    ])

    names = [
        obj["name"]
        for obj in objects
    ]

    risks = [
        obj["risk"]
        for obj in objects
    ]

    leo = len([
        obj for obj in objects
        if obj["altitude"] <= 2000
    ])

    meo = len([
        obj for obj in objects
        if 2000 < obj["altitude"] <= 35786
    ])

    geo = len([
        obj for obj in objects
        if obj["altitude"] > 35786
    ])

    average_risk = round(
        sum(risks) / len(risks),
        2
    )

    return render_template(
        "analytics.html",
        satellites=satellites,
        debris=debris,
        names=names,
        risks=risks,
        leo=leo,
        meo=meo,
        geo=geo,
        average_risk=average_risk
    )

    return render_template(
        "analytics.html",
        average_risk=average_risk
    )

@app.route("/api/analytics")
def api_analytics():
    objects = get_objects()

    satellites = len([o for o in objects if o["type"] == "satellite"])
    debris = len([o for o in objects if o["type"] == "debris"])

    names = [o["name"] for o in objects]
    risks = [o["risk"] for o in objects]

    leo = len([o for o in objects if o["altitude"] <= 2000])
    meo = len([o for o in objects if 2000 < o["altitude"] <= 35786])
    geo = len([o for o in objects if o["altitude"] > 35786])

    return jsonify({
        "names": names,
        "risks": risks,
        "satellites": satellites,
        "debris": debris,
        "leo": leo,
        "meo": meo,
        "geo": geo
    })

@app.route("/collision")
def collision():

    probability = collision_probability()

    return render_template(
        "collision.html",
        probability=probability
    )

@app.route("/mission-planner", methods=["GET", "POST"])
def mission_planner():
    result = None

    if request.method == "POST":
        fuel = int(request.form["fuel"])

        maneuvers = [
            {
                "name": "Desviar ISS de zona crítica",
                "fuel": 20,
                "benefit": 50
            },
            {
                "name": "Remover DEBRIS-A",
                "fuel": 40,
                "benefit": 95
            },
            {
                "name": "Remover DEBRIS-B",
                "fuel": 35,
                "benefit": 80
            },
            {
                "name": "Recalcular órbita STARLINK-1001",
                "fuel": 25,
                "benefit": 60
            }
        ]

        result = optimize_fuel(fuel, maneuvers)

    return render_template(
        "mission_planner.html",
        result=result
    )

@app.route("/report")
def report():
    objects = get_objects()

    total = len(objects)

    satellites = len([
        o for o in objects
        if o["type"] == "satellite"
    ])

    debris = len([
        o for o in objects
        if o["type"] == "debris"
    ])

    average_risk = round(
        sum(o["risk"] for o in objects) / total,
        2
    )

    most_dangerous = max(
        objects,
        key=lambda o: o["risk"]
    )

    high_risk = [
        o for o in objects
        if o["risk"] >= 70
    ]

    leo = len([
        o for o in objects
        if o["altitude"] <= 2000
    ])

    meo = len([
        o for o in objects
        if 2000 < o["altitude"] <= 35786
    ])

    geo = len([
        o for o in objects
        if o["altitude"] > 35786
    ])

    recommendation = (
        f"Priorizar o monitoramento de {most_dangerous['name']}, "
        "pois apresenta o maior risco orbital."
        if most_dangerous["risk"] >= 70
        else "Cenário orbital dentro de níveis aceitáveis de segurança."
    )

    return render_template(
        "report.html",
        objects=objects,
        total=total,
        satellites=satellites,
        debris=debris,
        average_risk=average_risk,
        most_dangerous=most_dangerous,
        high_risk=high_risk,
        leo=leo,
        meo=meo,
        geo=geo,
        recommendation=recommendation
    )

@app.route("/report/export")
def export_report_csv():
    objects = get_objects()

    output = StringIO()
    writer = csv.writer(output)

    total = len(objects)
    satellites = len([o for o in objects if o["type"] == "satellite"])
    debris = len([o for o in objects if o["type"] == "debris"])
    average_risk = round(sum(o["risk"] for o in objects) / total, 2)
    high_risk = [o for o in objects if o["risk"] >= 70]
    most_dangerous = max(objects, key=lambda o: o["risk"])

    leo = len([o for o in objects if o["altitude"] <= 2000])
    meo = len([o for o in objects if 2000 < o["altitude"] <= 35786])
    geo = len([o for o in objects if o["altitude"] > 35786])

    writer.writerow(["ORBITALGUARD EXECUTIVE REPORT"])
    writer.writerow([])

    writer.writerow(["SYSTEM_INSIGHTS"])
    writer.writerow(["total_objects", total])
    writer.writerow(["total_satellites", satellites])
    writer.writerow(["total_debris", debris])
    writer.writerow(["average_risk", average_risk])
    writer.writerow(["high_risk_objects", len(high_risk)])
    writer.writerow(["leo_objects", leo])
    writer.writerow(["meo_objects", meo])
    writer.writerow(["geo_objects", geo])
    writer.writerow(["most_dangerous_object", most_dangerous["name"]])
    writer.writerow(["most_dangerous_risk", most_dangerous["risk"]])
    writer.writerow([])

    writer.writerow(["ALGORITHMS"])
    writer.writerow(["Dijkstra", "Caminho mínimo orbital"])
    writer.writerow(["Greedy", "Priorização de detritos"])
    writer.writerow(["Monte Carlo", "Simulação probabilística de colisão"])
    writer.writerow(["Dynamic Programming", "Otimização de combustível"])
    writer.writerow([])

    writer.writerow(["RECOMMENDATIONS"])
    if most_dangerous["risk"] >= 70:
        writer.writerow([
            f"Priorizar monitoramento/remoção de {most_dangerous['name']}"
        ])
    writer.writerow(["Executar simulações Monte Carlo periodicamente"])
    writer.writerow(["Reavaliar objetos em órbita LEO"])
    writer.writerow(["Usar Dijkstra para rotas orbitais seguras"])
    writer.writerow([])

    writer.writerow(["ORBITAL_OBJECTS"])
    writer.writerow([
        "id",
        "name",
        "type",
        "altitude_km",
        "risk",
        "risk_classification",
        "orbit_region",
        "recommendation"
    ])

    for obj in objects:
        risk = obj["risk"]
        altitude = obj["altitude"]

        if risk >= 70:
            risk_classification = "ALTO"
            recommendation = "Priorizar monitoramento/remocao"
        elif risk >= 40:
            risk_classification = "MEDIO"
            recommendation = "Monitorar com frequencia"
        else:
            risk_classification = "BAIXO"
            recommendation = "Monitoramento normal"

        if altitude <= 2000:
            orbit_region = "LEO"
        elif altitude <= 35786:
            orbit_region = "MEO"
        else:
            orbit_region = "GEO"

        writer.writerow([
            obj["id"],
            obj["name"],
            obj["type"],
            altitude,
            risk,
            risk_classification,
            orbit_region,
            recommendation
        ])

    response = Response(
        output.getvalue(),
        mimetype="text/csv"
    )

    response.headers["Content-Disposition"] = (
        "attachment; filename=orbitalguard_report.csv"
    )

    return response

@app.route("/report/export/excel")
def export_report_excel():
    objects = get_objects()

    total = len(objects)
    satellites = len([o for o in objects if o["type"] == "satellite"])
    debris = len([o for o in objects if o["type"] == "debris"])
    average_risk = round(sum(o["risk"] for o in objects) / total, 2)
    high_risk = [o for o in objects if o["risk"] >= 70]
    most_dangerous = max(objects, key=lambda o: o["risk"])

    leo = len([o for o in objects if o["altitude"] <= 2000])
    meo = len([o for o in objects if 2000 < o["altitude"] <= 35786])
    geo = len([o for o in objects if o["altitude"] > 35786])

    wb = Workbook()

    header_fill = PatternFill(
        start_color="00D4FF",
        end_color="00D4FF",
        fill_type="solid"
    )

    title_font = Font(
        bold=True,
        size=16
    )

    header_font = Font(
        bold=True,
        color="000000"
    )

    # DASHBOARD
    ws = wb.active
    ws.title = "Dashboard"

    ws["A1"] = "OrbitalGuard Executive Report"
    ws["A1"].font = title_font

    dashboard_data = [
        ["Indicador", "Valor"],
        ["Total de objetos", total],
        ["Satélites", satellites],
        ["Detritos", debris],
        ["Risco médio", average_risk],
        ["Objetos de alto risco", len(high_risk)],
        ["LEO", leo],
        ["MEO", meo],
        ["GEO", geo],
        ["Objeto mais perigoso", most_dangerous["name"]],
        ["Risco do objeto mais perigoso", most_dangerous["risk"]]
    ]

    for row in dashboard_data:
        ws.append(row)

    # OBJECTS
    ws2 = wb.create_sheet("Objects")

    headers = [
        "ID",
        "Nome",
        "Tipo",
        "Altitude km",
        "Risco",
        "Classificação",
        "Região orbital",
        "Recomendação"
    ]

    ws2.append(headers)

    for obj in objects:
        risk = obj["risk"]
        altitude = obj["altitude"]

        if risk >= 70:
            classification = "ALTO"
            recommendation = "Priorizar monitoramento/remocao"
        elif risk >= 40:
            classification = "MEDIO"
            recommendation = "Monitorar com frequencia"
        else:
            classification = "BAIXO"
            recommendation = "Monitoramento normal"

        if altitude <= 2000:
            orbit = "LEO"
        elif altitude <= 35786:
            orbit = "MEO"
        else:
            orbit = "GEO"

        ws2.append([
            obj["id"],
            obj["name"],
            obj["type"],
            altitude,
            risk,
            classification,
            orbit,
            recommendation
        ])

    # RISK ANALYSIS
    ws3 = wb.create_sheet("Risk Analysis")

    ws3.append(["Objeto", "Risco", "Classificação"])

    for obj in sorted(objects, key=lambda o: o["risk"], reverse=True):
        risk = obj["risk"]

        if risk >= 70:
            classification = "ALTO"
        elif risk >= 40:
            classification = "MEDIO"
        else:
            classification = "BAIXO"

        ws3.append([
            obj["name"],
            risk,
            classification
        ])

    # INSIGHTS
    ws4 = wb.create_sheet("Executive Insights")

    ws4.append(["Insight", "Descrição"])

    ws4.append([
        "Objeto mais perigoso",
        f"{most_dangerous['name']} com risco {most_dangerous['risk']}"
    ])

    ws4.append([
        "Recomendação principal",
        f"Priorizar monitoramento/remoção de {most_dangerous['name']}"
        if most_dangerous["risk"] >= 70
        else "Cenário orbital dentro de níveis aceitáveis"
    ])

    ws4.append([
        "Dijkstra",
        "Usado para calcular caminho mínimo orbital"
    ])

    ws4.append([
        "Guloso",
        "Usado para priorizar detritos de maior risco"
    ])

    ws4.append([
        "Monte Carlo",
        "Usado para simular probabilidade de colisão"
    ])

    ws4.append([
        "Programação Dinâmica",
        "Usada para otimizar combustível e manobras"
    ])

    for sheet in wb.worksheets:
        for cell in sheet[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center")

        for column_cells in sheet.columns:
            max_length = 0
            column = column_cells[0].column_letter

            for cell in column_cells:
                if cell.value:
                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )

            sheet.column_dimensions[column].width = max_length + 4

    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return send_file(
        file_stream,
        as_attachment=True,
        download_name="orbitalguard_report.xlsx",
        mimetype=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )

@app.route("/route")
def route():

    result = find_best_route(
        "ISS",
        "DEBRIS-A"
    )

    return render_template(
        "route.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)