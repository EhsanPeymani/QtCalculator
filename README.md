# QtCalculator
Home project to make a replica of Windows Calculator using Qt and Python

I started this project to learn more about Qt and PyQt4. 
I am creating a replica of calculator that you can find in Windows OS. 

I create UI using Qt designer. Then convert the .ui file to .py using pyuic4.bat. You can use 'convert_qt_py.py' in the 'UserInterface' folder to create 'ui_calculator.py' which contains the UI definition for the calculator. 

For compiling resources, use 'compile_resources.py' in the 'UserInterface' folder.

As UserInterface is a python package, you may need to manually import 'icons_rc' in the 'ui_calculator.py': import UserInterface.icons_rc

[![calculator.png](https://s18.postimg.cc/55g1pgwe1/calculator.png)](https://postimg.cc/image/bvwiywjjp/)

# Installer
You can install the app by running ./Output/eCalculator.exe file.
The executable binary is located in ./dist/app.exe file. 

The binary is created using PyInstaller. See build_executable.py file for commands. 

The installer was created using Inno Setup Compiler. The project file is setup.iss. 

[![calc_setup.png](https://s18.postimg.cc/7mrswplfd/calc_setup.png)](https://postimg.cc/image/8cal92lyt/)

# Shortkeys
All keys on Numpad

Backspace --> Clear

Esc --> CE

Delete --> C

Ctrl + s --> sqrt

Alt + s --> squared

Ctrl + r --> reciprocate

Ctrl + n --> negate



