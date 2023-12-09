import math
import doctest

def trigonometric_functions(angle_degrees):
    """Calculate trigonometric functions for a given angle in degrees

    :param angle_degrees: Angle in degrees
    :return: Tuple of (sin, cos, tan) values for the angle
    
    >>> trigonometric_functions(30)
    (0.49999999999999994, 0.8660254037844387, 0.5773502691896256)
    """
    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    return sin_value, cos_value, tan_value

# Calculate trigonometric functions for a 45-degree angle
angle_degrees = 45
sin, cos, tan = trigonometric_functions(angle_degrees)

print(f"Angle: {angle_degrees} degrees")
print(f"Sine: {sin}")
print(f"Cosine: {cos}")
print(f"Tangent: {tan}")

doctest.testmod()
