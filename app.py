from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from calculator_main import CalculatorUi
import time

app = QApplication(sys.argv)
form = CalculatorUi()

# splash screen
splash_image = QPixmap(':/calculator.png').scaled(400, 400)
splash = QSplashScreen(splash_image)
splash.show()

# emulating delay in start up
import time
time.sleep(1.0)

form.show()
splash.finish(form)

app.exec_()