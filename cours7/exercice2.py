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
