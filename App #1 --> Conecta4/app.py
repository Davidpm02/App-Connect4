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
from colorama import init, Fore,Style

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
            
            resultado = random.choice(jugadores)
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
def accionesJugadores(jugador, tablero):   # esta funcion es propia para jugar J vs J, no para J vs IA.
    
    if jugador == 1:
        try:
            print("-- Turno del Jugador_1 -- ")
            print("-- Ficha del Jugador_1 --> X")
            
            print()
            columnaEscogida = int(input('Seleccione la columna donde quiera colocar su ficha:'))
            fichaJugador_1 = 'X'
            assert columnaEscogida in range(len(tablero[-1]) + 1)            # OPTIMIZAR EL CODIGO
            if tablero[-1][columnaEscogida] == ' ':                          # A partir de la segunda fila, no se ingresan X
                tablero[-1][columnaEscogida] = Fore.RED + fichaJugador_1                # Si hay una X en una columna y pongo una O, se sustituye la X por la O. SOLUCIONAR ESTO.
            elif tablero[-1][columnaEscogida] != ' ':
                tablero[-2][columnaEscogida] = Fore.RED + fichaJugador_1
            elif tablero[-2][columnaEscogida] != ' ':
                tablero[-3][columnaEscogida] = Fore.RED + fichaJugador_1
            elif tablero[-3][columnaEscogida] != ' ':
                tablero[-4][columnaEscogida] = Fore.RED + fichaJugador_1
            elif tablero[-4][columnaEscogida] != ' ':
                tablero[-5][columnaEscogida] = Fore.RED + fichaJugador_1
            elif tablero[-5][columnaEscogida] != ' ':
                tablero[-6][columnaEscogida] = Fore.RED + fichaJugador_1
            elif tablero[-6][columnaEscogida] != ' ':
                tablero[-7][columnaEscogida] = Fore.RED + fichaJugador_1
            elif tablero[-8][columnaEscogida] != ' ':
                tablero[-9][columnaEscogida] = Fore.RED + fichaJugador_1
            elif tablero[-9][columnaEscogida] != ' ':
                tablero[-10][columnaEscogida] = Fore.RED + fichaJugador_1
        except AssertionError:
            print()
            print(Fore.RESET + '=-=-= Por favor, escoge una columna que pertenezca al tablero. =-=-=')
        except IndexError:
            print(Fore.RESET + 'Se ha llegado al limite superior de la columna.')

            
    elif jugador == 2:
        try:
            print("-- Turno del Jugador_2 -- ")
            print("-- Ficha del Jugador_2 --> O")
            
            print()
            columnaEscogida = int(input('Seleccione la columna donde quiera colocar su ficha:'))
            fichaJugador_2 = 'O'
            assert columnaEscogida in range(len(tablero[-1]) + 1)            # OPTIMIZAR EL CODIGO
            if tablero[-1][columnaEscogida] == ' ':                          # A partir de la segunda fila, no se ingresan X
                tablero[-1][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-1][columnaEscogida] != ' ':
                tablero[-2][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-2][columnaEscogida] != ' ':
                tablero[-3][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-3][columnaEscogida] != ' ':
                tablero[-4][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-4][columnaEscogida] != ' ':
                tablero[-5][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-5][columnaEscogida] != ' ':
                tablero[-6][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-6][columnaEscogida] != ' ':
                tablero[-7][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-8][columnaEscogida] != ' ':
                tablero[-9][columnaEscogida] = Fore.GREEN + fichaJugador_2
            elif tablero[-9][columnaEscogida] != ' ':
                tablero[-10][columnaEscogida] = Fore.GREEN + fichaJugador_2 
        except AssertionError:
            print()
            print('=-=-= Por favor, escoge una columna que pertenezca al tablero. =-=-=')
        except IndexError:
            print('Se ha llegado al limite superior de la columna.')
        

def siguienteJugador(jugadorActual):
    try:
        assert jugadorActual == 1 or jugadorActual == 2
        if jugadorActual == 1:
            jugadorActual = 2
            return jugadorActual
        
        elif jugadorActual == 2:
            jugadorActual = 1
            return jugadorActual
    except AssertionError:
        print("Ha ocurrido un error al cambiar de jugador.")
        
    
    
    #Si es el jugador es 1, hace x cosas.
    #Si el jugador es 2 o IA, hace x cosas.
  

  
  
#Crear tablero
def crearTablero():  #borrar?
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
        lista = [tablero,numeroTurnos]
        return lista
        
            
  # -------------------------------------------------------------------------------------------------------------------------------- #

def mostrarTablero(tablero,numeroTurnos):
    try:
        assert tablero != None   # Esta funcion necesita que se le pase el argumento del tablero, pero es posible que en su creacion
        print()                  # no se cumplan algunas condiciones y se ejecute la excepcion AssertionError.
        for item in tablero:     # Es por esto que incluyo un bloque try: except: aqui, pues en el caso de que no reciba el argumento 
            print('|',end='')    # del tablero, no podemos dejar que el programa falle.
            for columna in item:
                print(Fore.RESET + str(columna),end=Fore.RESET + '|')
            else:
                print(Fore.RESET + '',end='\n')
        
    except AssertionError:
        pass
#Control de turnos
def controlarTurnos(turnos):
    try:
        turnos -= 1
        assert turnos > 0
        return turnos
    except AssertionError:
        print("El juego ha terminado.")
  
  # -------------------------------------------------------------------------------------------------------------------------------- #
  
# Jugar partida
def jugarPartida():
    jugadorActual = Jugador_1
    juegaPrimero(modoDeJuego)
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
        
    while numeroTurnos > 0:
        mostrarTablero(tablero,numeroTurnos)
        print(Fore.RESET + '+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        print(Fore.RESET + "NUMERO TURNOS RESTANTES: {}".format(numeroTurnos))
        accionesJugadores(jugadorActual, tablero)
        numeroTurnos -= 1
        if numeroTurnos == 0:
            mostrarTablero(tablero,numeroTurnos)            
        try:
            assert jugadorActual == Jugador_1 or jugadorActual == Jugador_2
            if jugadorActual == Jugador_1:
                jugadorActual = Jugador_2
            elif jugadorActual == Jugador_2:
                jugadorActual = Jugador_1
        except AssertionError:
            print(Fore.RESET + "Ha ocurrido un error al cambiar de jugador.")
    else:
        print()
        print('###')
        print("EL JUEGO HA TERMINADO.")
        print('Jugador_1 y Jugador_2 quedan EMPATE.')
        print('###')
        print()
    

if __name__ == '__main__':
    jugarPartida()