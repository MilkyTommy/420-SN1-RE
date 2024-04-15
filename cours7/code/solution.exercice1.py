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


# Liste de nom, dans un tableau. Ex. liste_de_nom[0] retourne "GABRIEL"
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

nom = input("entre un nom : ")

# Demande d'entrer un nom tant que le nom contient autre chose des lettres de l'alphabet
# tant que (non nom.isalpha) -> tant que pas dans l'alphabet
while not nom.isalpha() :
    nom = input("Oups, entre un nom : ")


# Cette variable assume que le nom n'est pas dans la liste. 
# Si le nom est dans la liste,cette variable devriendra vrai, 
#   et le programme affichera 'déjà présent' à la fin.  
# Sinon, le programme affichera le nom initiallement écrit à la fin.
is_deja_present = False


# Cette boucle parcourera chaque nom dans la liste_de_nom et mettrera le contenu dans la 
# variable nom_de_la_liste.
# Attention, la variable dans après le mot for doit etre différente, sinon elle effacera 
# ce qu'il y avait précédemment. Ex. ecrire  'nom' plutôt que 'nom_de_la_liste' aurait
# effacé le nom que vous aviez précédemment écrit à la ligne 187/192
for nom_de_la_liste in liste_de_nom :

    # il faut mettre le nom que vous avez écrit tout en minuscule, et le comparer
    # au nom_de_la_liste, lui aussi tout en minuscule.
    # Ex. "gabriel" == "GABRIEL" -> FAUX 
    # mais "gabriel" == "gabriel" -> VRAI
    if(nom.lower() == nom_de_la_liste.lower()) :

        # is_deja_present devient vrai. Le nom à été trouvé dans la liste.
        # Si, après avoir parcouru tous la liste, la variable n'a toujours pas été modifié,
        # cela veut dire que le nom entré n'est pas dans la liste.
        is_deja_present = True


# Imprime 'Déjà présent' si le nom est dans la liste (si is_deja_present == VRAI).
# Sinon, il imprimera le nom qui à initiallement été écrit, tel que demandé dans l'énoncé.
if is_deja_present :
    print("Déjà présent")
else :
    print(nom)