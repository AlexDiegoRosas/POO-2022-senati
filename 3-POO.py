#Metodos
'''class nombre:
    def nombre_metodo(self):
        self.variable = valor o (algoritmo)
        
creación_objto.asignación_clase()'''

#forma 1

class Matematica:
    def operacion(self):
        self.num_1 = 14
        self.num_2 = 3

suma = Matematica()
suma.operacion()
print('La suma es: ',suma.num_1 + suma.num_2)


#forma 2

class Matematica1:
    def __init__(self):
        self.num_1 = 10
        self.num_2 = 5
        
suma = Matematica1()
print('La suma es: ', suma.num_1 + suma.num_2)