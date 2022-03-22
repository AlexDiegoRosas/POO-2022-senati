from tkinter import Variable


def singleton(cls):
    instance = dict()
    def wrap(*arg, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*arg, **kwargs)
        return instance[cls]
    return wrap

class Producto:
    def __init__(self, id, description, costo):
        self.id = id
        self.description = description
        self.costo = costo
    
    def crear_etiqueta(self):
        return '%s \n %s \n %0.2f'%(self.id,self.description,self.costo)
@singleton    
class Electronico(Producto):
    def __init__(self, id, descripcion, costo, marca):
        super().__init__(id, descripcion, costo)
        self.marca = marca
if __name__ == '__main__':
        vendedor1 = Electronico('Electrodomestico','Lavadora',1750,'LG')
        vendedor2 = Electronico('Electrodomestico','licuadora',550,'Samsung')
        print(vendedor1 is vendedor2)
        print('Esta en uso')
class Comestibles(Producto):
    def __init__(self, id, description, costo, caducidad):
        super().__init__(id, description, costo)
        self.caducidad = caducidad
    def crear_etiqueta(self):
        return super().crear_etiqueta()+'\n %s'%self.caducidad
if __name__ == '__main__':
        vendedor1 = Comestibles('Alimentos','Papitas',1.5,'FV: 20/02/2022')
        vendedor2 = Comestibles('Alimentos','leche',1.5,'FV: 21/04/2022')
        variable = print(vendedor1 is vendedor2)
        if variable == True:
            print('Esta en uso')
        else:
            print('Siga con su venta')
        
# INSTANCIANDO XD #

productos = (Producto('General', 'Coche Bebé', 200), Comestibles('Alimentos','Papitas',1.5,'FV: 20/02/2022'), Electronico('Electrodomestico','Lavadora',1750,'LG'))

for objeto in productos:
    print('\n*****',objeto.crear_etiqueta())



