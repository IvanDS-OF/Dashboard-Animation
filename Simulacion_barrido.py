#Orueba de PLOTS
import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np
#import seaborn as sb

df = pd.read_csv("DATOS.csv")
data_1 = df["UNO"]
data_2 = df["DOS"]
data_3 = df["TRES"]
data_4 = df["CUATRO"]

guardar=[]

data_vector = [data_1,data_2,data_3,data_4]
x = np.arange(0,101,1)
es = np.arange(0,20,1)

fig, axs = plt.subplots(2,2)

for n in range(80):
    for i in range(4):
        
        datos = data_vector[i]    

        datos_plot = datos[n:n+20]
        
        guardar.append(datos_plot)
    
    
    axs[0,0].set_title("A")
    axs[0,0].plot(es,guardar[0], c="r")
    axs[0,0].axis([0, 23, -2, 2])

    axs[0,1].set_title("B")
    axs[0,1].plot(es,guardar[1], c="c")
    axs[0,1].axis([0, 23, -2, 2])

    axs[1,0].set_title("C")
    axs[1,0].plot(es,guardar[2], c="k")
    axs[1,0].axis([0, 23, -2, 2])

    axs[1,1].set_title("D")
    axs[1,1].plot(es,guardar[3], linewidth = "2")
    axs[1,1].axis([0, 23, -2, 2])
    
    plt.pause(0.01)

    axs[0,0].cla()
    axs[0,1].cla()
    axs[1,0].cla()
    axs[1,1].cla()

    guardar=[]




