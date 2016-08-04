class Node:
    def __init__(self, data):
        self.data = data
        self.links = []
        self.incident_edges = 0
        self.visited = False

    def add_link(self, node):
        node.incident_edges += 1
        self.links.append(node)

    def __repr__(self):
        return "(" + str(self.data) + "," + str([link.data for link in self.links]) + ")"

def generate_graph(adjacency_list):
    graph = {}
    for edge in adjacency_list:
        if edge[1] not in graph:
            graph[edge[1]] = Node(edge[1])
        if edge[0] not in graph:
            graph[edge[0]] = Node(edge[0])
        graph[edge[0]].add_link(graph[edge[1]])
    return graph

def get_start_nodes(graph):
    nodes = []
    for node in graph.values():
        if node.incident_edges == 0 and not node.visited:
            nodes.append(node)
    return nodes

def topological_sort(graph):
    sorted_list = []
    to_process = get_start_nodes(graph)
    while len(to_process) > 0:
        sorted_list += to_process
        for node in to_process:
            for linked in node.links:
                linked.incident_edges -= 1
            node.visited = True
        to_process = get_start_nodes(graph)
    return sorted_list

input_ = [(1,2),(1,3),(1,4),(3,5),(2,5),(4,5)]
print input_
graph = generate_graph(input_)
print graph
print topological_sort(graph)
