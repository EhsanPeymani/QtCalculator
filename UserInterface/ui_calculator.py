# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName(_fromUtf8("calculator"))
        calculator.resize(277, 413)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calculator.sizePolicy().hasHeightForWidth())
        calculator.setSizePolicy(sizePolicy)
        calculator.setMinimumSize(QtCore.QSize(277, 413))
        calculator.setMaximumSize(QtCore.QSize(277, 413))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/calculator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        calculator.setWindowIcon(icon)
        calculator.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(calculator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 190, 259, 192))
        self.frame.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"    border-radius: 4px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 0, 0);\n"
"    background-color: rgb(225, 203, 255);\n"
"}\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_9 = QtGui.QPushButton(self.frame)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_divide = QtGui.QPushButton(self.frame)
        self.pushButton_divide.setObjectName(_fromUtf8("pushButton_divide"))
        self.gridLayout.addWidget(self.pushButton_divide, 1, 3, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.frame)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_sqrt = QtGui.QPushButton(self.frame)
        self.pushButton_sqrt.setStyleSheet(_fromUtf8(""))
        self.pushButton_sqrt.setObjectName(_fromUtf8("pushButton_sqrt"))
        self.gridLayout.addWidget(self.pushButton_sqrt, 0, 4, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.frame)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_sum = QtGui.QPushButton(self.frame)
        self.pushButton_sum.setObjectName(_fromUtf8("pushButton_sum"))
        self.gridLayout.addWidget(self.pushButton_sum, 4, 3, 1, 1)
        self.pushButton_clear = QtGui.QPushButton(self.frame)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.gridLayout.addWidget(self.pushButton_clear, 0, 0, 1, 1)
        self.pushButton_reciproc = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_reciproc.setFont(font)
        self.pushButton_reciproc.setObjectName(_fromUtf8("pushButton_reciproc"))
        self.gridLayout.addWidget(self.pushButton_reciproc, 2, 4, 1, 1)
        self.pushButton_multiply = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        self.pushButton_multiply.setFont(font)
        self.pushButton_multiply.setObjectName(_fromUtf8("pushButton_multiply"))
        self.gridLayout.addWidget(self.pushButton_multiply, 2, 3, 1, 1)
        self.pushButton_1 = QtGui.QPushButton(self.frame)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_subtract = QtGui.QPushButton(self.frame)
        self.pushButton_subtract.setObjectName(_fromUtf8("pushButton_subtract"))
        self.gridLayout.addWidget(self.pushButton_subtract, 3, 3, 1, 1)
        self.pushButton_decimal_point = QtGui.QPushButton(self.frame)
        self.pushButton_decimal_point.setObjectName(_fromUtf8("pushButton_decimal_point"))
        self.gridLayout.addWidget(self.pushButton_decimal_point, 4, 2, 1, 1)
        self.pushButton_ce = QtGui.QPushButton(self.frame)
        self.pushButton_ce.setObjectName(_fromUtf8("pushButton_ce"))
        self.gridLayout.addWidget(self.pushButton_ce, 0, 1, 1, 1)
        self.pushButton_negate = QtGui.QPushButton(self.frame)
        self.pushButton_negate.setObjectName(_fromUtf8("pushButton_negate"))
        self.gridLayout.addWidget(self.pushButton_negate, 0, 3, 1, 1)
        self.pushButton_c = QtGui.QPushButton(self.frame)
        self.pushButton_c.setObjectName(_fromUtf8("pushButton_c"))
        self.gridLayout.addWidget(self.pushButton_c, 0, 2, 1, 1)
        self.pushButton_0 = QtGui.QPushButton(self.frame)
        self.pushButton_0.setObjectName(_fromUtf8("pushButton_0"))
        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 2)
        self.pushButton_squared = QtGui.QPushButton(self.frame)
        self.pushButton_squared.setObjectName(_fromUtf8("pushButton_squared"))
        self.gridLayout.addWidget(self.pushButton_squared, 1, 4, 1, 1)
        self.pushButton_equal = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_equal.sizePolicy().hasHeightForWidth())
        self.pushButton_equal.setSizePolicy(sizePolicy)
        self.pushButton_equal.setObjectName(_fromUtf8("pushButton_equal"))
        self.gridLayout.addWidget(self.pushButton_equal, 3, 4, 2, 1)
        self.result_textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.result_textBrowser.setGeometry(QtCore.QRect(11, 119, 259, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.result_textBrowser.setFont(font)
        self.result_textBrowser.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.result_textBrowser.setObjectName(_fromUtf8("result_textBrowser"))
        self.operation_plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.operation_plainTextEdit.setGeometry(QtCore.QRect(11, 11, 259, 101))
        self.operation_plainTextEdit.setReadOnly(True)
        self.operation_plainTextEdit.setObjectName(_fromUtf8("operation_plainTextEdit"))
        calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 277, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        calculator.setMenuBar(self.menubar)
        self.actionView_Help = QtGui.QAction(calculator)
        self.actionView_Help.setObjectName(_fromUtf8("actionView_Help"))
        self.actionAbout_Calculator = QtGui.QAction(calculator)
        self.actionAbout_Calculator.setObjectName(_fromUtf8("actionAbout_Calculator"))
        self.actionTo_be_completed = QtGui.QAction(calculator)
        self.actionTo_be_completed.setObjectName(_fromUtf8("actionTo_be_completed"))
        self.actionTo_be_completed_2 = QtGui.QAction(calculator)
        self.actionTo_be_completed_2.setObjectName(_fromUtf8("actionTo_be_completed_2"))
        self.menuView.addAction(self.actionTo_be_completed)
        self.menuEdit.addAction(self.actionTo_be_completed_2)
        self.menuHelp.addAction(self.actionView_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Calculator)
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

    def retranslateUi(self, calculator):
        calculator.setWindowTitle(_translate("calculator", "eCalculator", None))
        self.pushButton_9.setText(_translate("calculator", "9", None))
        self.pushButton_4.setText(_translate("calculator", "4", None))
        self.pushButton_5.setText(_translate("calculator", "5", None))
        self.pushButton_6.setText(_translate("calculator", "6", None))
        self.pushButton_divide.setText(_translate("calculator", "/", None))
        self.pushButton_7.setText(_translate("calculator", "7", None))
        self.pushButton_sqrt.setText(_translate("calculator", "sqrt", None))
        self.pushButton_8.setText(_translate("calculator", "8", None))
        self.pushButton_sum.setText(_translate("calculator", "+", None))
        self.pushButton_clear.setText(_translate("calculator", "Clear", None))
        self.pushButton_reciproc.setText(_translate("calculator", "1/x", None))
        self.pushButton_multiply.setText(_translate("calculator", "*", None))
        self.pushButton_1.setText(_translate("calculator", "1", None))
        self.pushButton_2.setText(_translate("calculator", "2", None))
        self.pushButton_3.setText(_translate("calculator", "3", None))
        self.pushButton_subtract.setText(_translate("calculator", "-", None))
        self.pushButton_decimal_point.setText(_translate("calculator", ".", None))
        self.pushButton_ce.setText(_translate("calculator", "CE", None))
        self.pushButton_negate.setText(_translate("calculator", "neg", None))
        self.pushButton_c.setText(_translate("calculator", "C", None))
        self.pushButton_0.setText(_translate("calculator", "0", None))
        self.pushButton_squared.setText(_translate("calculator", "sq", None))
        self.pushButton_equal.setText(_translate("calculator", "=", None))
        self.menuView.setTitle(_translate("calculator", "View", None))
        self.menuEdit.setTitle(_translate("calculator", "Edit", None))
        self.menuHelp.setTitle(_translate("calculator", "Help", None))
        self.actionView_Help.setText(_translate("calculator", "View Help", None))
        self.actionAbout_Calculator.setText(_translate("calculator", "About Calculator", None))
        self.actionTo_be_completed.setText(_translate("calculator", "To be completed", None))
        self.actionTo_be_completed_2.setText(_translate("calculator", "To be completed", None))

import UserInterface.icons_rc
