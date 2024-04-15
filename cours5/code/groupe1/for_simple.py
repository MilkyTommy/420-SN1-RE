n = int(input("Entre un nombre entre 0 et 100 : "))

# Execute le code à l'interieur de l'indendation n fois
for x in range(n) :
    print(x)

# Execute le code à l'interieur de l'indendation n fois
# de 1 à n+1 fois
for x in range(1,n+1) :
    print(x)

# Execute le code à l'interieur de l'indendation de 0 à 100
# avec un saut de n nombre
for x in range(0,100,n) : 
    print(x)