import os

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QMainWindow, QColorDialog, QLabel, QLineEdit, QPushButton, QSlider
from PyQt5.uic import loadUi
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap, QImage

class logic(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("m_win.ui", self)
        self.setFixedSize(self.size())
        self.color_button_left.clicked.connect(self.openColorDialogLeft)
        self.color_button_right.clicked.connect(self.openColorDialogRight)

        # Obtén una referencia al QLabel "gradient_preview"
        self.gradient_preview = self.findChild(QLabel, "gradient_preview")

        # Obtén una referencia al QSlider "verticalSlider"
        self.vertical_slider = self.findChild(QSlider, "verticalSlider")

        self.vertical_slider.valueChanged.connect(self.updateGradient)
        # Cuadros de texto para el ancho y el alto
        self.width_text = self.findChild(QLineEdit, "width_text")
        self.height_text = self.findChild(QLineEdit, "height_text")

        # Botón para generar la imagen
        self.generate_button = self.findChild(QPushButton, "gen_button")

        # Conectar el botón "generate" a la función de generación de imagen
        self.generate_button.clicked.connect(self.generateImage)

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

    def generateGradientImage(self, width, height, normalized_value, left_color, right_color):
        # Crear una imagen en blanco
        gradient_image = Image.new("RGB", (width, height))

        # Crear un objeto de dibujo
        draw = ImageDraw.Draw(gradient_image)

        # Obtener componentes de color de los colores de inicio y final
        r_start, g_start, b_start = left_color.getRgb()[:3]
        r_end, g_end, b_end = right_color.getRgb()[:3]

        for y in range(height):
            position = y / height  # Proporción vertical de la línea actual
            blended_r = int(r_start * (1 - normalized_value) + r_end * normalized_value)
            blended_g = int(g_start * (1 - normalized_value) + g_end * normalized_value)
            blended_b = int(b_start * (1 - normalized_value) + b_end * normalized_value)

            r = int(blended_r + (r_end - blended_r) * position)
            g = int(blended_g + (g_end - blended_g) * position)
            b = int(blended_b + (b_end - blended_b) * position)

            # Dibujar una línea horizontal en la imagen
            draw.line([(0, y), (width, y)], fill=(r, g, b))

        # Convertir la imagen de Pillow a QPixmap
        gradient_image_qimage = QImage(gradient_image.tobytes("raw", "RGB"), gradient_image.width,
                                       gradient_image.height, QImage.Format_RGB888)
        gradient_pixmap = QPixmap.fromImage(gradient_image_qimage)

        return gradient_pixmap

    def updateGradient(self):
        # Obtén los colores de los botones
        left_color = QColor(self.color_button_left.palette().color(QPalette.Button))
        right_color = QColor(self.color_button_right.palette().color(QPalette.Button))

        # Obtén el valor del QSlider
        slider_value = self.vertical_slider.value()

        # Convierte el valor del slider a un número flotante entre 0 y 1
        normalized_value = slider_value / 100

        # Generar la imagen del gradiente
        gradient_image = self.generateGradientImage(
            self.gradient_preview.width(),
            self.gradient_preview.height(),
            normalized_value,
            left_color,
            right_color
        )

        # Muestra la imagen en el QLabel
        self.gradient_preview.setPixmap(gradient_image)



    def generateImage(self):
        try:

            # Obtén los valores de ancho y alto desde los QLineEdits
            width = int(self.width_text.text())
            height = int(self.height_text.text())

            # Obtén los colores de los botones
            left_color = QColor(self.color_button_left.palette().color(QPalette.Button))
            right_color = QColor(self.color_button_right.palette().color(QPalette.Button))

            # Obtén el valor del QSlider
            slider_value = self.vertical_slider.value()

            # Convierte el valor del slider a un número flotante entre 0 y 1
            normalized_value = slider_value / 100

            # Generar la imagen del gradiente
            gradient_image = self.generateGradientImage(width, height, normalized_value, left_color, right_color)

            # Directorio para guardar la imagen
            save_dir = "imgs"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # Nombre de la imagen
            image_name = "Complete Gradient.png"

            # Ruta completa para guardar la imagen
            img_path = os.path.join(save_dir, image_name)

            # Guardar la imagen en el directorio
            gradient_image.save(img_path)

            print(f"Imagen generada y guardada en {img_path}")

        except Exception as e:
            print(f"Error al guardar la imagen: {e}")
