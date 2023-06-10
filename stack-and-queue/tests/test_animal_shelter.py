import pytest
from stack_queue_animal_shelter import AnimalShelter

def test_enqueue(capsys):
    animal_shel = AnimalShelter()
    animal_shel.enqueue("dog", "Mossberg")
    animal_shel.enqueue("cat", "Mirabel")
    animal_shel.print()
    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == "Animal Type: dog, Animal Name: Mossberg\nAnimal Type: cat, Animal Name: Mirabel"


def test_dequeue(capsys):
    animal_shel1 = AnimalShelter()
    animal_shel1.enqueue("dog", "Mossberg")
    animal_shel1.enqueue("cat", "Mirabel")
    animal_shel1.enqueue("dog", "Max")
    animal_shel1.dequeue("cat")

    animal_shel1.print()
    captured = capsys.readouterr()
    output = captured.out.strip()


    assert output == "Mirabel\nAnimal Type: dog, Animal Name: Mossberg\nAnimal Type: dog, Animal Name: Max"

def test_invalid_pref():
    animal_shel1 = AnimalShelter()
    animal_shel1.enqueue("dog", "Buddy")
    animal_shel1.enqueue("cat", "Whiskers")

    invalid_pref = animal_shel1.dequeue("lion")

    assert invalid_pref is None