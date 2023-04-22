# punto 1
numero = int(input("ingrese la cantidad de numeros a leer: "))
pares = 0
impares = 0

for i in range(numero):
    leer = int(input("Ingrese un número para determinar si es par o impar: "))
    if leer % 2 == 0:
        pares = pares+1
    else:
        impares = impares+1

print("La cantidad de números pares es:", pares)
print("La cantidad de números impares es:", impares)
