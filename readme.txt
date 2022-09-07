Versión de Python utilizada: 3.10
Librerías y paquetes utilizados se encuentran en requirements.txt

Integrates:
- Diego Caceres
- Matías Vergara
- Elías Ocque (en Educandus como Ibrahim Totesaut)

Notas adicionales:
- **El main del programa se encuentra en la clase race.py**
- El algoritmo Minimax y Alpha-Beta es lo suficientemente inteligente para saber que si
el j1 tiene acceso inmediato al nodo final, moverse al nodo final acabará el juego de forma
inmediata sin darle siquiera un turno al j2 (haciendo que el j1 gane por defecto) y, por lo tanto,
casi siempre tomará esta opción de estar disponible
- En el grafo, el rojo representa a MAX (j1) y el azul a MIN (j2)
- En los grafos generados, si se observa un color morado, 
es debido a que ambos jugadores tomaron ese camino

Código referenciado:
- Game y Search: https://github.com/aimacode/aima-python/blob/master/games4e.ipynb
- Grafos: https://networkx.org/documentation/stable/reference/introduction.html
