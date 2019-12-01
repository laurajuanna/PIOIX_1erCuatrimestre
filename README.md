# GENERALA

## Introducción

La generala es un juego de dados. Se juega con cinco dados y un cubilete; el número de jugadores es ilimitado, pero lo ideal es de 3 a 5. El objetivo del juego es lograr la mayor puntuación, de acuerdo a la valoración establecida para cada jugada posible en el juego, llamada categoría.

## Iniciar el juego
Para comenzar a jugar es necesario correr el archivo `principal.py` a través de la terminal de Python.

## Diagrama de flujo del programa

![diagrama-generala](/diagrama.jpeg)

- [Click acá para ver la imagen en tamaño grande](https://raw.githubusercontent.com/laurajuanna/TP-Final-Generala/master/diagrama.jpeg).

## Juego

### Categorias
- 1 : se coloca el número que dé la suma de 1 obtenidos.
- 2 : se coloca el número que dé la suma de 2 obtenidos.
- 3 : se coloca el número que dé la suma de 3 obtenidos.
- 4 : se coloca el número que dé la suma de 4 obtenidos.
- 5 : se coloca el número que dé la suma de 5 obtenidos.
- 6 : se coloca el número que dé la suma de 6 obtenidos.
- Escalera: 25 puntos si es servida, 20 si fue armada.
Se forma con una progresión de números. Hay dos posibilidades: 1-2-3-4-5 (escalera menor) y 2-3-4-5-6 (escalera mayor).
- Full: 35 puntos si es servido o 30 puntos si es armado. Se forma con dos grupos de dados iguales, uno de tres y otro de dos dados.
- Póker: 45 puntos si es servido o 40 puntos si es armado. Se forma con cuatro dados iguales.
- Generala: 50 puntos si se logra formar cinco números iguales en dos o tres tiros.
- Generala Doble: 60 puntos si se logra formar dos generalas en dos tiros de tres.
- Generala Servida: Cuando se logra la Generala de un solo tiro, se llama generala servida y el jugador automáticamente gana el juego.

### Nota y aclaraciones
Una vez lograda una categoría esta se considera "Cerrada", es decir, si el jugador la repite no la podrá usar, de tal forma que tendrá que buscar otra posible categoría con la combinación de dados obtenida. Por ejemplo, si el jugador tira 4-4-2-2-2, si ya había anotado el full, puede anotar la tirada en la categoría del 4 o del 2.

Ningún jugador está obligado a elegir una categoría hasta que él decida o hasta su tercer tiro. De tal forma que si un jugador hace en su primer tiro un "juego mayor", puede arriesgarse si quiere a intentar otra categoría tomando inclusive los cinco dados. Luego que un dado ha sido apartado no se lo puede volver a usar.

Si al terminar una tirada el jugador no puede armar un juego conveniente en ninguna de sus categorías abiertas, deberá elegir alguna y tachar la casilla correspondiente, con lo que quedará cerrada. Cuando se han completado las once vueltas del juego (o diez según si así se decidió), se sumarán los puntos. Si el juego elegido por el usuario resultó en la primera tirada y coincide con las categorías
escalera, full, poker, se adiciona 5 puntos extras.

### Puntajes
- Escalera: 20/25 (normal/servida)
- Full: 30/35 (normal/servida)
- Poker: 40/45 (normal/servida)
- Generala: 50/60 (normal/doble)

### Requerimientos
- El juego debe soportar “N” jugadores.
- Cada jugador tiene hasta 3 oportunidades para tirar sus dados
- Cada jugador debe poder elegir cuales de los 5 dados conservar y cuáles volver a
arrojar.
- Determinar cada uno de los puestos, desde el ganador hasta el perdedor.
- Tabla con resultados Parciales por cada tirada si se desea y Finales al terminar.

### Ejemplo de tabla con resultados parciales:
```
Alan,Luis,Maria
[1​, 3, 3, 2 ]
[2​, 6, 4, 2 ]
[3​, 6, 9, 6 ]
[4​, -, 20, 3 ]
[5​, 25, -, 6 ]
[6​, 6, 6, - ]
[E​, -, 20, 20 ]
[F​, 30, -, - ]
[P​, -, -, - ]
[G​, -, -, - ]
[DG​, -, -, - ]
Totales:
```
### Ejemplo de tabla con resultados Finales:
```
Alan,Luis,Maria
[1​, 3, 3, 2 ]
[2​, 6, 4, 2 ]
[3​, 6, 9, 6 ]
[4​, 24, 20, 3 ]
[5​, 25, 20, 6 ]
[6​, 6, 6, 6 ]
[E​, 20, 20, 20 ]
[F​, 30, 35, 30 ]
[P​, 45, 40, 0 ]
[G​, 50, 0, 0 ]
[DG​, 0, 0, 0 ]
Totales:
```
