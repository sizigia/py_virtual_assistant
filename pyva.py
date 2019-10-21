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


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

while True:
    raw_input = input("Whatcha wanna know: ")
    try:
        # wolframalpha
        app_id = os.getenv('WOLFRAM_ID')
        client = wolframalpha.Client(app_id)
        result = client.query(raw_input)
        answer1 = next(result.results).text
        print(answer1, '\n')
    except:
        # wikipedia
        lang = input("Which language do you feel comfortable with? ")[
            :2].upper()
        if lang == "":
            wikipedia.set_lang("ES")
        else:
            wikipedia.set_lang(lang)
        answer2 = wikipedia.summary(raw_input, sentences=3)
        print(answer2, '\n')
