age = int(input("Entrer votre age : "))
prenom = input("Enter you firstname :")
is_man = input("What is your gender :(Homme/Femme/Other)")

is_graduate = True
height = 189

if is_man == "Femme" or is_man == "Other" or is_man == "femme" or is_man == "other":
    is_man = False
else:
    is_man = True

# Categorie a = sexe:Homme, age:35-, taille:>160, graduate:Vrai
if age <=35 and is_man and height > 160 and is_graduate:
    category = "A"
else:
    if age <=35 and is_man and height > 160 and not is_graduate:
        category = "B"
    else:
        category = "C"

print("ma categorie : " + category)




