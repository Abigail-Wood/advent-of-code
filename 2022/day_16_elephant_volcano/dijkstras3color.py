#!/usr/bin/env python3

# Define a node object class.
class Node:
    def __init__ (self, name, edges):
        self.name = name
        self.edges = edges
        self.previous_node = ''
        self.current_min_path = None

def initialise_sets(nodes_dict):
    # Make a set of start node(s). Call this the 'grey' set.
    # This implementation uses an ordered dictionary and assumes the first node is the start (visited) node.
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

# Perform dikjstra's 3 color algorithm on set of node objects.
def apply_djikstras(nodes_dict, grey_set, white_set, black_set):
    current_node = None
    # While there are still frontier nodes, keep applying djikstras.
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

# Parse input into individual instantiated node objects.
nodes_dict = {}
with open("dummy_djisktra_input.txt", 'r') as f:
    # Line is of form "A,B;C;D;F,1"
    for line in list(f):
        node_facts = line.strip().split(',')
        node_name = node_facts[0]
        if (';' in node_facts[1]):
            edge_names = node_facts[1].split(';')
        else:
            edge_names = list(node_facts[1])
        
        if (';' in node_facts[2]):
            weights = [int(weight) for weight in node_facts[2].split(';')]
        else:
            weights = [int(weight) for weight in node_facts[2]]
        
        edges = {edge_names[i]: weights[i] for i in range(len(edge_names))}
        nodes_dict[node_name] = Node(node_name, edges)

    grey_set, white_set, black_set = initialise_sets(nodes_dict)
    final_nodes_dict = apply_djikstras(nodes_dict, grey_set, white_set, black_set)
    [print(node, final_nodes_dict[node].current_min_path, final_nodes_dict[node].previous_node) for node in final_nodes_dict]