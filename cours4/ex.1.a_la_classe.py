#vous voulez faire partie  
# de l'equipe de volleyball

# valider son nom, age, sexe et grandeur
age = int(input("votre age : "))
name = input("votre nom : ")
height = float(input("Votre grandeur: "))
gender = input("votre sexe : ")

# accepter si 
# age entre 16 25, 
# plus grand ou egal que 180 si homme
# plus grand ou 160 si femme ou autre
# si son nom n'est pas vide
if (name != "" and ((gender == "homme" and height >=180) or (gender == "femme" or gender == "autre" and height >=160)) and age >=16 and age <=25):
    print("you got it bro")
else:
    print("too bad short guy")