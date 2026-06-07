import random

from services.data_service import get_objects


def predict_collisions():

    objects = get_objects()

    predictions = []

    for obj in objects:

        risk = obj["risk"]

        probability = round(
            random.uniform(
                risk * 0.5,
                risk * 1.2
            ),
            2
        )

        predictions.append({

            "name": obj["name"],

            "type": obj["type"],

            "risk": probability

        })

    return predictions