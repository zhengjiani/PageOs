graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['A', 'C', 'E']
}
def dfs_traverse(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        visited.add(node)
        for nextNode in graph[node]:
            if nextNode not in visited:
                stack.append(nextNode)
    return visited


print(dfs_traverse(graph, 'A'))


def dfs_traverse_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nextNode in graph[start]:
        if nextNode not in visited:
            dfs_traverse_recursive(graph, nextNode, visited)
    return visited


print(dfs_traverse_recursive(graph, 'A'))
