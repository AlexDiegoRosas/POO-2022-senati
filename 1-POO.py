# clase y objeto + atributo

'''class nombre de clase'''

class VehiculoParticular:
    marca = 'Renault';
    modelo = 'Duster';
    placa = 'Z1R423';

class VehiculoPublico:
    marca = 'Toyota';
    modelo = 'RAV4';
    placa = 'PNP357';
    
'''Crear los objetos'''

taxi = VehiculoParticular()
print(taxi.marca)

patrullero = VehiculoPublico()
print(patrullero.marca)