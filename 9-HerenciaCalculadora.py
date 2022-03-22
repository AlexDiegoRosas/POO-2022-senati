# CLASE MAYOR

class Calculadora:
    def __init__(self, number= int()):
        self.number = number
        self.datos  = [0 for contador in range (number)] #bucle si necesita 1 dato o 2 limitamos el número de datos 
    def ingresoDatos(self):
        self.datos = [int(input('Ingreso dato '+str(contador + 1)+ ' : ')) for contador in range(self.number)]
    def __del__(self):
        self.number
        self.datos
        print ('*****La memoria ha sido liberada******\n')
class opBasica(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    def suma(self):
        a,b, = self.datos 
        suma = a + b
        print ('El resultado de la suma es: ',suma)
    def resta(self):
        a,b, = self.datos 
        resta = a - b
        print ("El resultado de la resta es: ",resta)
    def multiplicacion(self):
        a,b, = self.datos
        multiplicacion = a * b
        print ('El resultado de la Multiplicación es: ',multiplicacion)
    def division(self):
        a,b, = self.datos
        division = a / b
        print ('El resultado de la división es: ',division)
class opAvanzadas(Calculadora):
    def __init__(self):
        Calculadora. __init__(self,1)
    #Solo me debe pedir un dato
    def raizCuadrada(self):
        import math
        a, = self.datos
        print('El resultado de la raiz cuadrada es: ', round(math.sqrt(a),2))
    def raizCubica(self):
        a, = self.datos
        print('El resultado de la raiz cubica es: ', round(a**(1/3),2))

class Porcentaje(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    def porciento (self):
        a,b, = self.datos 
        porcentaje = a/100*b
        print (f'El {a} %  de {b} es:  {porcentaje}')
while True:
    opcion = input('\n operación: ')
    
    if opcion == 'x':
        print('\n ***GRACIAS*** \n')
        break
    else:
        pass
        #objRespuesta = Calculadora()
        #print(objRespuesta.ingresoDatos())
    if opcion == '+':              
        Resultadosuma = opBasica()
        print(Resultadosuma.ingresoDatos())
        print(Resultadosuma.suma())
    elif opcion == '-':
        Resultadoresta = opBasica()
        print(Resultadoresta.ingresoDatos())
        print(Resultadoresta.resta())
    elif opcion == '*':
        Resultadomulti = opBasica()         
        print(Resultadomulti.ingresoDatos())
        print(Resultadomulti.multiplicacion())
    elif opcion == '/':
        Resultadodiv = opBasica()
        print(Resultadodiv.ingresoDatos())
        print(Resultadodiv.division())
    elif opcion == 'r':
        Resultadocua = opAvanzadas()
        print(Resultadocua.ingresoDatos())
        print(Resultadocua.raizCuadrada())
    elif opcion == 'c':
        Resultadocub = opAvanzadas()
        print(Resultadocub.ingresoDatos())
        print(Resultadocub.raizCubica())
    elif opcion == '%':
        Rporcentaje = Porcentaje()
        print(Rporcentaje.ingresoDatos())
        print(Rporcentaje.porciento())
    else:
        print('\n OPCIÓN NO VALIDA\n')