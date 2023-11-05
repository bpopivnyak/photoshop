from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(500, 500)
folder = QPushButton("Папка")
Left = QPushButton("Вліво")
Right = QPushButton("Вправо")
mirror = QPushButton("Дзеркало")
sharpness = QPushButton("Різкість")
BW = QPushButton("Ч/Б")



mainLine = QHBoxLayout()

window.setLayout(mainLine)
window.show()

app.exec()