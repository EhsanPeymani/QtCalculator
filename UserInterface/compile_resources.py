import os

pyuic = 'C:\\Users\\247699\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt4\\pyrcc4.exe '

icons_path = '\\'.join(os.path.dirname(__file__).split('/')[:-1])
print(icons_path)
cmd = pyuic + icons_path + '\icons\icons.qrc -o icons_rc.py -py3'

# the generated py file must live in the root folder
# the name of the generated python is very imported, since the UI python file need to import it s icons_rc.py


try:
    os.system(cmd)
    print('resources compiled successfully.')
except:
    print('Unsuccessful')

