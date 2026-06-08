from services.data_service import get_objects


def classify_risk(risk):
    if risk >= 70:
        return "ALTO"
    elif risk >= 40:
        return "MÉDIO"
    return "BAIXO"


def greedy_priority():
    objects = get_objects()

    debris = [
        obj for obj in objects
        if obj["type"] == "debris"
    ]

    priorities = []

    for obj in debris:
        altitude_factor = 1

        if obj["altitude"] <= 2000:
            altitude_factor = 1.5
        elif obj["altitude"] <= 35786:
            altitude_factor = 1.2

        priority_score = round(
            obj["risk"] * altitude_factor,
            2
        )

        priorities.append({
            "id": obj["id"],
            "name": obj["name"],
            "type": obj["type"],
            "altitude": obj["altitude"],
            "risk": obj["risk"],
            "risk_classification": classify_risk(obj["risk"]),
            "priority_score": priority_score,
            "reason": (
                "Detrito em LEO com alto impacto operacional"
                if obj["altitude"] <= 2000
                else "Detrito relevante para monitoramento orbital"
            )
        })

    priorities.sort(
        key=lambda obj: obj["priority_score"],
        reverse=True
    )

    return priorities