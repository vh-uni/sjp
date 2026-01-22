#!/usr/bin/python3

import pytest
import math
from zd6 import calculate_ladder_height


class TestCalculateLadderHeight:
    """Tests for calculate_ladder_height function"""

    def test_ladder_at_90_degrees(self):
        """Test calculating height for a ladder at 90 degrees (vertical position)"""
        # Arrange
        length = 5.0
        angle = 90.0
        expected_height = 5.0

        # Act
        result = calculate_ladder_height(length, angle)

        # Assert
        assert math.isclose(result, expected_height), \
            f"For ladder length {length}m at angle {angle}° expected {expected_height}m, got {result}m"

    def test_ladder_at_30_degrees(self):
        """Test calculating height for a ladder at 30 degrees"""
        # Arrange
        length = 5.0
        angle = 30.0
        expected_height = 2.5

        # Act
        result = calculate_ladder_height(length, angle)

        # Assert
        assert math.isclose(result, expected_height), \
            f"For ladder length {length}m at angle {angle}° expected {expected_height}m, got {result}m"

    def test_ladder_at_0_degrees(self):
        """Test calculating height for a ladder at 0 degrees (horizontal position)"""
        # Arrange
        length = 5.0
        angle = 0.0
        expected_height = 0.0

        # Act
        result = calculate_ladder_height(length, angle)

        # Assert
        assert math.isclose(result, expected_height), \
            f"For ladder length {length}m at angle {angle}° expected {expected_height}m, got {result}m"

    def test_ladder_at_45_degrees(self):
        """Test calculating height for a ladder at 45 degrees"""
        # Arrange
        length = 10.0
        angle = 45.0
        expected_height = 10.0 * math.sin(math.radians(45))  # ≈ 7.071

        # Act
        result = calculate_ladder_height(length, angle)

        # Assert
        assert math.isclose(result, expected_height), \
            f"For ladder length {length}m at angle {angle}° expected {expected_height:.3f}m, got {result:.3f}m"

    def test_ladder_at_60_degrees(self):
        """Test calculating height for a ladder at 60 degrees"""
        # Arrange
        length = 4.0
        angle = 60.0
        expected_height = 4.0 * math.sin(math.radians(60))  # ~3.464

        # Act
        result = calculate_ladder_height(length, angle)

        # Assert
        assert math.isclose(result, expected_height), \
            f"For ladder length {length}m at angle {angle}° expected {expected_height:.3f}m, got {result:.3f}m"

    def test_different_ladder_lengths(self):
        """Test verifying proportionality - doubling ladder length should double height"""
        # Arrange
        angle = 30.0
        length1 = 6.0
        length2 = 12.0

        # Act
        height1 = calculate_ladder_height(length1, angle)
        height2 = calculate_ladder_height(length2, angle)

        # Assert
        assert math.isclose(height2, 2 * height1), \
            f"Doubling ladder length should double height: {height1}m * 2 != {height2}m"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

