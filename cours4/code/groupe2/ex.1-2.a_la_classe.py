# accepter si 
# age entre 16 25, 
# plus grand ou egal que 180 si homme
# plus grand ou 160 si femme ou autre
# si son nom n'est pas vide

nom = input("le nom : ")
age = int(input("le age : "))
genre = input("le genre : ")
grandeur = int(input("la grandeur : "))


if (nom != "" 
    and age >=16 and age <=25 and 
    ((genre == "homme" and grandeur >=180) or 
     (genre == "femme" 
      or genre =="autre" and grandeur >=160))) :
    print("tu as reussi")
else :
    print(" :( ")