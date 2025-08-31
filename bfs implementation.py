from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    visited.add(start_node)

    while queue: 
        node = queue.popleft() 
        print(node, end=" ") 

        for neighbor in graph[node]:
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append(neighbor)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS traversal starting from node A:")
    bfs(graph, 'A') 
