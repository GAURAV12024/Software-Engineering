import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 280, 370)

        self.initUI()

    def initUI(self):
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 10, 260, 40)

        buttons = [
            ('7', 10, 60), ('8', 80, 60), ('9', 150, 60), ('/', 220, 60),
            ('4', 10, 110), ('5', 80, 110), ('6', 150, 110), ('*', 220, 110),
            ('1', 10, 160), ('2', 80, 160), ('3', 150, 160), ('-', 220, 160),
            ('0', 10, 210), ('.', 80, 210), ('=', 150, 210), ('+', 220, 210),
            ('C', 150, 260)  # Added the 'C' button
        ]

        for btn_text, x, y in buttons:
            button = QPushButton(btn_text, self)
            button.setGeometry(x, y, 60, 40)
            button.clicked.connect(self.on_click)

    def on_click(self):
        button_text = self.sender().text()

        if button_text == '=':
            try:
                result = eval(self.input_field.text())
                self.input_field.setText(str(result))
            except Exception as e:
                self.input_field.setText('Error')
        elif button_text == 'C':
            self.input_field.clear()
        else:
            self.input_field.setText(self.input_field.text() + button_text)

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
