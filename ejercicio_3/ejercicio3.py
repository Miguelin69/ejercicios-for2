ndados = int(input("ingrese la cantidad de numeros a leer: "))
cara1 = 0
cara2 = 0
cara3 = 0
cara4 = 0
cara5 = 0
cara6 = 0

for i in range(ndados):
    
    if ndados  == 1:
        cara1 = cara1+1
    if ndados  == 2:
        cara2 = cara2+1
    if ndados  == 3:
        cara3 = cara3+1
    if ndados  == 4:
        cara4 = cara4+1
    if ndados  == 5:
        cara5 = cara5+1
    if ndados  == 6:
        cara6 = cara6+1
    

print(f"La cantidad de caras en 1 es:", str(cara1))
print(f"La cantidad de caras en 2 es:", str(cara2))
print(f"La cantidad de caras en 3 es:", str(cara3))
print(f"La cantidad de caras en 4 es:", str(cara4))
print(f"La cantidad de caras en 5 es:", str(cara5))
print(f"La cantidad de caras en 6 es:", str(cara6))