import sys
import os
from calculator import calculate
from PySide6.QtCore import QLocale
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QDoubleSpinBox,
    QPushButton,
)


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath("."), relative)


class CoordinateInput(QDoubleSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Force dot as decimal separator regardless of system locale
        self.setLocale(QLocale.c())

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.selectAll()


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("War Dogs Artillery Calculator")
window.setWindowIcon(QIcon(resource_path("assets/artillery.ico")))
window.resize(400, 300)

layout = QVBoxLayout(window)

# Your position
your_position = QVBoxLayout()

your_position.addWidget(QLabel("Your X"))
your_x = CoordinateInput()
your_x.setRange(0, 99999)
your_x.setDecimals(2)
your_position.addWidget(your_x)

your_position.addWidget(QLabel("Your Y"))
your_y = CoordinateInput()
your_y.setRange(0, 99999)
your_y.setDecimals(2)

your_position.addWidget(your_y)


# Enemy position
enemy_position = QVBoxLayout()

enemy_position.addWidget(QLabel("Enemy X"))
enemy_x = CoordinateInput()
enemy_x.setRange(0, 99999)
enemy_x.setDecimals(2)

enemy_position.addWidget(enemy_x)

enemy_position.addWidget(QLabel("Enemy Y"))
enemy_y = CoordinateInput()
enemy_y.setRange(0, 99999)
enemy_y.setDecimals(2)

enemy_position.addWidget(enemy_y)


positions = QHBoxLayout()

positions.addLayout(your_position)
positions.addLayout(enemy_position)

layout.addLayout(positions)


# Calculate button
button = QPushButton("Calculate")
layout.addWidget(button)

result = QLabel("Distance: -")
layout.addWidget(result)

button.clicked.connect(lambda: calculate(enemy_x, enemy_y, your_x, your_y, result))

window.show()

app.exec()
