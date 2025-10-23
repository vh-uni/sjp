#!/usr/bin/python3


def input_list(numbers):
    """Tworzy listę z liczb i zwraca listę oraz unikalne elementy"""
    new_list = []
    for num in numbers:
        try:
            new_list.append(int(num))
        except:
            pass
    return new_list, set(new_list)


def odd_filter():
    """Filtruje nieparzyste liczby z listy 1-10 i zwraca minimum"""
    new_list = [i for i in range(1, 11)]
    odd_elements = list(filter(lambda x: x % 2 == 1, new_list))
    return odd_elements, min(odd_elements)


def unite_lists(list_a, list_b):
    """Łączy dwie listy na dwa różne sposoby"""
    list_c = list(list_a)
    list_a[:0] = list_b
    list_b[:0] = list_c
    return list_a, list_b


# ===== TESTY DLA input_list() =====

def test_input_list_valid_numbers():
    """Test z poprawnymi liczbami"""
    result, unique = input_list(['5', '10', '15'])
    assert result == [5, 10, 15]
    assert unique == {5, 10, 15}


def test_input_list_with_duplicates():
    """Test z duplikatami"""
    result, unique = input_list(['3', '3', '7', '3'])
    assert result == [3, 3, 7, 3]
    assert unique == {3, 7}


def test_input_list_with_invalid():
    """Test z błędnymi danymi"""
    result, unique = input_list(['12', 'abc', '5', 'xyz'])
    assert result == [12, 5]
    assert unique == {12, 5}


# ===== TESTY DLA odd_filter() =====

def test_odd_filter_returns_correct_odds():
    """Test zwracania nieparzystych"""
    odds, minimum = odd_filter()
    assert odds == [1, 3, 5, 7, 9]


def test_odd_filter_returns_correct_minimum():
    """Test minimum nieparzystych"""
    odds, minimum = odd_filter()
    assert minimum == 1


def test_odd_filter_length():
    """Test długości listy nieparzystych"""
    odds, minimum = odd_filter()
    assert len(odds) == 5


# ===== TESTY DLA unite_lists() =====

def test_unite_lists_basic():
    """Test podstawowej zamiany"""
    a, b = unite_lists([1, 2, 3], [4, 5, 6])
    assert a == [4, 5, 6, 1, 2, 3]
    assert b == [1, 2, 3, 4, 5, 6]


def test_unite_lists_different_lengths():
    """Test z listami różnej długości"""
    a, b = unite_lists([1, 2], [3, 4, 5, 6])
    assert a == [3, 4, 5, 6, 1, 2]
    assert b == [1, 2, 3, 4, 5, 6]


def test_unite_lists_with_empty():
    """Test z pustą listą"""
    a, b = unite_lists([1, 2, 3], [])
    assert a == [1, 2, 3]
    assert b == [1, 2, 3]