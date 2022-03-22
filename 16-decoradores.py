# CREAR UNA SESION SINGLETON CON DECORADORES
def singleton(cls):
    instance = dict()
    def wrap(*arg, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*arg, **kwargs)
        return instance[cls]
    return wrap
        
@singleton
class Empleado(object):
    def __init__(self, vendedor):
        self.vendedor = vendedor
        
if __name__ == '__main__':
        
        vendedor1 = Empleado('Juanki')
        vendedor2 = Empleado('Alex')
        
        print(vendedor1 is vendedor2)
        
@singleton
class Empleado(object):
    def __init__(self, vendedor):
        self.vendedor = vendedor
        
if __name__ == '__main__':
        
        Cajero1   = Empleado('Juanki')
        vendedor2 = Empleado('Alex')
        
        print(Cajero1 is vendedor2)
        
'''Decoradores ¿Qué son?
Funciones que a su vez añaden funcionalidades a otras funciones.
Por eso se las denomina 'decoradores', porque 'decoran' a otras funciones.
Les añade funcionalidades.

ESTRUCTURA DE UN DECORADOR:
* 3 funciones (A,B y C) donde A recibe como parámetro a B para devolver C.
*Un decorador devuelve una funcion
'''
'''
    def funcion_decorador(funcion):
        def funcion_interna():
            #codigo de la funcion interna
        return función_interna
'''

