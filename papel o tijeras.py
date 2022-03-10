from random import choice
options = ["piedra", "tijeras", "papel"]
class Game():
    pass
        #options = ["piedra", "tijeras", "papel"]

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
    elif p1 == "papel" and p2 == "piedra":
        result = 1
    elif p1 == "papel" and p2 == "tijeras":
        result = 2
    return result

class GameHumanoVSHumano(Game):
    def vs(self):
        pass
        jugador1 = input("jugador 1 Ingrese su jugada:(piedra),(papel) o (tijeras): \n ")
        jugador2 = input("Jugador 2 Ingrese su jugada:(piedra),(papel) o (tijeras): \n ")
        print("Jugador1: %s - Jugador2: %s  - Ganador: %s " %(jugador1,  jugador2 ,buscar_ganador(jugador1, jugador2)))
    
class GameHumanoVSMaquina(Game):
    def VSMaquina(self):
        pass
        from random import choice
        def get_player():
            return choice(options)
        jugador1 = input("Ingrese su jugada:(piedra),(papel) o (tijeras): \n ")
        jugador2 = get_player()
        print("Jugador1: %s - Jugador2: %s  - Ganador: %s " %(jugador1,  jugador2 ,buscar_ganador(jugador1, jugador2)))

a = 0
# modalidad de Juego
while a < 5:
    a = a + 1
    opcion = input('\n Modalida de Juego "1": (1 vs 1) O "2":(1 vs Maquina): ')
    
    if opcion == 'x':
        print('\n ***GRACIAS*** \n')
        break
    else:
        pass
    # seleccionar la operacion a resolver
    if opcion == '1':
        game = GameHumanoVSHumano()
        game.vs()
    elif opcion == '2':
        game = GameHumanoVSMaquina()
        game.VSMaquina()
    else:
        print('\n OPCIÓN NO VALIDA\n')
    if a == 5:
        print ("Fin del juego XD!!!")
   

    