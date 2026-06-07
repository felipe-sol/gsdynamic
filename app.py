from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

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

        fuel = int(
            request.form["fuel"]
        )

        maneuvers = [

            (20, 50),   # custo, benefício

            (40, 80),

            (50, 120),

            (30, 70)

        ]

        result = optimize_fuel(
            fuel,
            maneuvers
        )

    return render_template(
        "mission_planner.html",
        result=result
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