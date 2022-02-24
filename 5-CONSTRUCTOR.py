# CONSTRUCTOR
""" class
    constructor
    METHOD
    
objeto = class
function  """

'''ESTRUCTURA BASE DEL CONSTRUCTOR'''
'''.format (adminnistrar variables)(dar formato)'''

#CLASE
class Persona:
    pass
    #CONSTRUCTOR
    def __init__(self,nombre,edad):
        self.name = nombre 
        self.age  = edad
    '''metodos dentro del constructor''' 
    def description(self):
        return '\n{} tiene {} años\n'.format(self.name, self.age)
    def comentario(self,saludo):
        return '\n{} dice {}\n'.format(self.name, saludo)
        
#OBJETO
instructor  = Persona('Juanki',36)
alumno      = Persona('Alex',21)
esposa      = Persona('María',20)

print(instructor.description())
print(instructor.comentario('Buenas Tardes jovenes'))

print(alumno.description())
print(alumno.comentario('Gracias por aceptarnos'))

print(esposa.description())
