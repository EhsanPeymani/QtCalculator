'''
This module compile the app.py into binaries.
The output is ./dist/app.exe
'''
import os

cmd = 'pyi-makespec app.py -F -w --icon ./icons/calculator.ico'
print(cmd)
os.system(cmd)


cmd = 'pyinstaller app.spec'
os.system(cmd)
