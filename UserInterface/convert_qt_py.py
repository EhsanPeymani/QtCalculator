# this file will convert the .ui file created by QtDesigner to .py file

pyuic = 'C:\\Users\\247699\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt4\\pyuic4.bat '
cmd = pyuic + 'Calculator.ui -o ui_calculator.py'

import os
os.system(cmd)

print('UI converted Successfully.')