def optimize_fuel(available_fuel, maneuvers):
    n = len(maneuvers)

    dp = [
        [0] * (available_fuel + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):
        fuel_cost = maneuvers[i - 1]["fuel"]
        benefit = maneuvers[i - 1]["benefit"]

        for f in range(available_fuel + 1):
            if fuel_cost <= f:
                dp[i][f] = max(
                    dp[i - 1][f],
                    dp[i - 1][f - fuel_cost] + benefit
                )
            else:
                dp[i][f] = dp[i - 1][f]

    selected = []
    f = available_fuel

    for i in range(n, 0, -1):
        if dp[i][f] != dp[i - 1][f]:
            maneuver = maneuvers[i - 1]
            selected.append(maneuver)
            f -= maneuver["fuel"]

    fuel_used = sum(item["fuel"] for item in selected)

    return {
        "max_benefit": dp[n][available_fuel],
        "fuel_used": fuel_used,
        "selected": selected
    }