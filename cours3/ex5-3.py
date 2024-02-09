first_name = input("Quel est votre prénom ? : ")

age = int(input("Quel est votre age ? (en année): "))

height = int(input("Quel est votre grandeur ? (en cm): "))

is_man = input("Quel est votre sexe ? (Homme/Femme/Autre) : ")

if is_man == "Homme" :
    is_man = True
else :
    is_man = False

category = "A"

if (age < 18 or age > 65) and (not is_man) or height > 1000 :
    category = "B"
else :
    if is_man and height < 150 :
        category = "Short"

print(category) 

premium_member = False

if age >= 65 and is_man or first_name == "Tommy" :
    premium_member = True
else :
    if not is_man and (age >= 18 and age<= 65) and height > 120 and height > 120:
        premium_member = True

print(premium_member)

if not (is_man and (age >= 18 and age<= 65) and height > 120 and height > 120):
    premium_member = True

if not is_man and age >= 18 and age<= 65 and height > 120 and height > 120:
    premium_member = False