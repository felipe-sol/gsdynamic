from services.data_service import get_objects


def get_alerts():

    alerts = []

    objects = get_objects()

    for obj in objects:

        if obj["risk"] >= 70:

            alerts.append(
                f"⚠ {obj['name']} possui alto risco orbital."
            )

    return alerts