#Agregar, Modificar un nuevo atributo en una clase hijo.
'''Modificar sobreescribir un metodo'''

class Persona():
    def __init__(self,apPat,apMat,nombre):
        self.apellidoPat    = apPat
        self.apellidoMat    = apMat
        self.nombres        = nombre
    
    # creacion de los métodos comportamientos:
    def mostrarNomb(self):
        mensaje = '{0} {1}, {2}'
        return mensaje.format(self.apellidoPat,self.apellidoMat,self.nombres)
    
    def entregarDatos(self):
        print(self.mostrarNomb())
class Prospecto (Persona):
    pass
class Recurrente (Persona):
    def __init__(self, apPat, apMat, nombre,deuda):
        super().__init__(apPat, apMat, nombre)
        self.prestamo = deuda
    def entregarDatos(self):
        super().entregarDatos()
        print(f'Mantiene {self.prestamo}')
        
cliente = Recurrente('Flores','Zenteno','Juan Carlos','deuda')
cliente.entregarDatos()

