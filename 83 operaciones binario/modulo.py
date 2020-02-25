# -*- coding: utf-8 -*-
"""
Crear un módulo que maneje funciones para operar en sistema binario, las operaciones que
se deben implementar son suma, resta, multiplicación y división.

"""
def a_entero(num):
     l = len(num) - 1
     entero = 0
     for i in num:
          potencia = 2 ** l
          entero = entero + ( int(i) * potencia)
          l = l - 1
     return entero

def a_binario(num):
     binario = ""
     while (True):
          aux = str( num % 2 )
          num = int( num / 2 )
          binario = aux + binario
          if (num <= 1):
               binario = ( str( num ) if num > 0 else "" ) + binario
               break
     return binario
    
def sum_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_binario(b1+b2)

def res_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_binario(b1-b2)

def div_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_binario(b1/b2)

def mul_bin(a,b):
    b1 = a_entero(a)
    b2 = a_entero(b)    
    return a_binario(b1*b2)



