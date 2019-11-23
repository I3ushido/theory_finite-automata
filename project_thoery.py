import sys
import time

import PyQt5
import cv2

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, \
    QFileDialog, QAction, QMessageBox, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import pyqtSlot, Qt, QSize, QTime, QTimer

datas = ''
i = 0
total = 0


class App(QWidget):
    check = False

    def __init__(self):
        super().__init__()
        self.title = 'Theory'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 450

        newFont = PyQt5.QtGui.QFont("Times", 10, PyQt5.QtGui.QFont.Bold)
        newFont1 = PyQt5.QtGui.QFont("Times", 20, PyQt5.QtGui.QFont.Bold)
        # Input
        self.label_type = QLabel(self)
        self.label_type.setFont(newFont)
        self.label_type.setText('Input String :')
        self.label_type.move(10, 10)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(105, 7)
        self.textbox.resize(280, 25)
        # Button
        button = QPushButton('Ok', self)
        button.setToolTip('Process String')
        button.move(390, 7)
        button.resize(100, 25)
        button.clicked.connect(self.get_text)

        # String Data
        self.string_data = QLabel(self)
        self.string_data.setFont(newFont)
        self.string_data.setText('String Data  : ')
        self.string_data.move(10, 50)

        # Show String Data
        self.string = QLabel(self)
        self.string.setFont(newFont)
        self.string.setText('                                                                                         ')
        self.string.move(110, 50)

        # Button Next
        button_next = QPushButton('Next', self)
        button_next.setToolTip('Step by step.')
        button_next.move(390, 45)
        button_next.resize(100, 25)
        button_next.clicked.connect(self.step)

        # Button Process without step
        button_process = QPushButton('Result', self)
        button_process.setToolTip('Step by step.')
        button_process.move(500, 8)
        button_process.resize(50, 60)
        button_process.clicked.connect(self.result_process)

        # Button Reset Program
        button_process = QPushButton('Reset', self)
        button_process.setToolTip('Step by step.')
        button_process.move(560, 8)
        button_process.resize(50, 60)
        button_process.clicked.connect(self.clear_data)

        # Label Answer
        self.string_answer = QLabel(self)
        self.string_answer.setFont(newFont)
        self.string_answer.setText('Answer : ')
        self.string_answer.move(10, 400)

        # Show Result
        self.string_result = QLabel(self)
        self.string_result.setFont(newFont)
        self.string_result.setText('Answer Form Codex                                           ')
        self.string_result.move(100, 400)

        # Show Status
        self.string_status = QLabel(self)
        self.string_status.setFont(newFont1)
        self.string_status.setText('Status : Running..')
        self.string_status.move(690, 15)
        self.string_status.setStyleSheet('color : green')

        # Label Start node
        self.label_start_node = QLabel(self)
        self.label_start_node.resize(250, 100)
        self.label_start_node.move(100, 250)
        self.pic_start_node = QPixmap('n_q0.png')
        self.label_start_node.setPixmap(self.pic_start_node)

        # Label q1 node
        self.label_node = QLabel(self)
        self.label_node.resize(250, 100)
        self.label_node.move(200, 150)
        self.pic_node = QPixmap('n_q1.png')
        self.label_node.setPixmap(self.pic_node)

        # Label q2 node
        self.label_node2 = QLabel(self)
        self.label_node2.resize(250, 100)
        self.label_node2.move(300, 250)
        self.pic_node2 = QPixmap('n_q2.png')
        self.label_node2.setPixmap(self.pic_node2)

        # Label q3 node
        self.label_node3 = QLabel(self)
        self.label_node3.resize(250, 100)
        self.label_node3.move(500, 250)
        self.pic_node3 = QPixmap('n_q3.png')
        self.label_node3.setPixmap(self.pic_node3)

        # Label Start Line
        self.label_line = QLabel(self)
        self.label_line.resize(250, 100)
        self.label_line.move(-145, 250)
        self.pic_line = QPixmap('Arrow_black1.png')
        self.label_line.setPixmap(self.pic_line)

        # Label age1 node q0 -> q2
        self.label_age02 = QLabel(self)
        self.label_age02.resize(250, 100)
        self.label_age02.move(158, 250)
        self.pic_age02 = QPixmap('ar_b150.png')
        self.label_age02.setPixmap(self.pic_age02)

        # Label age1 node q2 -> q3
        self.label_age23 = QLabel(self)
        self.label_age23.resize(250, 100)
        self.label_age23.move(358, 250)
        self.pic_age23 = QPixmap('ar_b150.png')
        self.label_age23.setPixmap(self.pic_age23)

        # Label self loop0
        self.label_loop0 = QLabel(self)
        self.label_loop0.resize(250, 97)
        self.label_loop0.move(490, 200)
        self.pic_loop0 = QPixmap('ac0.png')
        self.label_loop0.setPixmap(self.pic_loop0)

        # Label self loop1
        self.label_loop1 = QLabel(self)
        self.label_loop1.resize(250, 97)
        self.label_loop1.move(510, 200)
        self.pic_loop1 = QPixmap('ac1.png')
        self.label_loop1.setPixmap(self.pic_loop1)

        # Label age1 node q0 -> q1  Emtpy
        self.label_age01_reset = QLabel(self)
        self.label_age01_reset.resize(250, 98)
        self.label_age01_reset.move(130, 200)
        self.pic_age01_reset = QPixmap()
        self.label_age01_reset.setPixmap(self.pic_age01_reset)

        # Label age1 node q0 -> q1
        self.label_age01 = QLabel(self)
        self.label_age01.resize(250, 98)
        self.label_age01.move(130, 200)
        self.pic_age01 = QPixmap('ar_b50.png')
        self.label_age01.setPixmap(self.pic_age01)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_text(self):
        try:
            global i
            i = 0
            # string
            global total
            global datas
            datas = self.textbox.text()
            self.string.setText(datas)
            print('Text : {} Total : {}'.format(datas, len(datas)))
            total = len(datas)
            if total == 1 and datas[0] == "0":
                print("This 0")
                self.string_status.setText('Status : Stoped..')
                self.string_status.setStyleSheet('color : red')
                self.pic_age02 = QPixmap('ar_r100.png')
                self.label_age02.setPixmap(self.pic_age02)
                self.string_result.setText("This 0 Programe Stop ..")
                self.string_result.setStyleSheet('color : red')
                self.process_stop()

        except:
            print('Empty String')

    def step(self):
        global total
        global i
        print('Datas : ', datas[i])
        val = int(total)
        try:
            if total >= 2 and i == 0:
                self.pic_age02 = QPixmap('ar_r100.png')
                self.label_age02.setPixmap(self.pic_age02)

            if total >= 2 and datas[i] == "0" and datas[i - 1] == "0":
                print("Data has is 00")
                self.set_fa()
                self.pic_age23 = QPixmap('ar_r100.png')
                self.label_age23.setPixmap(self.pic_age23)
                self.result_00()


        except:
            print(" Step Error... ")

        # if i == 1:
        #
        #     self.pic_age01 = QPixmap('ar_r50.png')
        #     self.label_age01.setPixmap(self.pic_age01)
        # if i == 2:
        #     self.set_fa()
        #     # self.initUI()
        #     self.pic_age01 = QPixmap('ar_b50.png')
        #     self.label_age01.setPixmap(self.pic_age01)
        #
        # if i == 4:
        #
        #     self.pic_age01 = QPixmap('ar_r50.png')
        #     self.label_age01.setPixmap(self.pic_age01)

        print('I : {}'.format(i))
        i += 1

    def result_process(self):
        global total
        data = self.textbox.text()
        print(data, 'type : ', type(data), 'Total : ', total)
        try:
            if total == 1 and data[0] == "0":
                print("This 0")
                # time.sleep(0.5)
            for semi in range(len(data) - 1):
                print(data[semi], " ", data[semi + 1])
                # time.sleep(0.5)
                if data[semi] == "0" and data[semi + 1] == "0":
                    print("OMG!! Teacher X We found Data has is 00")
                    self.string_result.setText("OMG!! Teacher X We found Data has is 00")
                    self.string_result.setStyleSheet('color : red')
                    self.check = True
                    break

            if data[-1] != "1":
                print("Data not found 1")
                self.result_error_not_found_1()

            if data[-1] == "1" and self.check == False:
                print("Correct !")
                self.string_result.setText("Correct !")
                self.string_result.setStyleSheet('color : green')

        except:
            print(" String Data empty or Somethings Error... ")
            self.string_result.setText("String Data empty or Somethings Error...")
            self.string_result.setStyleSheet('color : red')

    def set_fa(self):
        print('Reset...')
        newFont = PyQt5.QtGui.QFont("Times", 10, PyQt5.QtGui.QFont.Bold)
        newFont1 = PyQt5.QtGui.QFont("Times", 20, PyQt5.QtGui.QFont.Bold)

        # Label Answer
        self.string_answer.setText('Answer : ')

        # Show Result
        self.string_result.setText('Answer Form Codex                                           ')
        self.string_result.setStyleSheet('color : black')

        # Show Status
        self.string_status.setFont(newFont1)
        self.string_status.setText('Status : Running..')
        self.string_status.setStyleSheet('color : green')

        # Label Start node
        self.pic_start_node = QPixmap('n_q0.png')
        self.label_start_node.setPixmap(self.pic_start_node)

        # Label q1 node
        self.pic_node = QPixmap('n_q1.png')
        self.label_node.setPixmap(self.pic_node)

        # Label q2 node
        self.pic_node2 = QPixmap('n_q2.png')
        self.label_node2.setPixmap(self.pic_node2)

        # Label q3 node
        self.pic_node3 = QPixmap('n_q3.png')
        self.label_node3.setPixmap(self.pic_node3)

        # Label age1 node q0 -> q2
        self.pic_age02 = QPixmap('ar_b150.png')
        self.label_age02.setPixmap(self.pic_age02)

        # Label age1 node q2 -> q3
        self.pic_age23 = QPixmap('ar_b150.png')
        self.label_age23.setPixmap(self.pic_age23)

        # Label self loop0
        self.pic_loop0 = QPixmap('ac0.png')
        self.label_loop0.setPixmap(self.pic_loop0)

        # Label self loop1
        self.pic_loop1 = QPixmap('ac1.png')
        self.label_loop1.setPixmap(self.pic_loop1)

        # Label age1 node q0 -> q1
        self.pic_age01 = QPixmap('ar_b50.png')
        self.label_age01.setPixmap(self.pic_age01)

        # # String in text box
        # self.textbox.setText('')
        # # Show String Data
        # self.string.setText('')

        return self

    def clear_data(self):
        global datas
        global i
        datas = ''
        i = 0
        self.set_fa()
        print('Clear Data.')

    def process_stop(self):
        self.string_status.setText('Status : Stoped..')
        self.string_status.setStyleSheet('color : red')

    def result_error_00(self):
        self.string_result.setText("Data has 00")
        self.string_result.setStyleSheet('color : red')
        self.process_stop()

    def result_error_not_found_01(self):
        self.string_result.setText("Data not found 1")
        self.string_result.setStyleSheet('color : red')
        self.process_stop()

    def result_correct(self):
        self.string_result.setText("Correct Smart Input")
        self.string_result.setStyleSheet('color : green')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
