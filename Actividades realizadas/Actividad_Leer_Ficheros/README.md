# Ejercicio: Lectura de Archivos en Python

![Logo de Python](https://www.python.org/static/community_logos/python-logo.png)

## Descripción

*Este ejercicio fue realizado durante 1ºCFGM SMR - Fundamentos de la Programación.*

El objetivo de esta actividad es aprender a leer archivos en Python utilizando la función `open()` y procesar su contenido adecuadamente.

## Objetivos

1. Abrir el archivo `hechos.txt` en modo lectura.
2. Leer todo el contenido del archivo.
3. Imprimir el contenido en pantalla precedido por el mensaje:*"Lo siguiente fue leído del archivo: hechos.txt"*

## Código en Python

```python
# Roberto Carrascoso Jordán - 1ºCFGM SMR
# Actividad Leer Ficheros

with open ("./hechos.txt", "r") as file:
    archivo = file.readlines()
    print("\nLo siguiente fue leído del archivo: hechos.txt")


```

## Resultados esperados

Al ejecutar el script correctamente, la salida en la terminal debería ser similar a:

```
Lo siguiente fue leído del archivo: hechos.txt

```

Este ejercicio ayuda a comprender la lectura de archivos en Python y la manipulación de datos de texto.

---

**Autor:** Roberto Carrascoso Jordán