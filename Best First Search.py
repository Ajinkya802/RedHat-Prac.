from queue import PriorityQueue

def best_first_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start)  # Use a priority queue with the initial node
    came_from = {}  # Dictionary to store the best path
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in came_from:
                came_from[neighbor] = current
                frontier.put(neighbor)

    return None

def reconstruct_path(came_from, current):
    path = []
    while current:
        path.insert(0, current)
        current = came_from[current]
    return path

# Example usage:
graph = {
    'a': [('b', 2)],
    'b': [('c', 3), ('d', 4)],
    'c': [('e', 5)],
    'd': [('e', 1)],
    'e': [('f', 2)],
}

start_node = 'a'
goal_node = 'f'
path = best_first_search(graph, start_node, goal_node)

if path:
    print(f"Shortest path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
