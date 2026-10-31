from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
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
entrada_tarea = QLineEdit()
entrada_tarea.setPlaceholderText("Escribe una tarea...")
boton_agregar = QPushButton("Agregar")
lista_tareas = QListWidget()

layout_principal = QVBoxLayout()
layout_principal.addWidget(title, alignment=Qt.AlignCenter)

layout_entrada = QHBoxLayout()
layout_entrada.addWidget(entrada_tarea)
layout_entrada.addWidget(boton_agregar)
layout_principal.addLayout(layout_entrada)
layout_principal.addWidget(lista_tareas)

Ventana_principal.setLayout(layout_principal)


def agregar_tarea():
    tarea = entrada_tarea.text().strip()
    if not tarea or lista_tareas.findItems(tarea, Qt.MatchExactly):
        return

    lista_tareas.addItem(tarea)
    entrada_tarea.clear()
    entrada_tarea.setFocus()


boton_agregar.clicked.connect(agregar_tarea)
entrada_tarea.returnPressed.connect(agregar_tarea)

Ventana_principal.show()
entrada_tarea.setFocus()
sys.exit(app.exec_())
