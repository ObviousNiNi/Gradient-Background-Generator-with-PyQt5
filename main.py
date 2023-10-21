import sys
from PyQt5.QtWidgets import QApplication
from gui import logic
from styles import slider_style, hQline_style, wQline_style, gen_button_style

def main():
    app = QApplication(sys.argv)
    window = logic()
    # Aplica el estilo al QSlider vertical
    window.vertical_slider.setStyleSheet(slider_style)
    # Aplica el estilo al height QLineEdit
    window.height_text.setStyleSheet(hQline_style)
    # Aplica el estilo al width QLineEdit
    window.width_text.setStyleSheet(wQline_style)
    # Aplica el estilo al QPushButton
    window.generate_button.setStyleSheet(gen_button_style)


    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
