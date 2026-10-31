from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QLabel,
    QPushButton,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
)

from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)

Ventana_principal = QWidget()
Ventana_principal.setWindowTitle('Gestor de Tareas')
Ventana_principal.setFixedSize(900,600)
Ventana_principal.setGeometry(0, 0, 900, 600)

title = QLabel("Mis Tareas", Ventana_principal)
layout_principal = QVBoxLayout()
layout_principal.addStretch(2)
layout_principal.addWidget(title, alignment=Qt.AlignCenter)
layout_principal.addStretch(3)

Ventana_principal.setLayout(layout_principal)
Ventana_principal.show()
sys.exit(app.exec_())
