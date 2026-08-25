# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:15:57 2024

@author: Camilo
"""

import numpy as np   #libreria para trabajr con arreglos 
import matplotlib.pyplot as plt  #libreria para graficar

# 1 definir l funcion objetivo que sera optimizada

def f(x):
    return x**2

#2  definir el gradiente dela funcion

def gradient (x):
    return 2 * x

#3 defino gradiente descendente

def gradien_descent(x_start, alpha, num_iterations):
    x = x_start
    trayectory = [x]
    for _ in range(num_iterations):
        x = x - alpha* gradient(x)# actualizar la trayectoria del gradiente
        trayectory.append(x)      # almacena la nueva solución
    return np.array(trayectory)  # devuelve los valores almacenados del gradiente

#4 inicializar los parametros del gradiente


x_start = 6  # inicializar x en un lugar aleatorio de la función
alpha = 1.0
num_iterations = 15


trayectory = gradien_descent(x_start, alpha, num_iterations)

#5 grafica la función objetivo y sus soluciones

x = np.linspace(-6, 6, 400)
y = f (x)

plt.figure(figsize=(8,6))
plt.plot(x,y, label='$f(x)=x^2', color = 'blue')
plt.scatter(trayectory, f(trayectory), color= 'red', zorder=5)
plt.plot(trayectory, f(trayectory), color = 'red', linestyle = "--", label='trayectoria del gradiente')
plt.xlabel('$x$')
plt.xlabel('$f(x)$')
plt.title('gradiente descendente')
plt.legend()
plt.grid(True)
plt.show()















        











