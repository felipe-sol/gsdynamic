import json
import os

from services.api_service import get_celestrak_objects


def get_local_objects():
    current_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(current_dir)

    file_path = os.path.join(
        project_root,
        "data",
        "orbital_objects.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_objects():
    try:
        return get_celestrak_objects()
    except Exception:
        return get_local_objects()