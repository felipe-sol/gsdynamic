import random

from services.data_service import get_objects


def run_monte_carlo(object_name, simulations=1000):
    objects = get_objects()

    selected = None

    for obj in objects:
        if obj["name"] == object_name:
            selected = obj
            break

    if not selected:
        return None

    collisions = 0
    samples = []

    base_risk = selected["risk"]

    for i in range(simulations):
        distance = random.uniform(0, 100)
        velocity_factor = random.uniform(0.7, 1.4)
        debris_density = random.uniform(0.5, 1.5)

        collision_score = (
            base_risk * velocity_factor * debris_density
        ) / max(distance, 1)

        collided = collision_score >= 1.2

        if collided:
            collisions += 1

        if i < 10:
            samples.append({
                "simulation": i + 1,
                "distance": round(distance, 2),
                "velocity_factor": round(velocity_factor, 2),
                "density": round(debris_density, 2),
                "collision_score": round(collision_score, 2),
                "result": "Colisão" if collided else "Seguro"
            })

    probability = round(
        (collisions / simulations) * 100,
        2
    )

    if probability >= 70:
        classification = "CRÍTICO"
    elif probability >= 40:
        classification = "ALTO"
    elif probability >= 20:
        classification = "MÉDIO"
    else:
        classification = "BAIXO"

    return {
        "object": selected,
        "simulations": simulations,
        "collisions": collisions,
        "probability": probability,
        "classification": classification,
        "samples": samples
    }