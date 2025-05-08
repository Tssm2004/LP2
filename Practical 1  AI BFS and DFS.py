graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
}

visited = []  # List to keep track of visited nodes
queue = []  # Queue to explore the nodes

def bfs(visited, graph, node):
    visited.append(node)  # Start with the node
    queue.append(node)  # Add the node to the queue

    # While there are nodes in the queue, keep processing them
    while queue:
        m = queue.pop(0)  # Dequeue the first node
        print(m, end=" ")  # Print the current node

        # Add all the unvisited neighbors to the queue
        for neighbour in graph[m]:
            if neighbour not in visited:  # If the neighbor has not been visited
                visited.append(neighbour)  # Mark as visited
                queue.append(neighbour)  # Add to the queue

print("Following is the path using BFS:")
bfs(visited, graph, 'A')
