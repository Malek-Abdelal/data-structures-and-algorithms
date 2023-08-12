import pytest
from graph import Graph, Vertex, Edge

@pytest.fixture
def graph():
    return Graph()

def test_add_vertex(graph):
    vertex = graph.add_vertex("A")
    assert vertex in graph.get_vertices()

def test_add_edge(graph):
    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")
    graph.add_edge(vertex_a, vertex_b, weight=3)
    neighbors = graph.get_neighbors(vertex_a)
    assert any(edge.vertex == vertex_b and edge.weight == 3 for edge in neighbors)

def test_get_vertices(graph):
    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")
    vertices = graph.get_vertices()
    assert vertex_a in vertices
    assert vertex_b in vertices

def test_get_neighbors(graph):
    vertex_a = graph.add_vertex("A")
    vertex_b = graph.add_vertex("B")
    graph.add_edge(vertex_a, vertex_b, weight=4)
    neighbors = graph.get_neighbors(vertex_a)
    assert any(edge.vertex == vertex_b and edge.weight == 4 for edge in neighbors)

def test_single_vertex_edge(graph):
    vertex_a = graph.add_vertex("A")
    graph.add_edge(vertex_a, vertex_a, weight=2)
    neighbors = graph.get_neighbors(vertex_a)
    assert any(edge.vertex == vertex_a and edge.weight == 2 for edge in neighbors)
