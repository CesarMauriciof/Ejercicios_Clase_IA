# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:59:34 2026

@author: 1059356199
"""

# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np   #libreria para trabajr con arreglos 
import matplotlib.pyplot as plt  #libreria para graficar

# 1 definir l funcion objetivo que sera optimizada

def f(x):
    return x**4 - 3*x**3 + 2

#2  definir el gradiente dela funcion

def gradient (x):
    return 24*x - 18

#3 defino gradiente descendente

def gradien_descent(x_start, alpha, num_iterations):
    x = x_start
    trayectory = [x]
    for _ in range(num_iterations):
        x = x - alpha* gradient(x)# actualizar la trayectoria del gradiente
        trayectory.append(x)      # almacena la nueva solución
    return np.array(trayectory)  # devuelve los valores almacenados del gradiente

#4 inicializar los parametros del gradiente


x_start = 2  # inicializar x en un lugar aleatorio de la función
alpha = 0.005
num_iterations =3


trayectory = gradien_descent(x_start, alpha, num_iterations)

#5 grafica la función objetivo y sus soluciones

x = np.linspace(-1, 3, 400)
y = f (x)

plt.figure(figsize=(10, 10))
plt.plot(x,y, label='$f(x)=x^4 - 3*x^3 + 2', color = 'blue')
plt.scatter(trayectory, f(trayectory), color= 'red', zorder=5)
plt.plot(trayectory, f(trayectory), color = 'red', linestyle = "--", label='trayectoria del gradiente')
plt.xlabel('$x$')
plt.xlabel('$f(x)$')
plt.title('gradiente descendente')
plt.legend()
plt.grid(True)
plt.show()















        











