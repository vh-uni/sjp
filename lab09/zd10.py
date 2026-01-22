#!/usr/bin/python3

import pytest
import numpy as np
from zd1 import replace_zeros


class TestReplaceZeros:
    """Tests for replace_zeros function"""

    def test_replace_zeros_with_positive_number(self):
        """Test replacing zeros with a positive number"""
        # Arrange
        arr = np.array([[0, 1, 2], [3, 0, 5], [0, 0, 8]])
        replacement_value = 10
        expected = np.array([[10, 1, 2], [3, 10, 5], [10, 10, 8]])

        # Act
        result = replace_zeros(arr, replacement_value)

        # Assert
        assert np.array_equal(result, expected), \
            f"Expected {expected}, got {result}"

    def test_replace_zeros_with_negative_number(self):
        """Test replacing zeros with a negative number"""
        # Arrange
        arr = np.array([[0, 5, 0], [10, 0, 15]])
        replacement_value = -1
        expected = np.array([[-1, 5, -1], [10, -1, 15]])

        # Act
        result = replace_zeros(arr, replacement_value)

        # Assert
        assert np.array_equal(result, expected), \
            f"Expected {expected}, got {result}"

    def test_replace_zeros_with_no_zeros_present(self):
        """Test replacing zeros when no zeros are present in array"""
        # Arrange
        arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        replacement_value = 99
        expected = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        # Act
        result = replace_zeros(arr, replacement_value)

        # Assert
        assert np.array_equal(result, expected), \
            f"Expected array to remain unchanged when no zeros present"

    def test_replace_zeros_with_zero(self):
        """Test replacing zeros with zero (edge case)"""
        # Arrange
        arr = np.array([[0, 1, 0], [2, 0, 3]])
        replacement_value = 0
        expected = np.array([[0, 1, 0], [2, 0, 3]])

        # Act
        result = replace_zeros(arr, replacement_value)

        # Assert
        assert np.array_equal(result, expected), \
            f"Expected {expected}, got {result}"

    def test_replace_all_zeros(self):
        """Test replacing zeros when entire array is zeros"""
        # Arrange
        arr = np.array([[0, 0, 0], [0, 0, 0]])
        replacement_value = 7
        expected = np.array([[7, 7, 7], [7, 7, 7]])

        # Act
        result = replace_zeros(arr, replacement_value)

        # Assert
        assert np.array_equal(result, expected), \
            f"Expected all zeros to be replaced with {replacement_value}"

    def test_replace_zeros_preserves_original_array(self):
        """Test that original array is not modified"""
        # Arrange
        arr = np.array([[0, 1, 2], [3, 0, 5]])
        original_copy = arr.copy()
        replacement_value = 100

        # Act
        result = replace_zeros(arr, replacement_value)

        # Assert
        assert np.array_equal(arr, original_copy), \
            "Original array should not be modified"
        assert not np.array_equal(result, arr), \
            "Result should be different from original array"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
