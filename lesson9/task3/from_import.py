
from calculator import Calculator       #Se importa todo el archivo pero se define que solo utilizara la clase Calculator

calc = Calculator()
calc.add(2)
print(calc.get_current())

from my_module import hello_world       #Se importa todo el archivo pero se define que solo se utilizara el metodo hello word

print(hello_world())
