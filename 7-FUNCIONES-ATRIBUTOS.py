# FUNCIONES PARA LOS ATRIBUTOS

class People:
    age     = 30
    name    = 'Juanki'
    
instructor = People()

# Permite reescribir o cambiar un atributo
print('\n') 
print(instructor.name)
print('\n') 
setattr(instructor,'name','Brandon')
print(instructor.name)
print('\n') 


''' #PERMITE PREGUNTAR SI EXISTE UN ATRIBUTO CON EL NOMBRE INDICADO
print('\n')
print('Humano tienes edad: ',hasattr(instructor,'age'))
print('\n') '''
''' 

#PERMITE MOSTRAR LOS ATRIBUTOS SIN NECESIDAD DE INGRESAR 

print('Humano tu nombre es: ',instructor.name)
print(f'\nHumano tu nombre es: {instructor.name}\n')
print('Tu nombre es: ',getattr(instructor,'name')) '''