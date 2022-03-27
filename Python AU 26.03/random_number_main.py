import random
import sys
import time
import asyncio
from webbrowser import open
from random_number import Ui_MainWindow
from random import randint
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class AppWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.button1.clicked.connect(self.randomize)
        self.button2.clicked.connect(self.antarctica)
        self.button3.clicked.connect(lambda: open('https://www.timeanddate.com/weather/antarctica/south-pole'))


    def randomize(self):
        n = randint(-500, 500)
        time.sleep(0.5)
        addition = ["ain't it beautiful?", 'do you think toddlers know this one?', 'the chance of getting that is about 0.001!', "I could've randomed a bigger one hehe", "that's like my granny's age"]
        qtw.QMessageBox.information(self, 'Random Number', f'Your number is {n}, {addition[n % 5]}')

    def antarctica(self):
        time.sleep(1.5)
        qtw.QMessageBox.information(self, 'Temperature', 'Somewhere between -90°C and -20°C!')


def main():

    if __name__ == "__main__":
        app = qtw.QApplication(sys.argv)
        app.setStyle('Fusion')
        app.setStyleSheet(" background-image: url(back.jpg);")
        window = AppWindow()
        window.show()


        sys.exit(app.exec())



main()