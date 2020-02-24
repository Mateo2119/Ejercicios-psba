# -*- coding: utf-8 -*-
"""
73. Escribir un programa que usando funciones lea una serie de números hasta que este numero
sea de un solo dígito y muestre en pantalla:
• Cuantos de estos números son palíndromos.
• Listar cuantas veces aparece cada dígito en la lista.
• Mostrar el promedio de los números leídos.
• La sumatoria de los números pares.
• La sumatoria de los números impares.
• La sumatoria de los dígitos pares.
• La sumatoria de los dígitos impares.
"""

lista = []

numero = int(input("Escriba el numero: "))

while numero > 9 or numero < -9:
    lista.append(numero)
    numero = int(input("Escriba el numero: "))
    
print(lista)

def palindromos(lis):
    palindromos = 0
    for i in lis:
        revez = ""
        for j in reversed(str(i)):
            revez = revez + j
            if str(i) == revez:
                palindromos = palindromos + 1
    return palindromos

def apariciones(lis):
    apariciones = []
    for i in lis:
        num_apar = 0        
        for j in lis:
            if i == j:
                num_apar = num_apar +1
        apariciones.append(num_apar)
    return apariciones

def promedio(lis):
    promedio = 0
    total = 0
    for i in lis:
        total = total + i
    promedio = total/len(lista)
    return promedio

def sum_pares(lis):
    suma = 0
    for i in lis:
        if i%2 == 0:
            suma = suma + i
    return suma

def sum_impares(lis):
    suma = 0
    for i in lis:
        if i%2 == 1:
            suma = suma + i
    return suma

def cantidad_pares(lis):
    suma = 0
    for i in lis:
        if i%2 == 0:
            suma = suma + 1
    return suma

def cantidad_impares(lis):
    suma = 0
    for i in lis:
        if i%2 == 1:
            suma = suma + 1
    return suma

print(f"\nEn: {lista} hay {palindromos(lista)} palindromos")
print(f"\nEn: la lista hay {apariciones(lista)} apariciones")
print(f"\nEl promedio es: {promedio(lista)}")
print(f"\nLa suma de los pares es: {sum_pares(lista)}")
print(f"\nLa suma de los impares es: {sum_impares(lista)}")
print(f"\nLa cantidad de pares es: {cantidad_pares(lista)}")
print(f"\nLa cantidad de impares es: {cantidad_impares(lista)}")