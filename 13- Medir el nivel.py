'''
1.-Medir el nivel de programación
2.-Insertar Script en el POO
3.-Manejo de arreglos
'''

# Diseñar un algoritmo de Juego: Piedra, papel y Tijeras.

options = ["piedra", "tijeras", "papel"]

def buscar_ganador (p1,p2):
    if p1 == p2:
        result = 0
    elif p1 == "piedra" and p2 == "tijeras":
        result = 1
    elif p1 == "piedra" and p2 == "papel":
        result = 2
    elif p1 == "tijeras" and p2 == "piedra":
        result = 2
    elif p1 == "tijeras" and p2 == "papel":
        result = 1
    elif p1 == "papel" and p2 == "tijeras":
        result = 2
    return result

# Jugadas con 2 Humanos 


#Prueba 1:
buscar_ganador("tijeras", "papel")

test = [["piedra","piedra",0],["piedra","tijeras",1],["piedra","papel",2]]

for partida in test:
    print("Jugador1: %s - Jugador2: %s ficha Ganadora: %s El ganador es: %s" %(partida [0], partida [1], buscar_ganador(partida[0],partida[1]),partida[2]))

# Jugadas al azar - humano vs computadora
from random import  choice
def get_choice():
    return choice(options)


for i in range(10):
    player1 = get_choice()
    player2 = get_choice()
    print("Jugador1: %s - Jugador2: %s  - Ganador: %s " %(player1,  player2 ,buscar_ganador(player1, player2)))


"""Crear el resto de codigo para ingresar la jugada por teclado
crear las funciones para jugar:
un While o if con limite
"""



''' class Juego:
    def __init__(self, piedra, papel, tijeras):
        self.piedra = piedra
        self.papel  = papel '''