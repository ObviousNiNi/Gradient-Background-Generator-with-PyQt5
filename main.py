import sys
from PyQt5.QtWidgets import QApplication
from gui import logic

def main():
    app = QApplication(sys.argv)
    window = logic()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
