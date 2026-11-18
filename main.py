
from collections import deque


def label(node):
    """Show O1 / O2 as plain 'O'."""
    return node[0]


# ---------------- BINARY TREE ----------------
# Each node maps to its [left, right] children.
tree = {
    "B": ["A", "R"],
    "A": ["C", "O1"],
    "R": ["S", "O2"],
    "C": [], "O1": [], "S": [], "O2": [],
}


def tree_bfs(root):
    """Breadth-First Search: visit level by level using a queue."""
    order, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        queue.extend(tree[node])          # left child, then right child
    return order


def tree_dfs(node, order=None):
    """Depth-First Search (preorder): root, left subtree, right subtree."""
    if order is None:
        order = []
    order.append(node)
    for child in tree[node]:
        tree_dfs(child, order)
    return order


# ---------------- GRAPH ----------------
# Adjacency list: each vertex maps to its neighbors (left to right).
graph = {
    "B":  ["A", "R", "C"],
    "A":  ["B", "O1", "S"],
    "R":  ["B", "S", "C"],
    "C":  ["B", "R", "O2"],
    "O1": ["A"],
    "S":  ["A", "R"],
    "O2": ["C"],
}


def graph_bfs(start):
    """BFS: visit all neighbors first, using a queue and a visited set."""
    visited, order, queue = {start}, [], deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return order


def graph_dfs(v, visited=None, order=None):
    """DFS: go as deep as possible, then backtrack."""
    if visited is None:
        visited, order = set(), []
    visited.add(v)
    order.append(v)
    for n in graph[v]:
        if n not in visited:
            graph_dfs(n, visited, order)
    return order


def show(title, nodes):
    print(f"{title:<14}", " - ".join(label(n) for n in nodes))


if __name__ == "__main__":
    print("Last name: BARCOSO\n")
    print("BINARY TREE")
    show("BFS:", tree_bfs("B"))
    show("DFS (preorder):", tree_dfs("B"))
    print("\nGRAPH")
    show("BFS:", graph_bfs("B"))
    show("DFS:", graph_dfs("B"))