#!/usr/bin/env python3

import re

# Define a node object class.
class Node:
    def __init__ (self, name, edges):
        self.name = name
        self.edges = edges
        self.previous_node = ''
        self.current_min_path = None

def initialise_sets(nodes_dict):
    # Make a set of start node(s). Call this the 'grey' set. Assume the first node is the start (visited) node.
    node_names = iter(nodes_dict.keys())
    grey_set = set(next(node_names))
    # Initialise the starting grey set node current min path to 0.
    for node in grey_set:
        nodes_dict[node].current_min_path = 0
    # Create a set of unvisited nodes (the default initialisation of node). Call this the 'white' set.
    white_set = set(node_names)
    # Create an empty set of completed nodes. Call this the 'black' set.
    black_set = set()
    return grey_set, white_set, black_set

# Perform dijkstra's 3 color algorithm on set of node objects.
def apply_dijkstras(nodes_dict, grey_set, white_set, black_set):
    current_node = None
    # While there are still frontier nodes, keep applying dijkstras.
    while grey_set:
        # Choose to evaluate the node with lowest current_min_path of the frontier nodes.
        current_node = min(grey_set, key=lambda x: nodes_dict[x].current_min_path)
        for edge in nodes_dict[current_node].edges:
            if edge in white_set:
                nodes_dict[edge].current_min_path = nodes_dict[edge].edges[current_node] + nodes_dict[current_node].current_min_path
                nodes_dict[edge].previous_node = current_node
                grey_set.add(edge)
                white_set.remove(edge)
            elif edge in grey_set:
                # Compare visited node current_min_path with current node's route to it. If the new route is better, use it!
                if nodes_dict[edge].current_min_path > (nodes_dict[edge].edges[current_node] + nodes_dict[current_node].current_min_path):
                    nodes_dict[edge].current_min_path = nodes_dict[edge].edges[current_node] + nodes_dict[current_node].current_min_path
                    nodes_dict[edge].previous_node = current_node
            # Ignore black set nodes.
        grey_set.remove(current_node)
        black_set.add(current_node)
    return nodes_dict

def run_time(t, nodes_dict, start):
    # Initialise start node as current node and total flow rate.
    current_node = nodes_dict[start]
    total_flow_rate = 0
    while t != 0:
        # Find node with the best remaining flow rate in the graph.
        # That will be (time minus cost to open valve minus minimum_path) times the remaining flow available.
        # (t - 1 - minimum_path) * flow
        current_node = max(nodes_dict.keys(), key=lambda x: (t - 1 - nodes_dict[x].current_min_path) * nodes_dict[x].flow)
        # Add the computed value in previous step to total flow rate acquired
        total_flow_rate = (t - 1 - nodes_dict[current_node].current_min_path) * nodes_dict[current_node].flow
        # Set current node flow rate to 0 (no further rate can be extracted).
        current_node.flow = 0
        # Update t
        t = t - 1 - nodes_dict[current_node].current_min_path
    return total_flow_rate

# Parse input into individual instantiated node objects.
nodes_dict = {}
with open("dummy_input.txt", 'r') as f:
    # Line is of form "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    for line in list(f):
        line_halved = line.strip().split(';')
        first_half_split = line_halved[0].split()
        node_name = first_half_split[1]
        flow_rate = int(first_half_split[4].split('=')[1])
        second_half_after_valve = re.split('valve |valves ', line_halved[1])
        edge_names = second_half_after_valve[1].split(', ')
        edges = {edge_names[i]: 1 for i in range(len(edge_names))}
        nodes_dict[node_name] = Node(node_name, edges, flow_rate)

    grey_set, white_set, black_set = initialise_sets(nodes_dict)
    final_nodes_dict = apply_dijkstras(nodes_dict, grey_set, white_set, black_set)
    [print(node, final_nodes_dict[node].current_min_path, final_nodes_dict[node].previous_node) for node in final_nodes_dict]
    
    # There is a missing piece connecting the opening min path dictionary to evolving directory.
    # Q: do I need to update min paths every time a node goes to 0?
    run_time(30, final_nodes_dict, 'AA')

    # Add cul-de-sac rules in as well (if linear graph all fixed.)
    # Traveling salesperson problem variant.
