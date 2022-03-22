# clase general

class Dispositivo:
    def __init__(self):
        pass
    # comportamientos que tiene un dispositivo
    def enLlamada(self):
        print('Llamada en curso ')
    def enEspera(self):
        print('Llamada en espera ')

class Imagen:
    def __init__(self):
        pass
    def cpturarFoto(self):
        print('Camara activada')
        
class Multimedia:
    def __init__(self):
        pass
    def capturarVideo(self):
        print('video en Grabación (en curso)')
    def reproducirMusica(self):
        print('Escuchando Musica')
        
class Utilitarios:
    def __init__(self):
        pass
    def calculadora(self):
        pass
    def notebook(self):
        pass
        
class EquipoMovil(Dispositivo,Imagen,Multimedia,Utilitarios):
    def __del__(self):
        print('El resto de utilidades detenidas')
        

class EquipoBasico(Dispositivo):
    def __del__(self):
        pass    
smartphone = EquipoMovil()
print(smartphone.reproducirMusica())