import sys
import time
import PyQt5


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, \
    QFileDialog, QAction, QMessageBox, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import pyqtSlot, Qt, QSize, QTime, QTimer

datas = ''
i = 0
total = 0
status_zero = False
index = 0
seen = False


class App(QWidget):
    check = False

    def __init__(self):
        super().__init__()
        self.title = 'Project Theory : Finite Automata 59011212130 phisanurat.Won & 59011212092 Nopparit.Sri'
        self.left = 10
        self.top = 10
        self.width = 960
        self.height = 450

        newFont = PyQt5.QtGui.QFont("Times", 10, PyQt5.QtGui.QFont.Bold)
        newFont1 = PyQt5.QtGui.QFont("Times", 20, PyQt5.QtGui.QFont.Bold)
        newFont2 = PyQt5.QtGui.QFont("Times", 15, PyQt5.QtGui.QFont.Bold)
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
        self.button = QPushButton('Ok', self)
        self.button.setToolTip('Process String')
        self.button.move(390, 7)
        self.button.resize(100, 25)
        self.button.setStyleSheet('background-color : MediumSeaGreen')
        self.button.clicked.connect(self.get_text)
        # String Data
        self.string_data = QLabel(self)
        self.string_data.setFont(newFont2)
        self.string_data.setText('String Data  : ')
        self.string_data.move(10, 50)
        # Show String Data
        self.string = QLabel(self)
        self.string.setFont(newFont2)
        self.string.setText('                                                                                         ')
        self.string.move(160, 50)
        # Button Next
        self.button_next = QPushButton('Next', self)
        self.button_next.setToolTip('Step by step.')
        self.button_next.move(390, 45)
        self.button_next.resize(100, 25)
        self.button_next.setStyleSheet('background-color : MistyRose ')
        self.button_next.clicked.connect(self.step)

        # Button Process without step
        self.button_process = QPushButton('Result', self)
        self.button_process.setToolTip('Step by step.')
        self.button_process.move(500, 8)
        self.button_process.resize(50, 60)
        self.button_process.setStyleSheet('background-color : PaleVioletRed')
        self.button_process.clicked.connect(self.result_process)
        # Button Reset Program
        self.button_process = QPushButton('Reset', self)
        self.button_process.setToolTip('Step by step.')
        self.button_process.move(560, 8)
        self.button_process.resize(50, 60)
        self.button_process.setStyleSheet('background-color : Lavender')
        self.button_process.clicked.connect(self.clear_data)
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
        self.label_loop0.move(490, 190)
        self.pic_loop0 = QPixmap('ac_0b.png')
        self.label_loop0.setPixmap(self.pic_loop0)
        # Label self loop1
        self.label_loop1 = QLabel(self)
        self.label_loop1.resize(250, 97)
        self.label_loop1.move(510, 190)
        self.pic_loop1 = QPixmap('ac_1b.png')
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
        # todo to day
        # Label Start node self
        self.label_start_self = QLabel(self)
        self.label_start_self.resize(250, 100)
        self.label_start_self.move(200, 85)
        self.pic_start_self = QPixmap('ac_1b.png')
        self.label_start_self.setPixmap(self.pic_start_self)
        self.photo = QLabel(self)
        self.photo.resize(350, 300)
        self.photo.move(600, 100)
        self.pix_photo = QPixmap('an.jpg')
        self.photo.setPixmap(self.pix_photo)
        # Label node q2 -> q1 1 Black
        self.label_age211 = QLabel(self)
        self.label_age211.resize(250, 98)
        self.label_age211.move(245, 200)
        self.pic_age211 = QPixmap('a45_1b.png')
        self.label_age211.setPixmap(self.pic_age211)
        # Label  node q1 -> q2 0 Black
        self.label_age120 = QLabel(self)
        self.label_age120.resize(250, 100)
        self.label_age120.move(250, 190)
        self.pic_age120 = QPixmap('a45_0b.png')
        self.label_age120.setPixmap(self.pic_age120)
        # Arrow
        self.arrow = QLabel(self)
        self.arrow.setFont(newFont2)
        self.arrow.setText('                                                                                   ')
        self.arrow.move(160, 70)
        self.arrow.setStyleSheet('color : green')
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
        self.show()

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_text(self):
        try:
            global i
            global index
            i = 0
            # string
            global total
            global datas
            datas = self.textbox.text()
            self.string.setText(datas)
            print('Text : {} Total : {}'.format(datas, len(datas)))
            total = len(datas)
            # Arrow
            self.arrow.setText('                                                                                      ')

            if total == 1 and datas[0] == "0":
                print("This 0")
                self.string_status.setText('Status : Stoped..')
                self.string_status.setStyleSheet('color : red')
                self.pic_age02 = QPixmap('ar_r100.png')
                self.label_age02.setPixmap(self.pic_age02)
                self.string_result.setText("This 0 Programe Stop ..")
                self.string_result.setStyleSheet('color : red')
                self.process_stop()
                self.no()

        except:
            print('Empty String')

    def step(self):
        global total
        global i
        global status_zero
        global index
        global seen
        try:
            slide = i
            self.arrow.setText('_' * slide + '^')
            print('i : {} Text : {} '.format(i, datas[i]))

            try:
                print('step')
                if total == 1 and datas[0] == '1':
                    self.start_with_1()
                    self.process_accept()
                    self.result_correct()
                    self.yes()

                elif total == 1 and datas[0] == '0':
                    self.start_with_0()
                    self.result_missing_1()
                    self.no()

                elif total > 1 and datas[0] == '0' and status_zero is False:
                    self.start_with_0()

                elif total > 1 and datas[0] == '1' and status_zero is False:
                    self.start_with_1()

                # todo ######################################
                if total >= 2 and i >= 1 and datas[i] == '1' and datas[i - 1] == '0' and status_zero is False:
                    self.age_node211_red()

                if total >= 2 and i >= 1 and datas[i] == '0' and datas[i - 1] == '1':
                    self.age_node120_red()

                if total > 1 and i > 0 and datas[i] == '0' and datas[i - 1] == '0' and seen is False:
                    self.result_error_00()
                    status_zero = True
                    seen = True
                    # index += 1 # Move to below

                if total > 1 and i > 0 and index > 1 and datas[i] == '0':
                    self.age_loop_last_0()

                if total > 1 and i > 0 and datas[i] == '1' and datas[i - 1] == '1' and status_zero is False:
                    self.age_self_loop_1()

                # todo with mic
                if total > 1 and datas[i] == '0' and seen is True and index == 1:
                    self.result_error_00()
                    self.age_loop_last_0()
                    self.no()
                # todo Start Final State not self loop
                if i == total - 1 and datas[i] == '1' and status_zero is False:
                    self.process_accept()
                    self.result_correct()
                    self.yes()
                # if i == total - 1 and datas[i] == '0' and status_zero is False:
                #     print('NOT LOOP 0')
                #     self.result_missing_1()
                #     self.no()
                #     self.button_close()
                if i == total - 1 and datas[i] == '0':
                    print('NOT LOOP 0')
                    self.result_missing_1()
                    self.no()
                    self.button_close()
                # todo End Final State not self loop
                # todo self loop
                if i == total - 1 and datas[i] == '0' and status_zero is True and index >= 1:
                    print('Last loop 0')
                    self.result_missing_1()
                    self.age_loop_last_0()
                    self.no()
                    self.button_next.setEnabled(False)
                # todo before Last 1
                if i > 1 and datas[i] == '1' and status_zero is True and index >= 1:
                    print('Last loop 1')
                    self.result_error_00()
                    self.age_loop_last_1()
                    self.no()
                # todo Last 1
                if i == total - 1 and datas[i] == '1' and status_zero is True and index >= 1:
                    print('Last loop 1')
                    self.result_error_00()
                    self.age_loop_last_1()
                    self.no()
                    self.button_next.setEnabled(False)

                if status_zero is True:
                    index += 1
                else:
                    print('NOT TO DO')

                print('status_zero : {} index {}'.format(status_zero, index))
            except:
                print(" Step Error... ")
            i += 1
        except:
            print('Stop pls :( ')

    def result_process(self):
        global total
        data = self.textbox.text()
        print(data, 'type : ', type(data), 'Total : ', total)
        try:
            if total == 1 and data[0] == "0":
                print("This 0")
                self.result_missing_1()
                
            for semi in range(len(data) - 1):
                print(data[semi], " ", data[semi + 1])
                if data[semi] == "0" and data[semi + 1] == "0":
                    print("OMG!! Teacher X We found Data has is 00")
                    self.string_result.setText("OMG!! Teacher X We found Data has is 00")
                    self.string_result.setStyleSheet('color : red')
                    self.data_has_00()
                    self.no()
                    self.button_next.setEnabled(False)
                    self.check = True
                    break
                
            if total > 1 and data[-1] == "0":
                print("Data not found 1")                
                self.result_missing_1()
                self.process_stop()
                self.no()

            if total > 1 and data[-1] == "1" and self.check is False:
                print("Correct !")
                self.string_result.setText("Correct !")
                self.string_result.setStyleSheet('color : green')
                self.result_correct()
                self.yes()
        except:
            print(" String Data empty or Somethings Error... ")
##            self.string_result.setText("String Data empty or Somethings Error...")
##            self.string_result.setStyleSheet('color : red')

    def set_fa(self):
        print('Reset FA')
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
        self.pic_loop0 = QPixmap('ac_0b.png')
        self.label_loop0.setPixmap(self.pic_loop0)
        # Label self loop1
        self.pic_loop1 = QPixmap('ac_1b.png')
        self.label_loop1.setPixmap(self.pic_loop1)
        # Label age1 node q0 -> q1
        self.pic_age01 = QPixmap('ar_b50.png')
        self.label_age01.setPixmap(self.pic_age01)
        # todo
        # self loop
        self.pic_start_self = QPixmap('ac_1b.png')
        self.label_start_self.setPixmap(self.pic_start_self)
        # photo answer
        self.pix_photo = QPixmap('an.jpg')
        self.photo.setPixmap(self.pix_photo)
        # Label node q2 -> q1 1 Black
        self.pic_age211 = QPixmap('a45_1b.png')
        self.label_age211.setPixmap(self.pic_age211)
        # Label  node q2 -> q1 0 Black
        self.pic_age120 = QPixmap('a45_0b.png')
        self.label_age120.setPixmap(self.pic_age120)

        # Last Node
        self.pic_loop0 = QPixmap('ac_0b.png')
        self.label_loop0.setPixmap(self.pic_loop0)
        # Label self loop1
        self.pic_loop1 = QPixmap('ac_1b.png')
        self.label_loop1.setPixmap(self.pic_loop1)

        self.button_next.setEnabled(True)
        return self

    def clear_data(self):
        global datas
        global i
        global status_zero
        global index
        global seen
        index = 0
        datas = ''
        seen = False
        i = 0
        status_zero = False
        self.textbox.setText('')
        self.string.setText('                                                                                         ')
        self.arrow.setText('                                                                                   ')
        self.set_fa()
        print('Clear Data.')

    def process_stop(self):
        print('process_stop')
        self.string_status.setText('Status : Stoped..')
        self.string_status.setStyleSheet('color : red')

    def process_accept(self):
        print('process_accept')
        self.string_status.setText('Status : Accept')
        self.string_status.setStyleSheet('color : green')

    def result_error_00(self):
        print("Data has is 00")
        self.set_fa()
        self.pic_age23 = QPixmap('ar_r100.png')
        self.label_age23.setPixmap(self.pic_age23)
        self.string_result.setText("Data has 00")
        self.string_result.setStyleSheet('color : red')
        self.process_stop()
        self.no()

    def result_error_not_found_01(self):
        print('result_error_not_found_01')
        self.string_result.setText("Data not found 1")
        self.string_result.setStyleSheet('color : red')
        self.process_stop()
        self.no()

    def result_missing_1(self):
        print("result_missing_1")
        self.string_result.setText("Data Missing 1")
        self.string_result.setStyleSheet('color : red')
        self.process_stop()
        self.no()

    def result_correct(self):
        print("result_correct")
        self.string_result.setText("Correct Smart Input")
        self.string_result.setStyleSheet('color : green')
        self.process_accept()
        self.yes()

    def start_with_0(self):
        self.set_fa()
        print('start_with_0')
        self.pic_age02 = QPixmap('ar_r100.png')
        self.label_age02.setPixmap(self.pic_age02)

    def start_with_1(self):
        print('start_with_1')
        self.pic_age01 = QPixmap('ar_r50.png')
        self.label_age01.setPixmap(self.pic_age01)

    def yes(self):
        print('Yes')
        self.pix_photo = QPixmap('yes.jpg')
        self.photo.setPixmap(self.pix_photo)
        self.button_next.setEnabled(False)

    def no(self):
        print('No')
        self.pix_photo = QPixmap('no.jpg')
        self.photo.setPixmap(self.pix_photo)
        # self.button_next.setEnabled(False)

    def age_node211_red(self):
        print('age_node211_red')
        self.set_fa()
        self.pic_age211 = QPixmap('a45_1r.png')
        self.label_age211.setPixmap(self.pic_age211)

    def age_node120_red(self):
        print('age_node120_red')
        self.set_fa()
        self.pic_age120 = QPixmap('a45_0r.png')
        self.label_age120.setPixmap(self.pic_age120)

    def age_self_loop_1(self):
        print('age_self_loop_1')
        self.set_fa()
        self.pic_start_self = QPixmap('ac_1r.png')
        self.label_start_self.setPixmap(self.pic_start_self)

    def age_loop_last_0(self):
        print('age_loop_last_0')
        # Label self loop0
        self.set_fa()
        self.pic_loop0 = QPixmap('ac_0r.png')
        self.label_loop0.setPixmap(self.pic_loop0)
        self.data_has_00()

    def age_loop_last_1(self):
        # Label self loop1
        print('age_loop_last_1')
        self.set_fa()
        self.pic_loop1 = QPixmap('ac_1r.png')
        self.label_loop1.setPixmap(self.pic_loop1)
        self.data_has_00()

    def data_has_00(self):
        print('data_has_00')
        self.string_result.setText("Data has 00")
        self.string_result.setStyleSheet('color : red')
        self.process_stop()
        self.no()

    def button_close(self):
        print('button_close')
        self.button_next.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
