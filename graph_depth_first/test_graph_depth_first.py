from graph_depth_first.graph_depth_first import Graph

def build_sample_graph():
    g = Graph()

    a = g.add_vertex('A')
    b = g.add_vertex('B')
    c = g.add_vertex('C')
    d = g.add_vertex('D')
    e = g.add_vertex('E')
    f = g.add_vertex('F')
    g_vertex = g.add_vertex('G')
    h = g.add_vertex('H')

    g.add_edge(a, b)
    g.add_edge(b, a)

    g.add_edge(b, c)
    g.add_edge(c, b)

    g.add_edge(c, g_vertex)
    g.add_edge(g_vertex, c)

    g.add_edge(a, d)
    g.add_edge(d, a)

    g.add_edge(b, d)
    g.add_edge(d, b)

    g.add_edge(d, e)
    g.add_edge(e, d)

    g.add_edge(d, h)
    g.add_edge(h, d)

    g.add_edge(d, f)
    g.add_edge(f, d)

    return g, a, h, c

def test_depth_first_1():
    graph, start_vertex, _, _ = build_sample_graph()

    depth_first = graph.depth_first(start_vertex)

    assert depth_first == ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']

def test_depth_first_2():
    graph, _, start_vertex, _ = build_sample_graph()

    depth_first = graph.depth_first(start_vertex)

    assert depth_first == ['H', 'D', 'A', 'B', 'C', 'G', 'E', 'F']

def test_depth_first_3():
    graph, _, _, start_vertex = build_sample_graph()

    depth_first = graph.depth_first(start_vertex)

    assert depth_first == ['C', 'B', 'A', 'D', 'E', 'H', 'F', 'G']
