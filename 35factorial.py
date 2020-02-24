numero = int(input("Ingrese el número: "))
factorial = 1

for i in range(1,numero+1):
    factorial = factorial * i
    
print(factorial)