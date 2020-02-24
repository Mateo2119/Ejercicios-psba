print("Ingrese A")
A = int(input())

print("Ingrese B")
B = int(input())
while B == 0:
    print("Ingrese un B válido")
    B = int(input())

entero = A//B
residuo = A%B

print(f"División entera: {entero}\nResiduo: {residuo}")
