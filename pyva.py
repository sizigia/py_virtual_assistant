import os
import sys
import wolframalpha
import wikipedia
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from dotenv import load_dotenv
load_dotenv()


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Python Virtual Assistant")
        self.resize(550, 120)

        label = QLabel(
            "Hello, I am PyVA, the Python Virtual Assistant. How can I help you?")
        label.setAlignment(Qt.AlignLeft)
        label.setIndent(20)

        self.setCentralWidget(label)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(500, 40)

        self.button = QPushButton('Now search!', self)
        self.button.move(20, 80)
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        raw_input = self.textbox.text()
        try:
            # wolframalpha
            app_id = os.getenv('WOLFRAM_ID')
            client = wolframalpha.Client(app_id)
            result = client.query(raw_input)
            answer1 = next(result.results).text
            QMessageBox.question(self, 'Results:',
                                 f"You asked {raw_input}, apparently the answer is... " + answer1, QMessageBox.Ok, QMessageBox.Ok)
        except StopIteration:
            # wikipedia
            wikipedia.set_lang("ES")
            answer2 = wikipedia.summary(raw_input, sentences=3)
            QMessageBox.question(self, 'Results:',
                                 f"You asked {raw_input}, apparently the answer is... " + answer2, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
