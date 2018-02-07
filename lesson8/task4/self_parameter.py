"""
self es el primer parámetro que se pasa a cualquier método de clase.
Python usará el parámetro self para referirse al objeto que se está creando.
"""
class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0

    def add(self, amount):
        self.current += amount
        print("ANIADIENDO "+str(self.current)+"Bs")

    def get_current(self):
        return self.current

Objeto_Complex = Complex()          #CREANDO OBJETO PARA COMPLEX
Objeto_Complex.create(5,10)         #LLAMANDO AL METODO /CREATE\ CON EL OBJETO_COMPLEX

Objeto_Calculadora = Calculator()   #CREANDO OBJETO PARA CALCULADORA
Objeto_Calculadora.add(100)         #HACIENDO USO AL METODO /ADD\ CON EL OBJETO_CALCULADORA PASANDOLE COMO PARAMETRO EL NUMERO 100!!!
print("MONTO : " + str(Objeto_Calculadora.get_current()))

# Para Complex cree el objeto y realize una llamada al metodo


# Para Calculator cree el objeto y realize llamadas a los metodos
# identifique y resuelva el problema
