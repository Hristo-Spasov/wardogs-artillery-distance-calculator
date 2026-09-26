import math


def calculate(enemy_x, enemy_y, your_x, your_y, result):
    try:
        x1 = float(your_x.value())
        y1 = float(your_y.value())
        x2 = float(enemy_x.value())
        y2 = float(enemy_y.value())

    except ValueError:
        result.setText("Please enter all coordinates")
        return

    dx = x2 - x1
    dy = y2 - y1

    distance = math.sqrt(dx**2 + dy**2)

    result.setText(f"Distance: {distance:.0f} meters")
