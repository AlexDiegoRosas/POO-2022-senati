# DESTRUCTOR
'''
1. EL DESTRUCTOR SOLO INICIA Y FUNCIONA SI EXISTE UN COSTRUNCTOR.
2. Se inicia con la palabra reservada  "__del__"
3. Sirve para eliminar los datos que no se esten utilizando, siendo su alcance hasta la memoria.
'''
'''El destructor trabaja en las variables, elimina lo que almacena las variables''' 

class Persona:
    # Creación del constructor
    def __init__(self,name,age):
        self.nombre = name 
        self.edad   = age
        
    def metodo1(self):
        return '\n{} tiene {} años\n'.format(self.nombre, self.edad)
    
    def metodo2(self,frase):
        return '\n{} dice {}\n'.format(self.nombre, frase)
 
    # Creación del destructor
    def __del__(self):
        self.nombre
        self.edad
        print ('*****La memoria ha sido liberada******\n')
        
# Creación de los objetos
doctor    = Persona('Mario', 45)
enfermera = Persona('Roxy', 28)
visita    = Persona('Tula', 50)
paciente  = Persona('Juan', 20)

print(doctor.metodo1())
print(enfermera.metodo1())
print(paciente.metodo1())

print(doctor.metodo2('Hola ¿Cómo se encuentra?'))
print(enfermera.metodo2('Bien Gracias'))
print(visita.metodo2('¿Puedo pasar?'))
