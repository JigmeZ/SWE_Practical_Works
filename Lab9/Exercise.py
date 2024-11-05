from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)
    
    def find_shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None
        visited = set()
        queue = deque([[start_vertex]])  
        visited.add(start_vertex)

        while queue:
            path = queue.popleft()
            vertex = path[-1]

            # If we reached the end_vertex, return the path
            if vertex == end_vertex:
                return path

            # Otherwise, add all unvisited neighbors to the queue
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append(new_path)
        return None  
# Test finding the shortest path
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("\nShortest path from vertex 0 to vertex 4:")
shortest_path = g.find_shortest_path(0, 4)
if shortest_path:
    print(" -> ".join(map(str, shortest_path)))
else:
    print("No path found")





class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    
    def has_cycle(self):
        visited = set()
        
        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True
            return False

        return any(dfs(vertex, None) for vertex in self.graph if vertex not in visited)
# Test cycle detection
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Graph contains a cycle:" if g.has_cycle() else "Graph does not contain a cycle")

# Test with an acyclic graph
g2 = Graph()
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)

print("Graph contains a cycle:" if g2.has_cycle() else "Graph does not contain a cycle")



import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))  # For undirected graph

    def dijkstra(self, start_vertex):
        # Initialize distances and priority queue
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]  # (distance, vertex)
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # If the popped vertex has a greater distance than the recorded one, skip it
            if current_distance > distances[current_vertex]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Only consider this new path if it's shorter
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
# Test Dijkstra's algorithm
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 2)

print("Shortest paths from vertex 0:")
distances = g.dijkstra(0)
for vertex, distance in distances.items():
    print(f"Vertex {vertex} : Distance {distance}")



