# App-Connect4
Juego Conecta 4 programado en Python3.

<h1> INTRODUCCION </h1>
Esta app consiste en programar el juego Conecta 4 utilizando Python.
<br>
<br>
<br>
<br>

<h2> COMMIT #1 </h2>

<br>
<br>
<br>
<br>
<h2> COMMIT #2 </h2>
He cambiado la funcion de creacion del tablero. Ahora respeta los limites inferiores y superiores que se establecen al inicio del programa como 'CONSTANTES'.

Todavia el juego no es funcional.
<br>
<br>
<br>
<br>
<h2> COMMIT #3 </h2>
Ahora se visualiza correctament el tablero de juego, con los numero marcados en la parte superior y 'delimitados' por pipes ('|').

Todavia el juego no es funcional.
<br>
<br>
<br>
<br>



<h3> ----------- Modificaciones en funcionalidades ----------- </h3>

<h2> COMMIT #4 --> juegaPrimero() </h2>
Se ha modificado la funcion juegaPrimero() para decidir correctamente que jugador empieza el juego.

La funcion tiene dos caminos definidos, en funcion de si el modo de juego introducido es 'J vs J', o 'J vs IA'.


Todavia el juego no es funcional.
<br>
<br>
<br>
<br>

<h2> COMMIT #5 --> siguienteJugador() ; jugarPartida() </h2>
Se ha creado una nueva funcion que recibe el jugador del turno actual y lo modifica para el siguiente turno.

El cuerpo de la funcion crearTablero() se ha incluido en la funcion jugarPartida(), por lo que se podria eliminar la funcion crearTablero() perse.

Paquenos cambios en otras funciones.


Todavia el juego no es funcional.
<br>
<br>
<br>
<br>


<h2> COMMIT #6 --> jugarPartida() </h2>
La funcion jugarPartida() ahora integra gran parte de codigo del cuerpo del resto de funciones.

El juego es funcional en cierto modo. Faltan cambios por hacer.
<br>
<br>
<br>
<br>

<h2> COMMIT #7 --> Colores en las Fichas </h2>
He cambiado el color de las fichas utilizando el paquete colorama de Python.

Ahora las fichas X del Jugador_1 se marcan en **ROJO**, y las fichas del Jugador_2 se marcan en **verde**.



<br>
<br>
<br>
<br>

<h2> Futuros Commit's </h2>
  - No se anaden fichas a partir de la segunda fila desde debajo.
  
  - Si existe una ficha en una columna y el otro jugador introduce una ficha suya en esa columna, la ficha existente se sustituye.
  
  - Hay ocasiones en los que ciertos fallos no estan contemplados, y el programa rompe.
  
  - Al introducir fichas, el numero de la columna no corresponde con el numero correcto ( numero 0 == columna 1; numero 1 == columna 2 ...)
  
  - IA
  
  - ...


