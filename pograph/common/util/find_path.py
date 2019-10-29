myGraph = {'A': ['B', 'C'],
           'B': ['C', 'D'],
           'C': ['D', 'F'],
           'D': ['C'],
           'E': ['F'],
           'F': ['C']}
#使用带有回溯的递归查找从开始到结束的路径
def find_path(graph,start,end,path=[]):
    path = path + [start]
    if (start == end):
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
            return newpath
    return None
#寻找所有路径
def find_all_path(graph,start,end,path=[]):
    path = path + [start]
    print(path)
    if (start == end):
        return [path]
    if not start in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
print(find_all_path(myGraph,'A','F'))
def bfs_traverse(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
    return visited