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

<h2> COMMIT #7 --> Colores en las Fichas </h2>
Se ha corregido un error que impedia insertar fichas a partir de la segunda columna desde debajo.

Se ha corregido el error de seleccionar la columna para jugar. 
Si ahora se selecciona como columna el valor '1', se insertara la ficha en la columna 1 (antes valor '1' insertaba en la columna 2).

Si un jugador introduce una ficha en otra columna donde ya hay una ficha, esta se coloca por encima (antes, la ficha que introduciamos se sustituia por la que ya estaba, no se colocaba arriba).
<br>
<br>
<br>
<br>

<h2> COMMIT #8 --> Control de los turnos </h2>
Ahora, si ocurre que durante el transcurso del turno de un jugador, este intenta introducir una ficha suya en una columna que no existe dentro del tablero, o en una columna que ya esta llena de fichas, NO SE PERDERA el turno del jugador, y podra volver a jugar para introducir su ficha en una columna que si sea valida.

Lo que ocurria antes si esto pasaba, es que el jugador que habia generado la excepcion perdia su turno. El juego seguia su curso y le tocaba jugar al jugador contrario.
<br>
<br>
<br>
<br>

<h2> COMMIT #9 --> Manejo de errores 1/2 </h2>
Es este commit he modificado el trascurso del programa cuando se introducian valores no permitidos en la creacion de la partida.

Si bien es cierto que ya estaban implementadas estructuras de manejo de excepciones, segun iba creciendo la funcion principal de jugarPartida(),
el programa no tenia ninguna ruta definida en el caso de haberse generado una excepcion.

Ahora esto esta solucionado, y el programa avisa con un mensaje en la terminal cuando se ha generado alguna excepcion.
<br>
<br>
<br>
<br>

<h2> COMMIT #10 --> Manejo de errores 2/2 </h2>
Ahora el programa controla todas las excepciones que se puedan generar al momento de el usuario interactuar con la partida.

Los mensajes de aviso al causar una excepcion se marcan en color rojo cuando los genera el Jugador_1, y en color verde cuando los genera el Jugador_2.
<br>
<br>
<br>
<br>

<h2> Futuros Commit's </h2>

  - Incluir en la partida un boton ('Pulsa "k" para salir de la partida.') y generar un mensaje por pantalla y el fin del juego.
  
  - El juego debe detectar cuando se han unido 4 fichas del mismo tipo para que un jugador gane.
  
  - IA
  
  - ...


