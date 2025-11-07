#!/usr/bin/python3

import pytest
from zd1 import Student


class TestStudentCalculateAverage:
    """Testy dla metody calculate_average klasy Student"""

    def test_calculate_average_with_multiple_marks(self):
        """Test obliczania średniej z kilku ocen"""
        # Arrange
        student = Student()
        student.give_mark(5)
        student.give_mark(4)
        student.give_mark(3)
        
        # Act
        average = student.calculate_average()
        
        # Assert
        assert average == 4.0, "Średnia z ocen [5, 4, 3] powinna wynosić 4.0"

    def test_calculate_average_with_single_mark(self):
        """Test obliczania średniej z pojedynczej oceny"""
        # Arrange
        student = Student()
        student.give_mark(5)
        
        # Act
        average = student.calculate_average()
        
        # Assert
        assert average == 5.0, "Średnia z jednej oceny [5] powinna wynosić 5.0"

    def test_calculate_average_with_no_marks_raises_error(self):
        """Test sprawdzający, czy metoda zgłasza błąd przy braku ocen"""
        # Arrange
        student = Student()
        
        # Act & Assert
        with pytest.raises(ZeroDivisionError):
            student.calculate_average()


class TestStudentGiveMark:
    """Testy dla metody give_mark klasy Student"""

    def test_give_mark_adds_single_mark(self):
        """Test dodawania pojedynczej oceny"""
        # Arrange
        student = Student()
        
        # Act
        student.give_mark(5)
        
        # Assert
        assert student.get_marks() == [5], "Lista ocen powinna zawierać jedną ocenę: [5]"

    def test_give_mark_adds_multiple_marks(self):
        """Test dodawania wielu ocen"""
        # Arrange
        student = Student()
        
        # Act
        student.give_mark(5)
        student.give_mark(4)
        student.give_mark(3)
        
        # Assert
        assert student.get_marks() == [5, 4, 3], "Lista ocen powinna zawierać [5, 4, 3]"

    def test_give_mark_maintains_order(self):
        """Test sprawdzający zachowanie kolejności dodawanych ocen"""
        # Arrange
        student = Student()
        
        # Act
        student.give_mark(2)
        student.give_mark(5)
        student.give_mark(3)
        
        # Assert
        marks = student.get_marks()
        assert marks == [2, 5, 3], "Kolejność ocen powinna być zachowana: [2, 5, 3]"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
