"""
<The_King_of_Macro_v1.3> - 21.12.23.목 ??:??
* Made by Yoonmen *

[update] 구조 단순화
"""

import sys
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import os
import csv
import keyboard
import mouse
import pyautogui
import time


class KOM(QWidget) : 
    def setupUi(self, Form) : 
        # Default Setting
        _translate = QCoreApplication.translate

        Form.setFixedSize(351, 664)
        Form.setWindowTitle(_translate("Form", "The_King_of_Macro_v1.3"))

        self.title = QLabel(Form)
        self.title.setGeometry(60, 10, 241, 71)
        font = QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setText(_translate("Form", "The King of Macro"))

        self.version = QLabel(Form)
        self.version.setGeometry(10, 10, 64, 15)
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.version.setFont(font)
        self.version.setText(_translate("Form", "v1.3"))

        self.loadButton = QToolButton(Form)
        self.loadButton.setGeometry(280, 10, 61, 20)
        self.loadButton.setText(_translate("Form", "불러오기"))

        self.noticeBoard = QListWidget(Form)
        self.noticeBoard.setGeometry(20, 550, 311, 81)

        self.dev = QLabel(Form)
        self.dev.setGeometry(130, 640, 101, 16)
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.dev.setFont(font)
        self.dev.setText(_translate("Form", "by. Yoonmen"))


        # addName_group
        self.addName_group = QLabel(Form)
        self.addName_group.setGeometry(20, 70, 131, 20)
        self.addName_group.setText(_translate("Form", "<Add Macro's Name>"))


        self.addName_le = QLineEdit(Form)
        self.addName_le.setGeometry(20, 100, 251, 20)
        self.addName_le.setPlaceholderText("ex) 자동사냥")
        self.addName_le.setClearButtonEnabled(True)

        self.addName_bt = QPushButton(Form)
        self.addName_bt.setGeometry(280, 100, 51, 21)
        self.addName_bt.setText(_translate("Form", "추가"))


        # addClick_group
        self.addClick_group = QLabel(Form)
        self.addClick_group.setGeometry(20, 140, 101, 20)
        self.addClick_group.setText(_translate("Form", "<Add Click>"))

        self.addClick_cb = QComboBox(Form)
        self.addClick_cb.setGeometry(20, 170, 101, 22)

        self.addClick_lb_1 = QLabel(Form)
        self.addClick_lb_1.setGeometry(130, 170, 16, 20)
        self.addClick_lb_1.setText(_translate("Form", "에"))

        self.addClick_lb_2 = QLabel(Form)
        self.addClick_lb_2.setGeometry(210, 170, 71, 20)
        self.addClick_lb_2.setText(_translate("Form", "초 간격으로"))

        self.addClick_ds = QDoubleSpinBox(Form)
        self.addClick_ds.setGeometry(150, 170, 51, 22)
        
        self.addClick_bt = QPushButton(Form)
        self.addClick_bt.setGeometry(280, 170, 51, 21)
        self.addClick_bt.setText(_translate("Form", "클릭"))

        self.addClick_lb_3 = QLabel(Form)
        self.addClick_lb_3.setGeometry(80, 200, 191, 20)
        self.addClick_lb_3.setText(_translate("Form", "(순서에 맞게 클릭을 진행하세요.)"))

        
        # addKeyboard_group
        self.addKeyboard_group = QLabel(Form)
        self.addKeyboard_group.setGeometry(20, 240, 101, 20)
        self.addKeyboard_group.setText(_translate("Form", "<Add Keyboard>"))

        self.addKeyboard_cb = QComboBox(Form)
        self.addKeyboard_cb.setGeometry(20, 270, 101, 22)

        self.addKeyboard_lb_1 = QLabel(Form)
        self.addKeyboard_lb_1.setGeometry(130, 270, 16, 20)
        self.addKeyboard_lb_1.setText(_translate("Form", "에"))

        self.addKeyboard_ds = QDoubleSpinBox(Form)
        self.addKeyboard_ds.setGeometry(150, 270, 51, 22)

        self.addKeyboard_lb_2 = QLabel(Form)
        self.addKeyboard_lb_2.setGeometry(210, 270, 71, 20)
        self.addKeyboard_lb_2.setText(_translate("Form", "초 간격으로"))

        self.addKeyboard_bt = QPushButton(Form)
        self.addKeyboard_bt.setGeometry(280, 270, 51, 21)
        self.addKeyboard_bt.setText(_translate("Form", "입력"))

        self.addKeyboard_lb_3 = QLabel(Form)
        self.addKeyboard_lb_3.setGeometry(80, 300, 191, 20)
        self.addKeyboard_lb_3.setText(_translate("Form", "(순서에 맞게 클릭을 진행하세요.)"))

        self.addLine = QFrame(Form)
        self.addLine.setGeometry(110, 350, 118, 3)
        self.addLine.setFrameShape(QFrame.HLine)
        self.addLine.setFrameShadow(QFrame.Sunken)
        

        # deleteMacro_group
        self.deleteMacro_group = QLabel(Form)
        self.deleteMacro_group.setGeometry(20, 370, 101, 20)
        self.deleteMacro_group.setText(_translate("Form", "<Delete Macro>"))

        self.deleteMacro_cb = QComboBox(Form)
        self.deleteMacro_cb.setGeometry(20, 400, 211, 22)

        self.deleteMacro_lb_1 = QLabel(Form)
        self.deleteMacro_lb_1.setGeometry(240, 400, 41, 20)
        self.deleteMacro_lb_1.setText(_translate("Form", "을(를)"))

        self.deleteMacro_bt = QPushButton(Form)
        self.deleteMacro_bt.setGeometry(280, 400, 51, 21)
        self.deleteMacro_bt.setText(_translate("Form", "삭제"))

        self.deleteLine = QFrame(Form)
        self.deleteLine.setGeometry(110, 460, 118, 3)
        self.deleteLine.setFrameShape(QFrame.HLine)
        self.deleteLine.setFrameShadow(QFrame.Sunken)


        # startMacro_group
        self.startMacro_group = QLabel(Form)
        self.startMacro_group.setGeometry(20, 480, 101, 20)
        self.startMacro_group.setText(_translate("Form", "<Start Macro>"))

        self.startMacro_cb = QComboBox(Form)
        self.startMacro_cb.setGeometry(20, 510, 141, 22)

        self.startMacro_lb_1 = QLabel(Form)
        self.startMacro_lb_1.setGeometry(170, 510, 41, 20)
        self.startMacro_lb_1.setText(_translate("Form", "을(를)"))

        self.startMacro_sb = QSpinBox(Form)
        self.startMacro_sb.setGeometry(210, 510, 42, 22)

        self.startMacro_lb_2 = QLabel(Form)
        self.startMacro_lb_2.setGeometry(260, 510, 16, 20)
        self.startMacro_lb_2.setText(_translate("Form", "번"))

        self.startMacro_bt = QPushButton(Form)
        self.startMacro_bt.setGeometry(280, 510, 51, 21)
        self.startMacro_bt.setText(_translate("Form", "실행"))

        QMetaObject.connectSlotsByName(Form)



if __name__ == '__main__' : 
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = KOM()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
