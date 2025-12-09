# Обнаружение цикла: O(V + E) по времени и O(V) по памяти
# Топологическая сортировка: O(V + E) по времени и O(V) по памяти

def detect_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(v):
        if v not in visited:
            visited.add(v)
            rec_stack.add(v)
            for neighbor in graph.get(v, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    cycle_path.append(neighbor)
                    cycle_path.append(v)
                    return True
            rec_stack.remove(v)
        return False

    for node in graph:
        cycle_path = []
        if dfs(node):
            return True, cycle_path
    return False, None

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        if v not in visited:
            visited.add(v)
            for neighbor in graph.get(v, []):
                dfs(neighbor)
            stack.append(v)

    for node in graph:
        dfs(node)

    return stack[::-1]
