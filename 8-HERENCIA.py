# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:39:09 2022

@author: Alex
"""

# Herencia
'''clase mayor o clase papá'''
class Animal:
    pass
    def __init__(self, nombre,raza):
        self.nombre = nombre
        self.raza   = raza
        
    #Metodos
    def description(self):
        return '{} es de raza {}'.format(self.nombre,self.raza)
    
'''clase hijo o subclases'''
class Perro(Animal):
    def comportamiento(self,tipoSonido):
        return '{} todo el tiempo {}'.format(self.nombre,tipoSonido)
        #return '{} todo el tiempo {}'.format(self.nombre,impulso)
class Gato(Animal):
    def comportamiento(self,tipoSonido):
        return '{} todo el tiempo {}'.format(self.nombre,tipoSonido)

#Objetos
nuevoAnimal = Perro('Firulays','Labrador')
print(nuevoAnimal.description())
print(nuevoAnimal.comportamiento('Ladra'))

otroAnimal = Gato('Mina','Siberiano')
print(otroAnimal.description())
print(otroAnimal.comportamiento('Maulla'))        

animalito = Perro('Rex','Sabueso')
print(animalito.description())
print(animalito.comportamiento('ladra'))
    