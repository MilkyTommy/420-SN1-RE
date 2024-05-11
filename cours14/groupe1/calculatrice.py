def add(l):
    total = l[0]

    for e in l[1:]:
        total += e

    return total

def sou(l):
    total = l[0]

    for e in l[1:]:
        total -= e

    return total

def div(l):
    total = l[0]

    for e in l[1:]:
        total /= e

    return total

def mul(l):
    total = l[0] 

    for e in l[1:]:
        total *= e

    return total

choix = input("Addition (+), Soustraction (-), multiplication (x) ou division (/) :")

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
    reponse = sou(l)
elif choix == "x":
     reponse= mul(l)
elif choix == "/":
     reponse= div(l)
else:
    pass #reponse = factorielle(l[0])

print(reponse)
