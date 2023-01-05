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

import time



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



def juegaPrimero(modoDeJuego):
    if modoDeJuego == 1:
        print('Se ha seleccionado el modo de juego J vs J.')
        # Definir que jugador empieza antes, random.randint()
        try:
            verifacionJugador_1 = input('Presiona cualquier tecla, Jugador_1...')
            verifacionJugador_2 = input('Presiona cualquier tecla, Jugador_2...')
            assert verifacionJugador_1 != None and verifacionJugador_2 != None
            print()
            
            
            
            jugadores = [Jugador_1,Jugador_2]  # Antes hemos definido que Jugador_1 apunta al valor 1 en memoria, y Jugador_2 apunta al valor 2.
            print('Se esta decidiendo que jugador comienza antes la partida.')
            time.sleep(4)
            
            resultado = random.randint(jugadores)
            print('El jugador elegido es...')
            if resultado == 1:
                time.sleep(2)
                print('Jugador_1!')
            elif resultado == 2:
                time.sleep(2)
                print('Jugador_2!')
                
            return resultado # Se debe utilizar esta variable en la funcion jugarPartida() para indicar es el turno del jugador 1, o el turno de jugador 2.
            
            
            
        except AssertionError:
            if verifacionJugador_1 == None:
                print('El Jugador_1 ha sido desconectado por falta de habilidad')
            elif verifacionJugador_2 == None:
                print('El Jugador_2 ha sido desconectado por falta de habilidad')
            
        
            
        
    elif modoDeJuego == 2:
        print('Se ha seleccionado el modo de juego J vs IA.')
        # Definir que jugador empieza antes, random.randint()
        try:
            verifacionJugador_1 = input('Presiona cualquier tecla, Jugador_1...')
            assert verifacionJugador_1 != None
            print("La IA ya esta lista!")
            print()
            
            
            
            CPU = 2
            jugadores = [Jugador_1,CPU]  # Antes hemos definido que Jugador_1 apunta al valor 1 en memoria, y Jugador_2 apunta al valor 2.
            print('Se esta decidiendo que jugador comienza antes la partida.')
            time.sleep(4)
            
            resultado = random.randint(jugadores)
            print('El jugador elegido es...')
            if resultado == 1:
                time.sleep(2)
                print('Jugador_1!')
            elif resultado == 2:
                time.sleep(2)
                print('IA!')
                
            return resultado # Se debe utilizar esta variable en la funcion jugarPartida() para indicar es el turno del jugador 1, o el turno de jugador 2.
            
            
            
        except AssertionError:
            if verifacionJugador_1 == None:
                print('El Jugador_1 ha sido desconectado por falta de habilidad')
            
        
               
#Definir Jugador 1   
def accionesJugadores(jugador):
    pass
    #Si es el jugador es 1, hace x cosas.
    #Si el jugador es 2 o IA, hace x cosas.
  

  
  
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
        tablero = []
        contador = 0
        for fila in range(numeroFilas + 1):     # + 1 porque la fila inicial se usara como cabecera, que marcara el numero de columnas.
            tablero.append([])
            if contador == 0:
                for numero in range(1,numeroColumnas + 1):
                    tablero[fila].append(numero)
                    contador +=1
            else:
                for columna in range(numeroColumnas):
                    tablero[fila].append(ESPACIO_VACIO)
                    
        print('**** EL TABLERO HA SIDO CREADO CON EXITO ****')  
          
        return tablero
            
  # -------------------------------------------------------------------------------------------------------------------------------- #

def mostrarTablero(tablero):
    try:
        assert tablero != None   # Esta funcion necesita que se le pase el argumento del tablero, pero es posible que en su creacion
        print()                  # no se cumplan algunas condiciones y se ejecute la excepcion AssertionError.
        for item in tablero:     # Es por esto que incluyo un bloque try: except: aqui, pues en el caso de que no reciba el argumento 
            print('|',end='')    # del tablero, no podemos dejar que el programa falle.
            for columna in item:
                print(columna,end='|')
            else:
                print('',end='\n')
                
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    except AssertionError:
        pass
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
    mostrarTablero((crearTablero()))