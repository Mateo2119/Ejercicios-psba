# -*- coding: utf-8 -*-
"""
Escribir un programa que implemente un calendario perpetuo, es decir, que dado una fecha
en formato mes, día y año le retorne al usuario el día de la semana que corresponde para esta
fecha.

@author: lenovo
"""
dia = int(input('Dia de nacimiento: '))
mes = int(input('Mes de nacimiento: '))
año = int(input('Anio de nacimiento: '))

while año < 1583:
  print('fecha muy baja')
  año = int(input('Año de nacimiento: '))
else:
  a = (14 - mes) // 12
  y = año - a
  m = mes + 12 * a - 2 
  d = (dia + año + (año//4) - (año//100) + (año//400) + ((31 * m)//12)) % 7
 
  if d == 0:
    dia_s = 'Domingo'
  elif d == 1:
    dia_s = 'Lunes'
  elif d == 2:
    dia_s = 'Martes'
  elif d == 3:
    dia_s = 'Miercoles'
  elif d == 4:
    dia_s = 'Jueves'
  elif d == 5:
    dia_s = 'Viernes'
  else:
    dia_s = 'Sabado'
 
  print(f"El {dia}/{mes}/{año} fue un {dia_s}")
