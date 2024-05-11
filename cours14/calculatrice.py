def add(l):
    total = l[0]
    # [1:] précise que l'on veut tout sélectionner à 
    # l'exception de la première valeur
    for e in l[1:]: 
        total += e

    return total

def sous(l):
    total = l[0]

    for e in l[1:]:
        total -= e

    return total

def div(l):
    total = l[0]

    for e in l[1:]:
        total /= e

    return total

def multi(l):
    total = l[0]

    for e in l[1:]:
        total *= e

    return total

def fact(n):
    total = 1
    for i in range(2, n+1):
        total *= i
    return total

choix = input("Addition (+), Soustraction (-), multiplication (x),division (/) ou factorielle (!) :")

nombre = ""
l = []

while nombre != "exit":
    nombre = input("Entre un nombre (exit pour terminer): ")
    
    if nombre.isdigit():
        l.append(float(nombre))
    elif nombre != "exit":
        print("ceci n'est pas un nombre !")

reponse = ""
if choix == "+":
    reponse = add(l)
elif choix == "-":
    reponse = sous(l)
elif choix == "x":
     reponse= multi(l)
elif choix == "/":
     reponse= div(l)
elif choix == "!":
     reponse= fact(l[0])

print(reponse)
