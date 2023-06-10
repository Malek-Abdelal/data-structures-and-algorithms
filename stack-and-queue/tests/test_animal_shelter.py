import pytest
from stack_queue_animal_shelter.animal_shelter import AnimalShelter, Animal

def test_enqueue(queue_with_3_elements_cat_dog_cat):
    actual = queue_with_3_elements_cat_dog_cat.back.name
    expected = "locyy"
    assert actual == expected

def test_dequeue(queue_with_3_elements_cat_dog_cat):
    actual = queue_with_3_elements_cat_dog_cat.dequeue("dog")
    expected = "joy"
    assert actual == expected

def test_cat_or_dog_is_not_preferred(queue_with_3_elements_cat_dog_cat):
    actual = queue_with_3_elements_cat_dog_cat.dequeue("lion")
    expected = "locy"
    assert actual == expected


@pytest.fixture
def queue_with_3_elements_cat_dog_cat():
    shelter = AnimalShelter()
    animal1 = Animal("cat", "locy")
    animal2 = Animal("dog", "joy") 
    animal3 = Animal("cat", "locyy")
    shelter.enqueue(animal1)
    shelter.enqueue(animal2)
    shelter.enqueue(animal3)
    return shelter
    