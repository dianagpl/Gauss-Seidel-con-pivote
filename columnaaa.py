# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:27:22 2021

@author: FERNANDA RAMIREZ
"""

import numpy as np


A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

B = np.array([[60.70],
              [92.90],
              [56.30]])


# Matriz aumentada
AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)


tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]


for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:]  = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal

# SALIDA
print('Matriz aumentada:')
print(AB0)
print('Pivoteo en columna: ')
print(AB)