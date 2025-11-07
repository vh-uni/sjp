#!/usr/bin/python3

import math


def verify_trigonometric_identity(start_angle: float = 0, end_angle: float = 90) -> None:
    print(f"{'Angle (°)':<12} {'sin²(α)':<15} {'cos²(α)':<15} {'Sum':<15} {'Correct?':<10}")
    print("-" * 70)

    all_correct = True
    angle = start_angle

    while angle <= end_angle:
        angle_radians = math.radians(angle)

        sin_squared = math.sin(angle_radians) ** 2
        cos_squared = math.cos(angle_radians) ** 2

        sum_value = sin_squared + cos_squared

        is_correct = math.isclose(sum_value, 1.0)
        if not is_correct:
            all_correct = False

        print(f"{angle:<12.1f} {sin_squared:<15.10f} {cos_squared:<15.10f} {sum_value:<15.10f} {'✓' if is_correct else '✗':<10}")
        angle += 1

    print("-" * 70)
    if all_correct:
        print("✓ Trigonometric identity verified")
    else:
        print("✗ Trigonometric identity not verified")


def main() -> None:
    print("Verification of trigonometric identity: sin²(α) + cos²(α) = 1")
    print("=" * 70)
    verify_trigonometric_identity()


if __name__ == "__main__":
    main()