import pytest
from hashmap_repeated_word.hashmap_repeated_word import find_first_repeated_word

def test_find_first_repeated_word_middle():
    """
    Test if the function can find the first repeated word in the middle of the string.
    """
    string = "This is a test string with repeated word test in the middle."
    assert find_first_repeated_word(string) == "test"

def test_find_first_repeated_word_beginning():
    """
    Test if the function can find the first repeated word at the beginning of the string.
    """
    string = "test this is a test string with a repeated word at the beginning."
    assert find_first_repeated_word(string) == "test"

def test_find_first_repeated_word_end():
    """
    Test if the function can find the first repeated word at the end of the string.
    """
    string = "This is test string with a repeated word at the end test."
    assert find_first_repeated_word(string) == "test"

def test_find_first_repeated_word_no_repetition():
    """
    Test if the function correctly handles a string with no repeated words.
    """
    string = "This is a test string with no repeated words."
    assert find_first_repeated_word(string) == "No Repetition"

def test_find_first_repeated_word_empty_string():
    """
    Test if the function correctly handles an empty string.
    """
    string = ""
    assert find_first_repeated_word(string) == "No Repetition"
