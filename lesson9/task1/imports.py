
import calculator

calc = calculator.Calculator()      #Se crea un metodo de la clase calculator para poder acceder a sus metodos.
calc.add(2)
print(calc.get_current())

import my_module    #Se importa el archivo my_module.py que se encuentra en la misma carpeta

my_module.hello_world("Dennis")
#Se llama al metodo directamente debido a que no tiene una clase para crear un objeto.