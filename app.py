from flask import Flask
from flask import render_template
from flask import request

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

    return render_template(
        "map.html",
        objects=objects
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

    return render_template(
        "tracking.html",
        objects=objects
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

    total_risk = sum(
        obj["risk"]
        for obj in objects
    )

    average_risk = round(
        total_risk / len(objects),
        2
    )

    return render_template(
        "analytics.html",
        average_risk=average_risk
    )

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