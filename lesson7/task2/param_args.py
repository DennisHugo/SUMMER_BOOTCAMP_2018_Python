def foo(x):                 # x es un parámetro de la función
    print("x = " + str(x))

foo(5)   # 5 es un argumento pasado a la funcion

def square(x):
    print(x," ", x**2)

for i in range(1,9,3):
    square(i)

"""
square(4)
square(8)
square(15)
square(23)
square(42)
"""