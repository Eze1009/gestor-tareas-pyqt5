from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
    QMessageBox,
    QInputDialog,
    QHBoxLayout,
    QVBoxLayout,
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
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
boton_completar = QPushButton("Completar")
boton_eliminar = QPushButton("Eliminar")
boton_completar.setEnabled(False)
boton_eliminar.setEnabled(False)

layout_principal = QVBoxLayout()
layout_principal.addWidget(title, alignment=Qt.AlignCenter)

layout_entrada = QHBoxLayout()
layout_entrada.addWidget(entrada_tarea)
layout_entrada.addWidget(boton_agregar)
layout_principal.addLayout(layout_entrada)
layout_principal.addWidget(lista_tareas)

layout_acciones = QHBoxLayout()
layout_acciones.addWidget(boton_completar)
layout_acciones.addWidget(boton_eliminar)
layout_principal.addLayout(layout_acciones)

Ventana_principal.setLayout(layout_principal)


def agregar_tarea():
    tarea = entrada_tarea.text().strip()
    if not tarea or lista_tareas.findItems(tarea, Qt.MatchExactly):
        return

    lista_tareas.addItem(tarea)
    entrada_tarea.clear()
    entrada_tarea.setFocus()


def actualizar_estado_botones():
    hay_seleccion = lista_tareas.currentItem() is not None
    boton_completar.setEnabled(hay_seleccion)
    boton_eliminar.setEnabled(hay_seleccion)


def completar_tarea():
    tarea = lista_tareas.currentItem()
    if tarea is None:
        return

    completada = not tarea.data(Qt.UserRole)
    tarea.setData(Qt.UserRole, completada)
    fuente = tarea.font()
    fuente.setStrikeOut(completada)
    tarea.setFont(fuente)
    tarea.setForeground(QBrush(QColor("gray")) if completada else QBrush())


def eliminar_tarea():
    tarea = lista_tareas.currentItem()
    if tarea is None:
        return

    respuesta = QMessageBox.question(
        Ventana_principal,
        "Eliminar tarea",
        f"¿Seguro que quieres eliminar «{tarea.text()}»?",
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No,
    )
    if respuesta == QMessageBox.Yes:
        lista_tareas.takeItem(lista_tareas.row(tarea))


def editar_tarea(tarea):
    texto, aceptado = QInputDialog.getText(
        Ventana_principal,
        "Editar tarea",
        "Texto de la tarea:",
        text=tarea.text(),
    )
    texto = texto.strip()
    fila_tarea = lista_tareas.row(tarea)
    if (
        aceptado
        and texto
        and not any(
            indice != fila_tarea
            and lista_tareas.item(indice).text() == texto
            for indice in range(lista_tareas.count())
        )
    ):
        tarea.setText(texto)


boton_agregar.clicked.connect(agregar_tarea)
entrada_tarea.returnPressed.connect(agregar_tarea)
lista_tareas.currentItemChanged.connect(actualizar_estado_botones)
boton_completar.clicked.connect(completar_tarea)
boton_eliminar.clicked.connect(eliminar_tarea)
lista_tareas.itemDoubleClicked.connect(editar_tarea)

Ventana_principal.show()
entrada_tarea.setFocus()
sys.exit(app.exec_())
