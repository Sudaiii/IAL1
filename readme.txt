Version de Python utilizada: 3.10
Librerias y paquetes utilizados se encuentran en requirements.txt

Notas adicionales:
- El algoritmo Minimax y Alpha-Beta es lo suficientemente inteligente para saber que si
el j1 tiene acceso inmediato al nodo final, moverse al nodo final acabara el juego de forma
inmediata sin darle siquiera un turno al j2 (haciendo que el j1 gane por defecto) y, por lo tanto,
casi siempre tomara esta opción de estar disponible