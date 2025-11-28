#!/usr/bin/python3

import pytest
import os
import tempfile
from zd6 import identify_phone_pattern
from zd9 import find_files_by_extension


class TestIdentifyPhonePattern:
    """Tests for identify_phone_pattern function"""

    def test_plus_plain_format(self):
        """Test identifying phone number with plus sign and no separators"""
        # Arrange
        phone_number = "+48123456789"
        expected_pattern = "plus_plain"

        # Act
        result = identify_phone_pattern(phone_number)

        # Assert
        assert result == expected_pattern, \
            f"Expected '{expected_pattern}' for '{phone_number}', got '{result}'"

    def test_zero_spaced_format(self):
        """Test identifying phone number with 00 prefix and spaces"""
        # Arrange
        phone_number = "0048 111 222 333"
        expected_pattern = "zero_spaced"

        # Act
        result = identify_phone_pattern(phone_number)

        # Assert
        assert result == expected_pattern, \
            f"Expected '{expected_pattern}' for '{phone_number}', got '{result}'"

    def test_invalid_format(self):
        """Test identifying invalid phone number format"""
        # Arrange
        phone_number = "123-456-789"
        expected_pattern = "invalid"

        # Act
        result = identify_phone_pattern(phone_number)

        # Assert
        assert result == expected_pattern, \
            f"Expected '{expected_pattern}' for '{phone_number}', got '{result}'"

    def test_plus_dashed_format(self):
        """Test identifying phone number with plus sign and dashes"""
        # Arrange
        phone_number = "+48-500-600-700"
        expected_pattern = "plus_dashed"

        # Act
        result = identify_phone_pattern(phone_number)

        # Assert
        assert result == expected_pattern, \
            f"Expected '{expected_pattern}' for '{phone_number}', got '{result}'"

    def test_zero_plain_format(self):
        """Test identifying phone number with 00 prefix and no separators"""
        # Arrange
        phone_number = "0048987654321"
        expected_pattern = "zero_plain"

        # Act
        result = identify_phone_pattern(phone_number)

        # Assert
        assert result == expected_pattern, \
            f"Expected '{expected_pattern}' for '{phone_number}', got '{result}'"

    def test_plus_spaced_format(self):
        """Test identifying phone number with plus sign and spaces"""
        # Arrange
        phone_number = "+1 202 555 0123"
        expected_pattern = "plus_spaced"

        # Act
        result = identify_phone_pattern(phone_number)

        # Assert
        assert result == expected_pattern, \
            f"Expected '{expected_pattern}' for '{phone_number}', got '{result}'"


class TestFindFilesByExtension:
    """Tests for find_files_by_extension function"""

    def test_find_txt_files_in_current_directory(self):
        """Test finding .txt files in the current directory"""
        # Arrange
        extension = "txt"

        # Act
        result = find_files_by_extension(extension, ".")

        # Assert
        assert isinstance(result, list), "Result should be a list"
        assert all(file.lower().endswith(".txt") for file in result), \
            "All returned files should end with .txt"

    def test_find_py_files_in_current_directory(self):
        """Test finding .py files in the current directory"""
        # Arrange
        extension = "py"

        # Act
        result = find_files_by_extension(extension, ".")

        # Assert
        assert isinstance(result, list), "Result should be a list"
        assert len(result) > 0, "Should find at least one .py file"
        assert all(file.lower().endswith(".py") for file in result), \
            "All returned files should end with .py"

    def test_find_files_with_case_insensitivity(self):
        """Test that file search is case-insensitive"""
        # Arrange
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test files with different case extensions
            test_files = ["test.TXT", "data.txt", "file.Txt"]
            for file in test_files:
                open(os.path.join(temp_dir, file), "w").close()

            extension = "txt"

            # Act
            result = find_files_by_extension(extension, temp_dir)

            # Assert
            assert len(result) == 3, \
                f"Should find all 3 .txt files regardless of case, found {len(result)}"

    def test_nonexistent_extension(self):
        """Test searching for files with extension that doesn't exist"""
        # Arrange
        extension = "nonexistent123"

        # Act
        result = find_files_by_extension(extension, ".")

        # Assert
        assert isinstance(result, list), "Result should be a list"
        assert len(result) == 0, "Should return empty list for non-existent extension"

    def test_nonexistent_directory(self):
        """Test searching in a directory that doesn't exist"""
        # Arrange
        extension = "txt"
        nonexistent_dir = "nonexistent_directory_xyz"

        # Act
        result = find_files_by_extension(extension, nonexistent_dir)

        # Assert
        assert result == [], \
            "Should return empty list when directory doesn't exist"

    def test_find_specific_extension_excludes_others(self):
        """Test that searching for .txt doesn't return .py files"""
        # Arrange
        extension = "txt"

        # Act
        result = find_files_by_extension(extension, ".")

        # Assert
        assert not any(file.lower().endswith(".py") for file in result), \
            "Should not include .py files when searching for .txt"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
