from collections import deque

# Function to perform Breadth-First Search (BFS) on a graph
def bfs(graph, start):
    # Set to keep track of visited nodes
    visited = set()
    # Queue for nodes to visit
    queue = deque([start])
    # Add the start node to the visited set
    visited.add(start)

    # While there are nodes in the queue
    while queue:
        # Dequeue the next node
        vertex = queue.popleft()
        # Print the node
        print(vertex, end=" ")

        # Iterate over the neighbors of the current node
        for neighbor in graph[vertex]:
            # If the neighbor has not been visited
            if neighbor not in visited:
                # Add the neighbor to the queue
                queue.append(neighbor)
                # Add the neighbor to the visited set
                visited.add(neighbor)

# Example graph representation (dictionary of lists)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal:")
bfs(graph, 'A')

