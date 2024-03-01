num = int(input("Entrer un nombre de votre choix:"))

def decimalToBinary(n, b = ""):

    if(n != 0) :
        if  n % 2 == 0:
            b = "0" + b
        else:
            b = "1" + b
        return decimalToBinary(n//2,b)
    
    return b

print(f"Votre nombre est {num}.")
print(f"Son équivalent binaire est {decimalToBinary(num)}.")