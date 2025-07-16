grap = {
    "A" : ["B", "C"],
    "B" : ["D"],
    "C" : ["E"],
    "D" : [],
    "E" : {},
}
def dfs(grap, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in grap[node]:
        if neighbor not in visited:
            dfs(grap, neighbor, visited)
dfs(grap, "A")
