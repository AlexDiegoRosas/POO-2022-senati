#clase general 

class Dispositivo:
    def __init__(self):
        pass
    #comportamientos que tiene un dispositivo
    def enLlamada(self):
        print('Llamada en curso')
    def enEspera(self):
        print('Llamada en espera')

class Imagen:
    def __init__(self):
        pass
    def capturarFoto(self):
        print('Camara Activa')
    def enviarFoto(self):
        print('Foto Enviada')


class Multimedia:
    def __init__(self):
        pass
    def capturarVideo(self):
        print('Video en grabacion')
    def reproducirMusica(self):
        print('Escuchando Musica')


class EquipoMovil(Dispositivo,Imagen,Multimedia):
    def __del__(self):
        pass

class EquipoBasico(Dispositivo):
    def __def__(self):
        pass
        #print('El resto de utilidades detenidas')


smartphone = EquipoMovil()
print(smartphone.enLlamada())

nokia315 = EquipoBasico()
print(nokia315.enLlamada())




