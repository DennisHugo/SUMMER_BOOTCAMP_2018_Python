import sys

class Employe:

    def __init__(self, nombcomp):
        first,last = nombcomp.lower().split(' ')
        self.__first, self._last = first,last
        self.email = first + "." + last + "@email.com"

    def getEmail(self):
        return self.email


author = "FAL"

if __name__ == "__main__":
    nomc = sys.argv[1]  #Es para ingresar parametros desde ejecutar python
    numc = sys.argv[2]  #Para ingresar el parametro de numero
    emp = Employe(nomc)
    print(emp.getEmail())
    print("El nombre es: " ,nomc)
    print("El numero de Cel. es: ", numc)

    #Se imprime todo con el siguiente comando: python intaractive_mode.py "dennis tala" "123455"