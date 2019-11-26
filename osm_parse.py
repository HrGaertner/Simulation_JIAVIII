"""This file parses osm: for now it is just creating an easy network."""

import networkx as nx

def create_streetnetwork():
    streets = nx.Graph()

    # Add all nodes and edges

    streets.add_node("A")  # These blocks are creating the Nodes
    streets.add_node("B")
    streets.add_node("C")
    streets.add_node("D")
    streets.add_node("E")
    streets.add_node("F")

    streets.add_edge("A", "B", max_v = 50/3.6, length = 3.0, cars = {'A':[], 'B':[]})  #max_v in km/h Here the Nodes are connected and list for cars are initialized
    streets.add_edge("B", "C", max_v = 50/3.6, length = 14.0, cars = {'B':[], 'C':[]})
    streets.add_edge("B", "E", max_v = 50/3.6, length = 4.0, cars = {'B':[], 'E':[]})
    streets.add_edge("C", "D", max_v = 50/3.6, length = 11.0, cars = {'C':[], 'D':[]})
    streets.add_edge("D", "E", max_v = 50/3.6, length = 13.0, cars = {'D':[], 'E':[]})
    streets.add_edge("E", "F", max_v = 50/3.6, length = 7.0, cars = {'E':[], 'F':[]})  # A car driving from E to F will be placed in 'F'
    streets.add_edge("F", "A", max_v = 50/3.6, length = 9.0, cars = {'F':[], 'A':[]})

    nx.draw(streets, with_labels=True, font_weight='bold')  # Visiualize streets
    return streets
