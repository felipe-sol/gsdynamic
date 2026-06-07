import random
import requests


CELESTRAK_URL = (
    "https://celestrak.org/NORAD/elements/gp.php"
    "?GROUP=active&FORMAT=tle"
)


def get_celestrak_objects(limit=8):
    response = requests.get(CELESTRAK_URL, timeout=8)
    response.raise_for_status()

    lines = response.text.strip().splitlines()
    objects = []

    for i in range(0, len(lines), 3):
        if i + 2 >= len(lines):
            continue

        name = lines[i].strip()
        tle_line_1 = lines[i + 1].strip()

        try:
            norad_id = int(tle_line_1[2:7])
        except ValueError:
            norad_id = random.randint(10000, 99999)

        obj_type = "satellite"

        objects.append({
            "id": norad_id,
            "name": name,
            "type": obj_type,
            "altitude": random.randint(350, 1200),
            "risk": random.randint(10, 60)
        })

        if len(objects) >= limit:
            break

    objects.append({
        "id": 90001,
        "name": "DEBRIS-A",
        "type": "debris",
        "altitude": 545,
        "risk": 80
    })

    objects.append({
        "id": 90002,
        "name": "DEBRIS-B",
        "type": "debris",
        "altitude": 600,
        "risk": 65
    })

    return objects