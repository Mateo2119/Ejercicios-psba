print("Ingrese la base")
base = int(input())
while base < 0:
    print("Ingrese la base")
    base = int(input())
print("Ingrese la altura")
altura = int(input())
while altura <0:
    print("Ingrese la altura")
    altura = int(input())

area = (base*altura)/2
print(f"El area es: {area}")
