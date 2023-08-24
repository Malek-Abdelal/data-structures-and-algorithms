class Vertex:
    def __init__(self, value):

        self.value = value
    def __str__(self):
        return str(self.value)
    
class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.__adj_list = {}

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        if start_vertex == end_vertex :
            edge1 = Edge(end_vertex, weight)
            self.__adj_list[start_vertex].append(edge1)
            return 
        
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)

    def get_vertices(self):
      return self.__adj_list.keys()
    
    def size(self):
      return len(self.__adj_list)
    
    def get_neighbors(self,vertex):
      return self.__adj_list.get(vertex, [])
    

    def depth_first(self, start_vertex):
        
        result = []
        visited = set()
        
        def helper(vertex):
            if vertex not in visited:
                result.append(vertex.value)
                visited.add(vertex)
                for edge in self.get_neighbors(vertex):
                    neighbor = edge.vertex
                    helper(neighbor)
        
        helper(start_vertex)
        return result