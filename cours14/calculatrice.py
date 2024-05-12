def addition(l):
    total = l[0]

    for e in l[1:]:
        total += e

    return total

def soustraction(l):
    total = l[0]

    for e in l[1:]:
        total -= e

    return total

def multiplication(l):
    total = l[0]

    for e in l[1:]:
        total *= e

    return total

def division(l):
    total = l[0]

    for e in l[1:]:
        total /= e

    return total

def factorielle(n):
    total = 1
    for i in range(2, n+1):
        total *= i
    return total


def calcul(l,type):
    if len(l) == 0:
        return "Au moin un nombre est nécéssaire"
    elif len(l) == 1:
        if type == "+":
            return addition([l[0],l[0]])
        elif type == "-":
            return soustraction([l[0],l[0]])
        elif type == "*":
            return multiplication([l[0],l[0]])
        elif type == "/":
            return division([l[0],l[0]])
        elif type == "!":
            return factorielle(int(l[0]))
        
    if type == "+":
        return addition(l)
    elif type == "-":
        return soustraction(l)
    elif type == "*":
        return multiplication(l)
    elif type == "/":
        return division(l)
    elif type == "!":
        return "Une factorielle ne peux pas prenre plusieurs valeurs"

def main():
    choix = input("Addition (+), Soustraction (-), multiplication (x) ou division (/) :")

    nombre = ""
    l = []

    while nombre != "exit":
        nombre = input("Entre un nombre (exit pour terminer): ")
        
        if nombre.isdigit():
            l.append(float(nombre))
        elif nombre != "exit":
            print("ceci n'est pas un nombre !")

    reponse = calcul(l,choix)

    print(reponse)

if __name__ == "__main__":
    main()