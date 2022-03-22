# POLIMORFISMO COMO TAL: 
'''
Es una repetición del constructor sobre las clases hijo
'''
'''redefinir el constructor''' #La redefinicion se ve en el metodo#
class Empleado:
    def __init__(self,nombre,sueldoMensual):
        self.nombre         =   nombre
        self.sueldoMensual  =   sueldoMensual
               
    def clalcularSueldoAnual(self):
        sueldo   =   12 * self.sueldoMensual *(1+1/100)
        print(f'El sueldo anual de {self.nombre}, empleado regular es de {sueldo}')
    
class Instructor(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
    def clalcularSueldoAnual(self):
        sueldo   =   12 * self.sueldoMensual *(1+2/100)
        print(f'El sueldo anual de {self.nombre}, - Instructor, es de {sueldo}')    
class AsistenteAcademico(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
    def clalcularSueldoAnual(self):
        sueldo   =   12 * self.sueldoMensual *(1+4/100)
        print(f'El sueldo anual de {self.nombre}, - Asistente Academico, es de {sueldo}')    
class Director(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
    def clalcularSueldoAnual(self):
        sueldo   =   12 * self.sueldoMensual *(1+6/100)
        print(f'El sueldo anual de {self.nombre}, - Director, es de {sueldo}')
        
class JefeZonal(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
    def clalcularSueldoAnual(self):
        sueldo   =   12 * self.sueldoMensual *(1+8/100)
        print(f'El sueldo anual de {self.nombre}, - Jefe Zonal, es de {sueldo}')
        
  