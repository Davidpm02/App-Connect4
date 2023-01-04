#El juego está formado por un tablero, y fichas de dos colores diferentes.
# Es un juego para dos jugadores y cada jugador tiene asignado un color de fichas.

#El objetivo de Connect4, como su nombre lo dice, consiste en conectar 4 fichas del mismo color en una línea,
# en cualquier dirección, horizontal, vertical, y diagonalmente (hacia ambos lados).


#El jugador que forme la fila de cuatro fichas primero ganará. Las reglas del juego no son muy complicadas:
#     - El jugador que juega primero se escoge al azar.
#     - Cada jugador tira una sola ficha por turno.
#     - El tablero se compone de columnas, no de filas. Eso quiere decir que las fichas solo pueden
#       introducirse en la parte de arriba de una columna, y caer hasta llegar al la parte más baja o encima de otra ficha,
#       no puede quedar flotando por ahí.
#     - El juego se gana solo si uno de los jugadores logra forman una fila de cuatro fichas del mismo color.
#     - Si el tablero se llena de fichas y no hay ganador, el juego quedó empatado.


import random
from colorama import init



# Declaro las constantes del juego ----------------------


Min_Filas = 5
Max_Filas = 10
Min_Columnas = 6
Max_Columnas = 10
ESPACIO_VACIO = ' '
Jugador_1 = 1
Jugador_2 = 2
JUGANDO_CPU = False
CONECTA = 4



# ------------------------------------------------------------



def modoDeJuego():
    try:
        modoJuego = int(input("""Selecciona un modo de juego:
                              1. J vs J
                              2. J vs IA"""))
        assert modoDeJuego == 1 or modoDeJuego == 2
        return modoDeJuego
    except AssertionError:
        print('Por favor, selecciona un modo de juego valido.')



def accionJugadores(modoDeJuego):
    if modoDeJuego == 1:
        print('Se ha seleccionado el modo de juego J vs J.')
        # Definir que jugador empieza antes, random.randint()
        
    elif modoDeJuego == 2:
        print('Se ha seleccionado el modo de juego J vs IA.')
        # Definir que jugador empieza antes, random.randint()
        
        
               
#Definir Jugador 1   
def juegaPrimero():
    jugador1 = int(input('Escriba un numero del 1 al 5:'))
    jugador2 = int(input('Escriba un numero del 1 al 5:'))
    
    resultado = random.randint(jugador1,jugador2)
    if resultado == jugador1:
        return '--- El jugador 1 empieza el juego primero. ---'
    elif resultado == jugador2:
        return '--- El jugador 2 empieza el juego primero. ---'
    else:
        return 'Ha ocurrido un error al elegir al primero jugador.'
        
  
#Crear tablero
def crearTablero():
    try:
        try:
            numeroColumnas = int(input('Selecciona un numero de columnas:'))
            print()
            assert numeroColumnas > Min_Columnas and numeroColumnas < Max_Columnas
            
        except AssertionError:
            if numeroColumnas < Min_Columnas:
                print('El numero de columnas elegido es inferior al minimo requerido.')
                raise Exception
            elif numeroColumnas > Max_Columnas:
                print('El numero de columnas elegido es superior al maximo permitido.')
                raise Exception
                
                
        try:       
            numeroFilas = int(input('Seleccione un numero de filas:'))
            print()
            assert numeroFilas > Min_Filas and numeroFilas < Max_Filas
            
        except AssertionError:
            if numeroFilas < Min_Filas:
                print('El numero de filas elegido es inferior al minimo requerido.')
                raise Exception
            elif numeroFilas > Max_Filas:
                print('El numero de filas elegido es superior al maximo permitido.')
                raise Exception
                
        
        try:        
            numeroTurnos = int(input('Selecciona un numero de turnos:'))
            print()
            assert numeroTurnos > 0 and numeroTurnos < 100
            
        except AssertionError:
            if numeroTurnos <= 0:
                print('El numero de turnos elegidos debe ser positivo y distinto de 0.')
                raise Exception
            elif numeroTurnos >= 100:
                print("El numero maximo de turnos permitidos es de 99.")
                raise Exception
                
                
                
    except Exception:
        print('Ha ocurrido algun fallo al crear la partida. Por favor, intentelo de nuevo.')
        print()
    
    else:
        for num in range(1,numeroColumnas + 1):
            print('|'+ str(num),end='')
        else:
            print('|',end='\n')
            
        for num in range(numeroFilas):
            print("| "* (numeroColumnas + 1))
            
        print('**** EL TABLERO HA SIDO CREADO CON EXITO ****')
            
  # -------------------------------------------------------------------------------------------------------------------------------- #


#Control de turnos
def controlarTurnos(turnos):
    try:
        turnosRestantes = turnos - 1
        assert turnosRestantes > 0
        return "Turnos restantes: {} turnos.".format(turnosRestantes)
    except AssertionError:
        print("El juego ha terminado.")
  
  # -------------------------------------------------------------------------------------------------------------------------------- #
  
# Jugar partida
def jugarPartida():
    pass

if __name__ == '__main__':
    crearTablero()
    