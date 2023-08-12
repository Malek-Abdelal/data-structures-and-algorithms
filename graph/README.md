# Graph Implementation

Implementing Graph with it's methods **(add_vertex, add_edge, get_vertices, size, get_neighbors, breadth_first)**.

## The time and space complexity for each method:

**1. add_vertex(self, value):**

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**2. add_edge(self, start_vertex, end_vertex, weight=0):**

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**3. get_vertices(self):**

**Time Complexity:** O(V), where V is the number of vertices.

**Space Complexity:** O(V)

**4. size(self):**

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**5. get_neighbors(self, vertex):**

**Time Complexity:** O(1) on average, but can be O(E) in the worst case, where E is the number of edges connected to the vertex

**Space Complexity:** O(E), where E is the number of edges connected to the vertex

**6. breadth_first(self, start_vertex):**

**Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges in the graph

**Space Complexity:** O(V), as the visited set and the queue can store at most all vertices