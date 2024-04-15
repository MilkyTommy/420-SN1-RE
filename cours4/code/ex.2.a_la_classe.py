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

 
if(age >= 16 and age <= 25) :
    age_requis = True
else :
    age_requis = False

if (not age_requis):
    print("lol")