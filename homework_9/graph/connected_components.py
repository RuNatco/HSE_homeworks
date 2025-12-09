# Сложность: O(V + E) по времени и O(V) по памяти из-за хранения visited узлов

def find_connected_components(graph):
    visited = set()
    components = []

    def bfs(start):
        queue = [start]
        component = []
        visited.add(start)
        while queue:
            node = queue.pop(0)
            component.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return component

    for node in graph:
        if node not in visited:
            component = bfs(node)
            components.append(component)

    isolated_nodes = set(graph.keys()).difference(visited)
    for node in isolated_nodes:
        components.append([node])

    return components
