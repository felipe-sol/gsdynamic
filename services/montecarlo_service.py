import random


def collision_probability(simulations=1000):

    collisions = 0

    for _ in range(simulations):

        satellite_position = random.randint(1, 1000)

        debris_position = random.randint(1, 1000)

        if abs(satellite_position - debris_position) <= 10:

            collisions += 1

    probability = (
        collisions / simulations
    ) * 100

    return round(probability, 2)