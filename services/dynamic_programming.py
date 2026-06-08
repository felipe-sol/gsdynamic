def optimize_mission(available_fuel):
    maneuvers = [
        {"name": "Remover DEBRIS-A", "fuel": 40, "benefit": 95, "risk": "Alto"},
        {"name": "Remover DEBRIS-B", "fuel": 35, "benefit": 80, "risk": "Alto"},
        {"name": "Desviar ISS de zona crítica", "fuel": 20, "benefit": 50, "risk": "Médio"},
        {"name": "Recalcular órbita STARLINK-1001", "fuel": 25, "benefit": 60, "risk": "Médio"},
        {"name": "Monitorar fragmentos em LEO", "fuel": 15, "benefit": 35, "risk": "Baixo"},
        {"name": "Atualizar rota segura via Dijkstra", "fuel": 10, "benefit": 25, "risk": "Baixo"}
    ]

    n = len(maneuvers)

    dp = [
        [0 for _ in range(available_fuel + 1)]
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):
        fuel = maneuvers[i - 1]["fuel"]
        benefit = maneuvers[i - 1]["benefit"]

        for capacity in range(available_fuel + 1):
            if fuel <= capacity:
                dp[i][capacity] = max(
                    dp[i - 1][capacity],
                    benefit + dp[i - 1][capacity - fuel]
                )
            else:
                dp[i][capacity] = dp[i - 1][capacity]

    selected = []
    capacity = available_fuel

    for i in range(n, 0, -1):
        if dp[i][capacity] != dp[i - 1][capacity]:
            maneuver = maneuvers[i - 1]
            selected.append(maneuver)
            capacity -= maneuver["fuel"]

    selected.reverse()

    selected_names = [
        item["name"]
        for item in selected
    ]

    discarded = [
        item for item in maneuvers
        if item["name"] not in selected_names
    ]

    fuel_used = sum(
        item["fuel"]
        for item in selected
    )

    remaining_fuel = available_fuel - fuel_used

    efficiency = round(
        dp[n][available_fuel] / fuel_used,
        2
    ) if fuel_used > 0 else 0

    return {
        "available_fuel": available_fuel,
        "max_benefit": dp[n][available_fuel],
        "fuel_used": fuel_used,
        "remaining_fuel": remaining_fuel,
        "efficiency": efficiency,
        "selected": selected,
        "discarded": discarded,
        "total_maneuvers": len(maneuvers)
    }