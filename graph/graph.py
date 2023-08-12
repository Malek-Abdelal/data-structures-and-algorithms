from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def dequeue(self):
        return self.queue.popleft()
    
    def enqueue(self, value):
        self.queue.append(value)

    def __len__(self):
        return len(self.queue)


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, value):
        """
        Add a vertex to the graph.
        Args:
            value: Value of the vertex to be added.
        Returns:
            The added vertex.
        """
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Add a new edge between two vertices in the graph.
        Args:
            start_vertex: Starting vertex of the edge.
            end_vertex: Ending vertex of the edge.
            weight: Weight of the edge (default is 0).
        Returns: None
        """
        if start_vertex not in self.adjacency_list:
            raise KeyError("Start vertex not found")
        if end_vertex not in self.adjacency_list:
            raise KeyError("End vertex not found")

        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex)
        self.adjacency_list[start_vertex].append(edge1)
        self.adjacency_list[end_vertex].append(edge2)

    def get_vertices(self):
        """
        Get all vertices in the graph.
        Returns:
            A collection of all vertices in the graph.
        """
        return self.adjacency_list.keys()

    def size(self):
        """
        Get the total number of vertices in the graph.
        Returns:
            The number of vertices in the graph.
        """
        return len(self.adjacency_list)

    def get_neighbors(self, vertex):
        """
        Get neighbors of a vertex.
        Args:
            vertex: Vertex for which to get neighbors.
        Returns:
            A collection of edges connected to the given vertex.
        """
        return self.adjacency_list.get(vertex, [])

    def breadth_first(self, start_vertex):
        """
        Perform breadth-first traversal of the graph.
        Args:
            start_vertex: Starting vertex for traversal.
        Returns: List of values visited during breadth-first traversal.
        """
        result = []
        visited = set()
        queue = Queue()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)

        return result


if __name__ == "__main__":
    graph = Graph()
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_e = graph.add_vertex('E')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_a, vertex_c)
    graph.add_edge(vertex_b, vertex_d)
    graph.add_edge(vertex_b, vertex_e)
    graph.add_edge(vertex_e, vertex_d)
    graph.add_edge(vertex_e, vertex_c)
    print(graph.breadth_first(vertex_a))
