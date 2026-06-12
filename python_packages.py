#Instead of modules in javascript, Python uses packages that are simply .py files
#a python module is a .py file
#a package is a directory containing a special "__init__.py" file which can include one or more modules

#utils.py
def add(a,b):
  return a + b

def multiply(a, b):
  return a * b

#in a different file

#main.py
from utils import add, multiply

print(add(2, 3,))
print(multiply(2, 3))

#Python uses pip to manage packages (python installer package) to manage libraries and frameworks
#Python projects commonly use requirements.txt file to list dependencies

#in the terminal to install a library with pip

pip install flask

#defining dependencies in requirements.txt

flask==2.3.0
requests==2.31.0

#to install all dependencies in requirements.txt:

bashCopy codepip install -r requirements.txt

