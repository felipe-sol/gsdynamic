import networkx as nx

from services.graph_service import build_graph


def find_best_route(start, end):

    graph = build_graph()

    try:

        path = nx.dijkstra_path(
            graph,
            start,
            end,
            weight="weight"
        )

        distance = nx.dijkstra_path_length(
            graph,
            start,
            end,
            weight="weight"
        )

        return {
            "path": path,
            "distance": distance
        }

    except:

        return None