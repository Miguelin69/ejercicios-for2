multiplo = 0
multiplo2 = 0
for i in range(1000, 5000):
    if i % 7 == 0:
        multiplo = multiplo + 1
    elif i % 9 == 0:
        multiplo2 = multiplo2 + 1

print("Los multiplos de 9 son: " , str(multiplo2))
print("Los multiplos de 7 son: " , str(multiplo))