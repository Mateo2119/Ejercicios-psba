# -*- coding: utf-8 -*-
"""
Escribir un programa que sume, independientemente, los elementos positivos y negativos de
la una matriz de 5x5, la matriz se debe llenar solicitando los datos al usuario. 
"""
filas = 5
columnas = 5
sum_pos = 0
sum_neg = 0
numero = 0
matriz = []

for a in range(filas):
    matriz.append([0]*columnas)

for i in range(filas):
    for j in range(columnas):
        numero = int(input(f"Ingrese el numero para la posicion [{i}] [{j}]: "))
        matriz[i][j] = numero
        if numero >= 0:
            sum_pos = sum_pos + numero
        else:
            sum_neg = sum_neg + numero 
            
print(f"\nLa suma de los elemenos positivos es: {sum_pos} y la de los negativos es: {sum_neg}")
        
