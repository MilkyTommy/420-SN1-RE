# Voici une liste des prénoms les plus populaires en france en 2023.
# Votre programme doit demander à l'utilisateur d'écrire au clavier son nom, puis valider plusieurs choses :
#   1. Valide si son nom est un prénom valide ( sans chiffre).
#      Si le nom est non valide, il faut demander indéfiniment jusqu'à ce qu'il entre un choix valide.
#   2. Regarde si le nom est déjà dans la liste. 
#       Si le nom est dans la liste, afficher seulement 'Déjà présent'.
#       Sinon, afficher le nom inscrit.

# INDICES : 
#   1. str.isalpha() retourne Vrai seulement si uniquement des caractères sont présents dans le mot.
#   2. str.lower() retourne le mot uniquement en minuscule.
#   3. str.upper() retourne le mot uniquement en majuscule.
#   4. str.title() retourne le mot avec une majuscule comme première lettre, suivi de minuscules.
# str -> la chaîne de charactère que tu veux tester.

liste_de_nom = [
    "GABRIEL",
    "adam",
    "Raphaël",
    "LOUis",
    "LouiSe",
    "aLMa",
    "nOAh",
    "Isaac",
    "MoHameD",
    "aRTHUr",
    "Gaspard",
    "JosEph",
    "AlIce",
    "Léon",
    "AnNA",
    "Olivia",
    "Lucas",
    "jeanne",
    "Victor",
    "léo",
    "Paul",
    "Ibrahim",
    "Alexandre",
    "Gabrielle",
    "Emma",
    "Adèle",
    "Iris",
    "Aaron",
    "Rose",
    "Sacha",
    "Léa",
    "Andrea",
    "Ismaël",
    "Chloé",
    "Liam",
    "Victoire",
    "Jade",
    "Lina",
    "Victoria",
    "Oscar",
    "Augustin",
    "Côme",
    "Charlie",
    "Lou",
    "Sofia",
    "Joséphine",
    "Diane",
    "Sarah",
    "Ava",
    "Mia",
    "Maël",
    "Auguste",
    "Zoé",
    "Noé",
    "Ella",
    "Jules",
    "Antoine",
    "Nour",
    "Abel",
    "Timothée",
    "Alix",
    "Hugo",
    "Julia",
    "Suzanne",
    "Théo",
    "Marius",
    "Juliette",
    "Marceau",
    "Charles",
    "Maya",
    "Simon",
    "Nina",
    "Charlotte",
    "Eva",
    "Alba",
    "Eliott",
    "Agathe",
    "Romy",
    "Basile",
    "Mariam",
    "Eden",
    "Octave",
    "Zayn",
    "Fatoumata",
    "Léonard",
    "Nathan",
    "Inaya",
    "Georges",
    "Mathis",
    "Ethan",
    "Maxime",
    "Aminata",
    "Camille",
    "Samuel",
    "Ulysse",
    "Rayan",
    "Elena",
    "Aylan",
    "Félix",
    "Inès",
    "Martin",
    "Ambre",
    "Moussa",
    "Henri",
    "Apolline",
    "Axel",
    "Ayden",
    "Romane",
    "Issa",
    "Elio",
    "Valentin",
    "Céleste",
    "Alya",
    "Amir",
    "Giulia",
    "Thelma",
    "David",
    "Héloïse",
    "Constance",
    "Margot",
    "Imran",
    "Gustave",
    "Ali",
    "Léonie",
    "Hector",
    "Achille",
    "Noa",
    "Marin",
    "Thomas",
    "Éléonore",
    "Sophia",
    "Ysée",
    "Fatima",
    "Solal",
    "Elias",
    "Raphaëlle",
    "Noam",
    "Yasmine",
    "Léna",
    "Liv",
    "Clara",
    "Camille",
    "Lucie",
    "Gabin",
    "Lucien",
    "Albane",
    "Naël",
    "Madeleine",
    "Ilyan",
    "Margaux",
    "Luna",
    "Pia",
    "Maryam",
    "Mila",
    "Souleymane",
    "Milo",
    "Jean",
    "Olympe",
    "Haroun",
    "Malo",
    "Idriss",
    "Youssef",
    "Maxence",
    "Émile"
]

nom = input("Entrer ton nom: ")

while not nom.isalpha() :
    nom = input("Entrer ton nom :")


for nom_dans_la_liste in liste_de_nom :
    if(nom.lower() == nom_dans_la_liste.lower()):
        print("deja present")
    else :
        print(nom_dans_la_liste)