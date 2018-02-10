# QtCalculator
Home project to make a replica of Windows Calculator using Qt and Python

I started this project to learn more about Qt and PyQt4. 
I am creating a replica of calculator that you can find in Windows OS. 

I create UI using Qt designer. Then convert the .ui file to .py using pyuic4.bat. You can use 'convert_qt_py.py' in the 'UserInterface' folder to create 'ui_calculator.py' which contains the UI definition for the calculator. 

For compiling resources, use 'compile_resources.py' in the 'UserInterface' folder.

As UserInterface is a python package, you may need to manually import 'icons_rc' in the 'ui_calculator.py': import UserInterface.icons_rc
