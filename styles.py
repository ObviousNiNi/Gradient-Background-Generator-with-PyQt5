slider_style = """
QSlider::groove:vertical {
    background: #543940;
    width: 10px;
    border-radius: 5px; 
}

QSlider::handle:vertical {
    background: #e1da1a; 
    width: 10px; 
    height: 20px;
    margin: 0px -7px; /* Ajusta la posición vertical y horizontal del handle para que esté fuera del groove */
    border-radius: 10px;
}
"""

hQline_style = """
QLineEdit {
    background-color: #F5F5F5;
    border: 1px solid #D3D3D3;
    border-radius: 5px;
    padding: 1px;
    selection-color: white; /* Color del texto seleccionado */
    selection-background-color: #543940; /* Color de fondo del texto seleccionado */
}

QLineEdit:focus {
    border: 2px solid #e1da1a; /* Cambia el borde cuando el QLineEdit está enfocado */
}
"""

wQline_style = """
QLineEdit {
    background-color: #F5F5F5;
    border: 1px solid #D3D3D3;
    border-radius: 5px;
    padding: 1px;
    selection-color: white; /* Color del texto seleccionado */
    selection-background-color: #543940; /* Color de fondo del texto seleccionado */
}

QLineEdit:focus {
    border: 2px solid #e1da1a; /* Cambia el borde cuando el QLineEdit está enfocado */
}
"""

gen_button_style = """
QPushButton {
    background-color: #e1da1a;
    color: #625e0b;
    border: 1px solid #625e0b;
    border-radius: 5px;
    padding: 5px 10px;
}

QPushButton:hover {
    background-color: #c8bf17;  /* Cambia el color cuando el mouse pasa por encima */
    border: 1px solid #625e0b;
}

QPushButton:pressed {
    background-color: #625e0b;  /* Cambia el color cuando el botón está presionado */
    border: 1px solid #e1da1a;
    color: white;
}
"""