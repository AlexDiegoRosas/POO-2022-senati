# CLASE MAYOR

class Calculadora:
    def __init__(self, number):
        self.number = number
        self.datos  = [0 for contador in range (number)] #bucle si necesita 1 dato o 2 limitamos el número de datos 
    def ingresoDatos(self):
        self.datos = [int(input('Ingreso dato '+str(contador + 1)+ ' : ')) for contador in range(self.number)]
    def __del__(self):
        self.number
        self.datos
        print ('*****La memoria ha sido liberada******\n')
class OpBasica(Calculadora):
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

class Logaritmos(Calculadora):
    def __init__(self):
        Calculadora. __init__(self,2)
    def logartimo(self):
        import math
        a,b, = self.datos
        loga = round(math.log(a,b),2)
        print(f'El logaritmo de {a} en base {b} es: {loga}' )    
class AreaCuadrado(Calculadora):
    def __init__(self):
        Calculadora. __init__(self,2)
    def cuadrado(self):
        a,b, = self.datos
        print('El area del cuadrado es: ', a*b)
        
class AreaTriangulo(Calculadora):
    def __init__(self):
        Calculadora. __init__(self,2)
    def trian(self):
        a,b, = self.datos
        print("El área del triángulo es: ", (a*b)/2)
        
class CalculadoraAvanzada(OpBasica,opAvanzadas):
    def __def__(self):
        pass
class CalculadoraCientifica(CalculadoraAvanzada,Porcentaje,Logaritmos,AreaCuadrado,AreaTriangulo):
    def __def__(self):
        pass

while True:
    opcion = input('\n operación: ')
    
    if opcion == 'x':
        print('\n ***GRACIAS*** \n')
        break
    else:
        pass
    if opcion == '+':              
        Resultadosuma = CalculadoraCientifica()
        print(Resultadosuma.ingresoDatos())
        print(Resultadosuma.suma())
    elif opcion == '-':
        Resultadoresta = CalculadoraCientifica()
        print(Resultadoresta.ingresoDatos())
        print(Resultadoresta.resta())
    elif opcion == '*':
        Resultadomulti = CalculadoraCientifica()         
        print(Resultadomulti.ingresoDatos())
        print(Resultadomulti.multiplicacion())
    elif opcion == '/':
        Resultadodiv = CalculadoraCientifica()
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
        Rporcentaje = CalculadoraCientifica()
        print(Rporcentaje.ingresoDatos())
        print(Rporcentaje.porciento())
    elif opcion == 'log':
        Rlog = CalculadoraCientifica()
        print(Rlog.ingresoDatos())
        print(Rlog.logartimo())
    elif opcion == "acuad":
        Racuad = CalculadoraCientifica()
        print(Racuad.ingresoDatos())
        print(Racuad.cuadrado())
    elif opcion == "atrian":
        Ratrian = CalculadoraCientifica()
        print(Ratrian.ingresoDatos())
        print(Ratrian.trian())
    else:
        print('\n OPCIÓN NO VALIDA\n')
