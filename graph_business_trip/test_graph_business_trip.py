import pytest
from graph_business_trip.graph_business_trip import Graph, business_trip 

def test_case_1():
    cities_names = ['Jarsh', 'Aqaba', 'Maan']
    cost = business_trip(new_graph, cities_names)
    assert cost == 115

def test_case_2():
    cities_names = ['Maan', 'Irbid']
    cost = business_trip(new_graph, cities_names)
    assert cost is None

def test_case_3():
    cities_names = ['Amman', 'Jarsh', 'Maan']
    cost = business_trip(new_graph, cities_names)
    assert cost is None

def test_case_4():
    cities_names = ["Zarqa", "Irbid"]
    cost = business_trip(new_graph, cities_names)
    assert cost == 82

def test_case_5():
    cities_names = ["Zarqa"]
    cost = business_trip(new_graph, cities_names)
    assert cost == 0

new_graph = Graph()
new_graph.add_vertex("Amman")
new_graph.add_vertex("Irbid")
new_graph.add_vertex("Aqaba")
new_graph.add_vertex("Jarsh")
new_graph.add_vertex("Maan")
new_graph.add_vertex("Zarqa")
new_graph.add_edge("Aqaba", "Zarqa", 105)
new_graph.add_edge("Zarqa", "Irbid", 82)
new_graph.add_edge("Maan", "Zarqa", 26)
new_graph.add_edge("Jarsh", "Zarqa", 99)
new_graph.add_edge("Irbid", "Jarsh", 150)
new_graph.add_edge("Jarsh", "Aqaba", 42)
new_graph.add_edge("Maan", "Amman", 250)
new_graph.add_edge("Zarqa", "Amman", 37)
new_graph.add_edge("Aqaba", "Maan", 73)