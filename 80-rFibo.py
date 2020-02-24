# -*- coding: utf-8 -*-
"""
Escribir un programa que mediante funciones recursivas calcule el termino “x” de la serie de
fibonacci. 
"""

numero = int(input("Digite el número: "))

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(f"el numero es: {fibo(numero)}")