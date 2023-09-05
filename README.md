# Dashboard-Animation
Dashboard animation

Este repositorio muestra cómo programar con Python 3.8 una animación del comportamiento de la lectura de una base de datos, o en su defecto, una lectura de algún sensor analógico en tiempo real. 


Dentro de Python es posible realizar animaciones ó simulaciones de comportamiento usando solamente la librería de **matplotlib**


### Programa principal

Primero tememos que importar las librerías necesarias para el correcto funcionamiento del programa, así como son: 

```
import matplotlib.pyplot 
import time
import pandas as pd
import numpy as np
```

Luego tenemos que leer con pandas los datos para poder crear un vector el cual será leído de forma iterada: 

Con comandos de pandas creamos nuestro dataFrame y separamos los datos que serán mostrados a manera de listas:

```
df = pd.read_csv("DATOS.csv")
data_1 = df["UNO"]
data_2 = df["DOS"]
data_3 = df["TRES"]
data_4 = df["CUATRO"]
```

**Nota:** En caso de que sea la lectura de un sensor y en tiempo real, solo al inicio es necesario inicializar el vector, puede ser una lista de 0's. 


Posteriormente, declaramos un vector vacio para guardar datos después: 

Creamos una matriz llamada **data_vector** que es en donde se van a almacenar todos los datos _(previamente guardados y medidos)_

Creamos una lista llamada **x** para almacenar los datos que serán mostrados en la animación correspondiente a cada vector de la información disponible. 

Inicializamos la figura con comandos de matplotlib y comenzamos los ciclos para mostrar la información. **Nota: En este caso se realizará mediante un ciclo "for" ya que la información / base de datos que se tiene ed estática y no se renueva cada cierto tiempo como puede llegar a ocurrir cuando se tiene un sensor conectado a un proceso de producción**

### For's

Se tienen dos ciclos anidados: El primero es para iterar la información guardada almacenada, que es la que será mostrada en las gráficas y el segundo ciclo es para iterar la gráfica y dentro de la figura: Debido a que se tienen 4 diferentes columnas de datos, es necesario iterar entre las columnas de datos

La lógica general del programa es el siguente: Vamos a tomar los primeros 20 valores de las listas en un inicio para generar la gráfica y luego vamos a mover el índice de los datos sumando una unidad: 

En la primera muestra se plotean del 0 al 20, en la segunda muestra se van a plotear del 1 al 21, y así de forma consecutiva.

Los comandos posteriores son para hacer el muestreo de los datos con los comandos de matplotlib.

Dos comandos importantes que nos son de gran utilidad para realizar la animación son: 

```
plt.pause(0.01)
axs[0,0].cla()
```

Gracias a la combinación de estos dos comandos podemos hacer la animación, el primer comando nos ayuda a mantener por un breve momento los datos que son ploteados, y el segundo comando es para eliminar la información que se muestra en la imagen, y así de forma iterativa.

Al final se manda a borrar la información que tiene la variable "guardar" ya que de no hacerlo puede mostrar cosas confusas en las imágenes















































