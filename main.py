# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Graph:
    def __init__(self):
        self.adjacency_list={}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node]=[]

    def add_edge(self, from_node, to_node, capacity):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_list[from_node].append((to_node, capacity))

    def get_neighbours(self, node):
        return self.adjacency_list.get(node, [])

    def __str__(self):
        return str(self.adjacency_list)


def dfs(graph, current_node, target_node, path_flow, flow_graph, visited=None):
    if visited is None:
        visited = set()

    if current_node == target_node:
        return path_flow
    visited.add(current_node)

    for neighbor, capacity in graph.get_neighbours(current_node):
        if neighbor not in flow_graph[current_node]:
            flow_graph[current_node][neighbor] = 0
        if current_node not in flow_graph[neighbor]:
            flow_graph[neighbor][current_node] = 0

        residual_capacity = capacity - flow_graph[current_node][neighbor]
        if neighbor not in visited and residual_capacity > 0:
            min_capacity = min(path_flow, residual_capacity)
            result = dfs(graph, neighbor, target_node, min_capacity, flow_graph, visited)
            if result > 0:
                flow_graph[current_node][neighbor] += result
                flow_graph[neighbor][current_node] -= result
                return result
    return 0

def ford_fulkerson(graph, source, sink):
    flow_graph = {node: {} for node in graph.adjacency_list}
    for u in graph.adjacency_list:
        for v, _ in graph.adjacency_list[u]:
            flow_graph[u][v] = 0

    max_flow = 0

    while True:
        path_flow = dfs(graph, source, sink, float('Inf'), flow_graph, visited=set())
        if path_flow == 0:
            break
        max_flow += path_flow

    return max_flow
def initialize_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            entry = line.split(" ")
            from_city = entry[0]
            to_city = entry[1]
            capacity = int(entry[2])

            graph.add_edge(from_city,to_city,capacity)
    return graph



def main():
    graph = initialize_graph("canadian_cities.txt")
    print(ford_fulkerson(graph, "Argentia", "Inuvik"))

main()