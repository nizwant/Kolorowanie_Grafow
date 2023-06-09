from networkx import Graph
from time import perf_counter


def wrapper(coloring_func, G: Graph, report=True):
    """
    A wrapper function for coloring algorithms.
    Returns a dictionary of colors for each node and the number of used colors.
    """

    timing_dict = {}
    timing_dict["start"] = perf_counter()
    coloring, number_of_color_used, timing_dict = coloring_func(G, timing_dict)
    timing_dict["stop"] = perf_counter()

    time = timing_dict["stop"] - timing_dict["start"]
    timing_list = timing_dict["coloring"]
    for i, t in enumerate(timing_list):
        timing_list[i][1] = t[1] - timing_dict["start"]
    timing_dict["coloring"] = timing_list

    if report:
        print(f"Time taken: {time:.3f}s, coloring function: {coloring_func.__name__}")
        print(f"color used: {number_of_color_used}, number of nodes: {len(G)}")
        print("")

    return coloring, number_of_color_used, time, timing_dict
