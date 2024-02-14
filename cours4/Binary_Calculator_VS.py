b_num = ""
num = int(input("Entrer un nombre de votre choix:"))
first_num = num

def binary_calc():
    global num
    global b_num
    if  num % 2 == 0:
        b_num = "0" + b_num
    else:
        b_num = "1" + b_num
    num = num // 2
    ###TEST print(f"{num}")
    

while num != 0:
    binary_calc()

print(f"Votre nombre est {first_num}.")
print(f"Son équivalent binaire est {b_num}.")