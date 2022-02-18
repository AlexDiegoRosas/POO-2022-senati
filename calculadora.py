print("CALCULADORA BÁSICA DE 2 NÚMEROS")
print("##############################")

class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1 = float(num_1)
        self.num_2 = float(num_2)

    def sumar(self):
        suma = self.num_1 + self.num_2
        print("El resultado de la suma es: ", suma)

    def restar(self):
        resta = self.num_1 - self.num_2
        print("El resultado de la resta es: ", resta)

    def producto(self):
        multiplicacion = self.num_1 * self.num_2
        print("El resultado de la multiplicación es: ", multiplicacion)

    def dividir(self):
        division = self.num_1 / self.num_2
        print("El resultado de la divición es: ", division)
        
num_1 = input("Ingrese su primer número: ")
num_2 = input("Ingrese su segundo número: ")
calculadora = Calculadora(num_1, num_2)

calculadora.sumar()
calculadora.restar()
calculadora.producto()
calculadora.dividir()