import networkx as nx

from services.data_service import get_objects


def build_graph():

    objects = get_objects()

    G = nx.Graph()

    for obj in objects:

        G.add_node(
            obj["name"],
            type=obj["type"],
            altitude=obj["altitude"]
        )

    for i in range(len(objects)):

        for j in range(i + 1, len(objects)):

            alt1 = objects[i]["altitude"]
            alt2 = objects[j]["altitude"]

            distance = abs(alt1 - alt2)

            if distance <= 100:

                G.add_edge(
                    objects[i]["name"],
                    objects[j]["name"],
                    weight=distance
                )

    return G