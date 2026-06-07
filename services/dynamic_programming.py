def optimize_fuel(
    available_fuel,
    maneuvers
):

    dp = [0] * (available_fuel + 1)

    for fuel_cost, benefit in maneuvers:

        for f in range(
            available_fuel,
            fuel_cost - 1,
            -1
        ):

            dp[f] = max(
                dp[f],
                dp[f - fuel_cost] + benefit
            )

    return dp[available_fuel]