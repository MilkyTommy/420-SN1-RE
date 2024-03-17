# Voici une liste de personnes fictives. 
# Imprime à l'écran la liste complète des personnes selon les critères suivants.

#Critère #1 :
# Demande à l'utilisateur de choisir parmi une selection de choix.
# Les choix sont : 
#   1. Affiche les personnes par 'prénom'
#   2. Affiche les personnes par 'nom'
#   3. Affiche les personnes par 'nom de jeune fille'
#   4. Affiche les personnes par 'nom','prénom' et 'Age'

#Critère #2 :
# Si l'utilisateur entre un choix invalide, 
# il faut demander indéfiniment jusqu'à ce qu'il entre un choix valide.

# INDICES:
# 1. Pour selectionner une personne dans une liste de personnes, il faut faire :
#   personnes[0]
# 2. Pour selectionner le prénom d'une personne, il faut faire 
#   personne['firstName']
# 3. Donc pour selectionner l'age de la 4ième personne dans la liste de personne, il faudrait faire :
#   personnes[3]['age']
# 4. Il faut utiliser la boucle for pour itérer parmi les personnes (Critère #1).
# 5. Il faut utiliser la boucle while pour demander un choix valide (Critère #2).



# Cette liste est plus complexe. Il s'agit d'une liste de dictionnaire.
# Un dictionaire est une suite de "clé" : "valeur". Il faudra donc utiliser une boucle for
# pour parcourir chaque élément de la liste 'personnes'.
# Ex. personnes[0] retourne {"id":1,"firstName":"Terry","lastName":"Medhurst", ...}
# Puis, il faut selectionner les informations d'une personne avec la clé correspondant.
# Ex. personnes[3]["firstName"] -> "Miles"
personnes = [
   {
      "id":1,
      "firstName":"Terry",
      "lastName":"Medhurst",
      "maidenName":"Smitham",
      "age":50
   },
   {
      "id":2,
      "firstName":"Sheldon",
      "lastName":"Quigley",
      "maidenName":"Cole",
      "age":28
   },
   {
      "id":3,
      "firstName":"Terrill",
      "lastName":"Hills",
      "maidenName":"Hoeger",
      "age":38
   },
   {
      "id":4,
      "firstName":"Miles",
      "lastName":"Cummerata",
      "maidenName":"Maggio",
      "age":49
   },
   {
      "id":5,
      "firstName":"Mavis",
      "lastName":"Schultz",
      "maidenName":"Yundt",
      "age":38
   },
   {
      "id":6,
      "firstName":"Alison",
      "lastName":"Reichert",
      "maidenName":"Franecki",
      "age":21
   },
   {
      "id":7,
      "firstName":"Oleta",
      "lastName":"Abbott",
      "maidenName":"Wyman",
      "age":31
   },
   {
      "id":8,
      "firstName":"Ewell",
      "lastName":"Mueller",
      "maidenName":"Durgan",
      "age":29
   },
   {
      "id":9,
      "firstName":"Demetrius",
      "lastName":"Corkery",
      "maidenName":"Gleason",
      "age":22
   },
   {
      "id":10,
      "firstName":"Tommy",
      "lastName":"Joyal",
      "maidenName":"Gagnon",
      "age":99
   }
]


# Mise en page pour afficher tous les choix possibles.
print("1. Affiche les personnes par 'prénom'")
print("2. Affiche les personnes par 'nom'")
print("3. Affiche les personnes par 'nom de jeune fille'")
print("4. Affiche les personnes par 'nom','prénom' et 'Age'")
choix = input("Votre choix : ")

# Demande d'entrer un choix tant que le choix est différent de 1,2,3 et 4.
# Puisque le choix n'a pas été converti en entier (avec int("1")), le choix est une chaîne
# de caractères. Il faut donc comparer la variable choix avec des chaînes comme 
# "1","2","3" ou "4".
while choix != "1" and  choix != "2" and choix != "3" and choix != "4":
    print("Choix éronné, veuillez réessayer.")
    choix = input("Votre choix : ")

# Cette boucle parcourera chaque personne dans la liste 'personnes' et mettrera le contenu dans la 
# variable personne. Il faudra ensuite afficher le contenu demandé, selon le choix.
# Ex. Si le choix est "1", on affiche le prénom de chaque personne.
for personne in personnes :
    if choix =="1" : print(personne['firstName'])
    elif choix =="2" : print(personne['lastName'])
    elif choix =="3" : print(personne['maidenName'])
    else : print(personne['lastName'],",",personne['firstName'],",", personne['age'])
    