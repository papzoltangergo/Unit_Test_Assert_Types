import pytest
from text_processor import TextProcessor


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result == "HELLO WORLD"

def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result != "hello world"

def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("hello world")
    assert "olleh" in result
    assert "h" in result
    assert "world" not in result

def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("hello world")
    assert "hello" not in result
    assert "dlrow" in result
    assert "x" not in result

def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("hello world")
    assert result == 2
    assert isinstance(result, str) is False
    assert result is not None
    assert isinstance(processor.count_words("csokolom mama"), int)


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result1 = processor.count_words("hello world from pytest")
    result2 = processor.count_words("one two three four")
    result3 = processor.count_words("a b c d e f g h i j")
    assert result1 > result2 - 1
    assert result1 >= result2 - 1
    assert result3 > result1
    assert result2 < result1 + 2
    assert result2 <= result1 + 2 <= result3

def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    pass


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    pass


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    pass

#ypython -m pytest .\Unit_Test_Assert_Types\test_text_processor.py -v