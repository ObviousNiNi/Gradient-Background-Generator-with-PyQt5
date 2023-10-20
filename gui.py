import os

from PyQt5.QtGui import QColor, QLinearGradient, QPalette, QPixmap, QPainter
from PyQt5.QtWidgets import QMainWindow, QColorDialog, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class logic(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("m_win.ui", self)
        self.setFixedSize(self.size())
        self.color_button_left.clicked.connect(self.openColorDialogLeft)
        self.color_button_right.clicked.connect(self.openColorDialogRight)

        # Obtén una referencia al QLabel "gradient_preview"
        self.gradient_preview = self.findChild(QLabel, "gradient_preview")

        # Conectar la señal currentIndexChanged del QComboBox
        self.gradient_value.currentIndexChanged.connect(self.updateGradient)

        # Define el directorio para guardar las imágenes temporales
        self.img_dir = "imgs"

        # Asegúrate de que el directorio exista
        if not os.path.exists(self.img_dir):
            os.makedirs(self.img_dir)


        # Inicializa el gradiente con los colores actuales de los botones
        self.updateGradient()

    def openColorDialogLeft(self):
        color_dialog_left = QColorDialog(self)
        color = color_dialog_left.getColor()
        if color.isValid():
            self.color_button_left.setStyleSheet("background-color: " + color.name())
            self.updateGradient()

    def openColorDialogRight(self):
        color_dialog_right = QColorDialog(self)
        color = color_dialog_right.getColor()
        if color.isValid():
            self.color_button_right.setStyleSheet("background-color: " + color.name())
            self.updateGradient()

    def updateGradient(self):
        # Obtén los colores de los botones
        left_color = QColor(self.color_button_left.palette().color(QPalette.Button))
        right_color = QColor(self.color_button_right.palette().color(QPalette.Button))

        # Obtén el valor seleccionado en el combo box (de 0 a 100)
        gradient_value = self.gradient_value.currentText()

        # Convierte el valor del combo box a un número
        gradient_value = int(gradient_value)

        # Ajusta el valor a un rango entre 0 y 1
        normalized_value = gradient_value / 100

        # Crea un gradiente con los colores y la posición vertical
        gradient = QLinearGradient(0, 0, 0, self.gradient_preview.height())

        if normalized_value == 0:
            gradient.setColorAt(0, left_color)
            gradient.setColorAt(1, left_color)
        elif normalized_value == 1:
            gradient.setColorAt(0, right_color)
            gradient.setColorAt(1, right_color)
        else:
            gradient.setColorAt(0, left_color)
            gradient.setColorAt(normalized_value, left_color)
            gradient.setColorAt(normalized_value, right_color)
            gradient.setColorAt(1, right_color)

        # Crea un QPixmap con el tamaño del widget gradient_preview
        gradient_pixmap = QPixmap(self.gradient_preview.size())
        gradient_pixmap.fill(Qt.transparent)  # Rellena con fondo transparente

        # Crea un QPainter para dibujar en el QPixmap
        gradient_painter = QPainter(gradient_pixmap)
        gradient_painter.setRenderHint(QPainter.Antialiasing)
        gradient_painter.setBrush(gradient)

        # Dibuja el gradiente en el QPixmap
        gradient_painter.fillRect(gradient_pixmap.rect(), gradient)
        gradient_painter.end()  # Finaliza el dibujo

        # Define la ruta completa de la imagen en tu directorio
        img_path = os.path.join(self.img_dir, "gradient_image.png")

        # Guarda la imagen en el directorio específico
        gradient_pixmap.save(img_path)

        # Cargar la imagen desde el archivo guardado
        gradient_image = QPixmap(img_path)

        # Mostrar la imagen en el QLabel
        self.gradient_preview.setPixmap(gradient_image)

