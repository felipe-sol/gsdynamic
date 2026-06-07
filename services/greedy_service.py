from services.data_service import get_objects


def greedy_priority():
    objects = get_objects()

    debris = [
        obj for obj in objects
        if obj["type"] == "debris"
    ]

    ordered = sorted(
        debris,
        key=lambda obj: obj["risk"],
        reverse=True
    )

    return ordered