"""GD-9: Locations graph. DFS using adjacency matrix, BFS using adjacency list."""
from collections import deque

n = int(input("Number of locations: "))
labels = input(f"Enter {n} location names (space separated, e.g. A B C D): ").split()
idx = {name: i for i, name in enumerate(labels)}

matrix = [[0] * n for _ in range(n)]
adj_list = {name: [] for name in labels}

print("Enter routes as 'A B' (blank line to finish):")
while True:
    line = input().split()
    if len(line) != 2:
        break
    u, v = line
    if u in idx and v in idx:
        matrix[idx[u]][idx[v]] = matrix[idx[v]][idx[u]] = 1
        adj_list[u].append(v)
        adj_list[v].append(u)
    else:
        print("Unknown location.")

print("\nAdjacency Matrix:")
print("   " + " ".join(labels))
for i, row in enumerate(matrix):
    print(f"{labels[i]}  " + " ".join(map(str, row)))
print("\nAdjacency List:")
for k, v in adj_list.items():
    print(f"{k}: {v}")


def dfs(start):
    visited, order = [False] * n, []

    def visit(i):
        visited[i] = True
        order.append(labels[i])
        for j in range(n):
            if matrix[i][j] and not visited[j]:
                visit(j)

    visit(idx[start])
    return order


def bfs(start):
    visited, order, q = {start}, [], deque([start])
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj_list[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order


start = input("\nStart location: ")
if start in idx:
    print("BFS (adjacency list)  :", " -> ".join(bfs(start)))
    print("DFS (adjacency matrix):", " -> ".join(dfs(start)))
else:
    print("Invalid start location.")
