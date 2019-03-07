import math
from collections import defaultdict


class Edge:

    def __init__(self, weight, node):
        self.weight = weight
        self.node = node

class Node:

    def __init__(self, alias):
        self.alias = alias
        self.neighbour_edges = []

    def add_neighbour_node(self, weight, node):
        edge = Edge(weight, node)
        self.neighbour_edges.append(edge)
        
    def all_nodes(self):
        nodes = [self]
        for edge in self.neighbour_edges:
            nodes += edge.node.all_nodes()
        return set(nodes)

    def update_neighbour_nodes(self, costs_by_alias, parents_by_alias):
        own_cost = costs_by_alias[self.alias]
        for edge in self.neighbour_edges:
            new_weight = own_cost + edge.weight
            if costs_by_alias[edge.node.alias] > new_weight:
                costs_by_alias[edge.node.alias] = new_weight
                parents_by_alias[edge.node.alias] = self.alias

    @staticmethod
    def find_cheapest_node_alias(costs_by_alias, processed_nodes_by_alias):
        lowest_cost = math.inf
        lowest_cost_node_alias = None

        for node_alias, cost in costs_by_alias.items():
            if cost < lowest_cost and not processed_nodes_by_alias[node_alias]:
                lowest_cost = cost
                lowest_cost_node_alias = node_alias

        return lowest_cost_node_alias

    def shortest_path_to_child_node(self, node):
        all_nodes_by_alias = {node.alias: node for node in self.all_nodes()}
        processed_nodes_by_alias = defaultdict(lambda: False)
        costs_by_alias = defaultdict(lambda: math.inf)
        costs_by_alias[self.alias] = 0 # no costs to self
        parents_by_alias = defaultdict(lambda: None)

        current_node = self
        while True:
            processed_nodes_by_alias[current_node.alias] = True
            current_node.update_neighbour_nodes(costs_by_alias, parents_by_alias)
            cheapest_node_alias = Node.find_cheapest_node_alias(costs_by_alias, processed_nodes_by_alias)
            if not cheapest_node_alias:
                return parents_by_alias
            current_node = all_nodes_by_alias[cheapest_node_alias]
            if not current_node:
                return parents_by_alias


if __name__ == "__main__":
    # Create nodes
    book = Node("book")
    rare_lp = Node("rare lp")
    poster = Node("poster")
    bass_guitar = Node("bass guitar")
    drum_set = Node("drum set")
    piano = Node("piano")

    # Set up relations
    book.add_neighbour_node(5, rare_lp)
    book.add_neighbour_node(0, poster)

    rare_lp.add_neighbour_node(15, bass_guitar)
    rare_lp.add_neighbour_node(20, drum_set)

    poster.add_neighbour_node(30, bass_guitar)
    poster.add_neighbour_node(35, drum_set)

    bass_guitar.add_neighbour_node(20, piano)
    drum_set.add_neighbour_node(10, piano)

    print(book.shortest_path_to_child_node(piano))
