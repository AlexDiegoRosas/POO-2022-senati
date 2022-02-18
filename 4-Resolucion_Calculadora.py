'''Crear una calculadora con 4 funciones básicas'''

# Crear la clase

class Calculadora:
    def __init__(self,num1,num2):
        self.opSuma          = num1 + num2
        self.opResta         = num1 - num2
        self.opMultipicacion = num1 * num2
        self.opDivision      = round(num1 / num2,1)
        
while True:
    opcion = input('\n operación: ')
    
    if opcion == 'x':
        print('\n ***GRACIAS*** \n')
        break
    else:
        # solicitando ingreso
        num1 = int(input('\n Ingrese su primer Número: '))
        num2 = int(input('\n Ingrese su segundo Número: '))        
        objRespuesta = Calculadora(num1,num2)
        
    # seleccionar la operacion a resolver
    if opcion == '+':
        print(f'\n La suma es: {objRespuesta.opSuma}')
    elif opcion == '-':
        print(f'\n La resta es: {objRespuesta.opResta}')
    elif opcion == '*':
        print(f'\n La multiplicación es: {objRespuesta.opMultipicacion}')
    elif opcion == '/':
        print(f'\n La División es: {objRespuesta.opDivision}')
    else:
        print('\n OPCIÓN NO VALIDA\n')


