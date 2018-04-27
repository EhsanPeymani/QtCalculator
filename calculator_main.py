import decimal

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from UserInterface.ui_calculator import Ui_calculator
from decimal import Decimal

# to make sure that we do not directly convert float to decimal
decimal.getcontext().traps[decimal.FloatOperation] = True


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class CalculatorUi(QMainWindow, Ui_calculator):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.input = ''
        self.result = Decimal('0')
        self.current_operation = ' '
        self.selected_operator = ''

        self.operation_plainTextEdit.setReadOnly(True)
        self.add_system_tray()
        self.setWindowFlags(self.windowFlags() |
                            Qt.WindowMinimizeButtonHint |
                            Qt.WindowSystemMenuHint)

        self.set_shortkeys()

        self.present_result()

        self.numeric_signals()
        self.operator_signals()
        self.c_signals()

    def changeEvent(self, event: QEvent):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                if not self.isHidden():
                    event.ignore()
                    # self.setWindowState(Qt.WindowNoState)
                    print('it does not work as intended')

    def close(self):
        self.systray.hide()
        self.close()

    def add_system_tray(self):
        # systray_icon = QIcon(':/icons/calculator.png')
        systray_icon = QIcon(':/calculator.png')
        systray = QSystemTrayIcon(systray_icon, self)
        menu = QMenu()
        restore = QAction('Restore', self)
        close = QAction('Close', self)
        menu.addActions([restore, close])
        systray.setContextMenu(menu)

        close.triggered.connect(self.close)
        restore.triggered.connect(lambda: self.showNormal())

        self.systray = systray
        self.systray.show()
        self.systray.showMessage('eCalculator', 'eCalculator is running ...\nDouble click to minimize the calculator\n'
                                                'to system tray and vice versa.',
                                 icon=QSystemTrayIcon.Information, msecs=2000)

        self.systray.activated.connect(lambda reason: self.on_system_tray_activated(reason))

        return systray

    def on_system_tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.setVisible(True)
                self.systray.showMessage('eCalculator', 'eCalculator becomes visible.',
                                 icon=QSystemTrayIcon.Information, msecs=2000)
            else:
                self.setVisible(False)
                self.systray.showMessage('eCalculator', 'eCalculator is in the system tray.',
                                 icon=QSystemTrayIcon.Information, msecs=2000)

    def set_shortkeys(self):
        self.pushButton_0.setShortcut(QKeySequence('Numpad+0'))
        self.pushButton_1.setShortcut(QKeySequence('Numpad+1'))
        self.pushButton_2.setShortcut(QKeySequence('Numpad+2'))
        self.pushButton_3.setShortcut(QKeySequence('Numpad+3'))
        self.pushButton_4.setShortcut(QKeySequence('Numpad+4'))
        self.pushButton_5.setShortcut(QKeySequence('Numpad+5'))
        self.pushButton_6.setShortcut(QKeySequence('Numpad+6'))
        self.pushButton_7.setShortcut(QKeySequence('Numpad+7'))
        self.pushButton_8.setShortcut(QKeySequence('Numpad+8'))
        self.pushButton_9.setShortcut(QKeySequence('Numpad+9'))
        self.pushButton_sum.setShortcut(QKeySequence('Numpad++'))
        self.pushButton_subtract.setShortcut(QKeySequence('Numpad+-'))
        self.pushButton_multiply.setShortcut(QKeySequence('Numpad+*'))
        self.pushButton_divide.setShortcut(QKeySequence('Numpad+/'))
        self.pushButton_decimal_point.setShortcut(QKeySequence('Numpad+.'))
        self.pushButton_c.setShortcut(QKeySequence('Delete'))
        self.pushButton_ce.setShortcut(QKeySequence('Esc'))
        self.pushButton_clear.setShortcut(QKeySequence('Backspace'))
        self.pushButton_equal.setShortcut(QKeySequence('Numpad+Enter'))
        self.pushButton_squared.setShortcut(QKeySequence('Alt+s'))
        self.pushButton_sqrt.setShortcut(QKeySequence('Ctrl+s'))
        self.pushButton_reciproc.setShortcut(QKeySequence('Ctrl+r'))
        self.pushButton_negate.setShortcut(QKeySequence('Ctrl+n'))

        self.actionAbout_Calculator.triggered.connect(self.about_calculator)
        self.actionView_Help.triggered.connect(self.view_Help)

    def view_Help(self):
        QMessageBox.aboutQt(self.centralwidget, 'About Qt')

    def about_calculator(self):
        message = 'Developed by Ehsan Peymani.\n\n' \
                  'This is a home project to lean more about Qt, PyQt4 and Python.\n\n' \
                  'email: ehsan.peymani.f@gmail.com\n' \
                  'phone: +47 942 24 458'
        QMessageBox.about(self.centralwidget, 'About eCalculator', message)

    def numeric_signals(self):
        self.pushButton_0.clicked.connect(self.get_0)
        self.pushButton_1.clicked.connect(self.get_1)
        self.pushButton_2.clicked.connect(self.get_2)
        self.pushButton_3.clicked.connect(self.get_3)
        self.pushButton_4.clicked.connect(self.get_4)
        self.pushButton_5.clicked.connect(self.get_5)
        self.pushButton_6.clicked.connect(self.get_6)
        self.pushButton_7.clicked.connect(self.get_7)
        self.pushButton_8.clicked.connect(self.get_8)
        self.pushButton_9.clicked.connect(self.get_9)
        self.pushButton_decimal_point.clicked.connect(self.decimal_point)

    def operator_signals(self):
        self.pushButton_sum.clicked.connect(self.sum)
        self.pushButton_subtract.clicked.connect(self.subtract)
        self.pushButton_multiply.clicked.connect(self.multiply)
        self.pushButton_divide.clicked.connect(self.divide)
        self.pushButton_equal.clicked.connect(self.equal)
        self.pushButton_negate.clicked.connect(self.negate)
        self.pushButton_reciproc.clicked.connect(self.reciproc)
        self.pushButton_sqrt.clicked.connect(self.squared_root)
        self.pushButton_squared.clicked.connect(self.squared)

    def c_signals(self):
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_ce.clicked.connect(self.ce)
        self.pushButton_c.clicked.connect(self.c)

    def c(self):
        '''clear all entries and result.'''
        self.result = 0.0
        self.clear_operation()
        self.present_result()

    def ce(self):
        self.input = ''
        self.update_operation_text()

    def clear(self):
        self.input = self.input[:-1]
        self.update_operation_text()

    def special_operate(self, operator):
        if self.input == '':
            self.input = self.result_textBrowser.toPlainText()
        temp_input = self.input
        if not isfloat(self.input):
            temp_input = self.result_textBrowser.toPlainText()
        try:
            if operator == 'squared':
                temp_result = Decimal(temp_input) ** 2
            elif operator == 'sqrt':
                temp_result = Decimal(temp_input).sqrt()
            elif operator == 'reciproc':
                temp_result = 1 / Decimal(temp_input)

            self.input = operator + '({})'.format(self.input)
            self.update_operation_text()
            self.present_result(message=str(temp_result))
            return True
        except ValueError:
            self.present_result('Invalid Input')
            return False

    def squared(self):
        self.special_operate('squared')

    def squared_root(self):
        self.special_operate('sqrt')

    def reciproc(self):
        self.special_operate('reciproc')

    def operate(self):
        input_float = 's'

        if isfloat(self.input):
            input_float = Decimal(self.input)
        else:
            input_float = Decimal(self.result_textBrowser.toPlainText())

        assert isinstance(input_float, Decimal), self.present_result('bad input')

        if self.selected_operator == '':
            self.result = input_float
        elif self.selected_operator == '+':
            self.result += input_float
        elif self.selected_operator == '-':
            self.result -= input_float
        elif self.selected_operator == '/':
            try:
                self.result /= input_float
            except ZeroDivisionError:
                self.present_result('cannot divide by zero')
        elif self.selected_operator == '*':
            self.result *= input_float

    def negate(self):
        if self.input == '':
            self.input = self.result_textBrowser.toPlainText()

        self.negate_input()  # 42 --> -42

    def negate_input(self):
        special_operators = ['reciproc', 'sqrt', 'squared']
        found_special = False

        for operator in special_operators:
            if self.input.find(operator) != -1:
                found_special = True
                break

        if found_special:
            new_input = '-' + self.result_textBrowser.toPlainText()
        else:
            if self.input.strip('-').isdecimal():
                new_input = str(int(self.input) * -1)
            else:
                new_input = str(Decimal(self.input) * -1)
        self.input = new_input
        self.update_operation_text()

    def validate_input(self):
        if isfloat(self.input) \
                or self.input.find('reciproc') != -1 \
                or self.input.find('sqrt') != -1:
            return True
        else:
            return False

    def do_operation(self, operator: str):
        if self.input == '' and self.current_operation == '':  # this happens after pressing =
            self.input = self.result_textBrowser.toPlainText()
            self.result = Decimal(self.input)
            self.selected_operator = operator
            self.fix_input_field(operator)
            return
        elif self.input == '' and self.current_operation != '':  # this happens when you change operator
            self.selected_operator = operator
            self.current_operation = self.current_operation[:-2] + operator + ' '
            self.operation_plainTextEdit.setPlainText(self.current_operation)
            return
        else:
            if not self.validate_input():
                return

        self.operate()

        self.selected_operator = operator
        self.fix_input_field(operator)

        self.present_result()

    def equal(self):
        if not self.validate_input():
            return

        self.operate()

        self.clear_operation()
        self.present_result()
        self.result = 0.0

    def sum(self):
        self.do_operation('+')

    def subtract(self):
        self.do_operation('-')

    def multiply(self):
        self.do_operation('*')

    def divide(self):
        self.do_operation('/')

    def clear_operation(self):
        self.input = ''
        self.current_operation = ''
        self.selected_operator = ''
        self.operation_plainTextEdit.clear()

    def fix_input_field(self, operator):
        self.current_operation += (self.input + ' ' + operator + ' ')
        self.input = ''
        self.operation_plainTextEdit.setPlainText(self.current_operation)

    def update_operation_text(self):
        self.operation_plainTextEdit.setPlainText(self.current_operation + self.input)

    def present_result(self, message=None):
        if message is None:
            message = str(self.result)

        self.result_textBrowser.setPlainText(message)

    def get_0(self):
        self.input += '0'
        self.update_operation_text()

    def get_1(self):
        self.input += '1'
        self.update_operation_text()

    def get_2(self):
        self.input += '2'
        self.update_operation_text()

    def get_3(self):
        self.input += '3'
        self.update_operation_text()

    def get_4(self):
        self.input += '4'
        self.update_operation_text()

    def get_5(self):
        self.input += '5'
        self.update_operation_text()

    def get_6(self):
        self.input += '6'
        self.update_operation_text()

    def get_7(self):
        self.input += '7'
        self.update_operation_text()

    def get_8(self):
        self.input += '8'
        self.update_operation_text()

    def get_9(self):
        self.input += '9'
        self.update_operation_text()

    def decimal_point(self):
        self.input += '.'
        self.update_operation_text()



