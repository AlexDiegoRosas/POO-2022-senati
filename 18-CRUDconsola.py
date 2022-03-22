import pyodbc
import Persona

print('1. Obtener')

print('2. Crear')

print('3. Editar')

print('4. Eliminar')
op= input('Selecciona una opcion: ')

if op == '1':
    oPersona = Persona.Persona()
    oPersona.Obtener()
elif op == '2':
    oPersona = Persona.Persona()
    oPersona.Add('Juanki','Peru')
elif op == '3':
    oPersona = Persona.Persona()
    oPersona.Obtener()
    id = input('cual perosna desear editar')
elif op == '4':
    oPersona = Persona.Persona()
    oPersona.Obtener()
    id = input('cual perosna desear eliminar')
else:
    print('opcion invalida')



