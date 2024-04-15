# Votre programme demande à l'utilisateur de faire un choix parmi les énoncés suivants :
#   1. Transformer un nombre Décimal en nombre binaire.
#   2. Transformer un nombre Binaire en nombre Décimal.
# Votre programme demande ensuite d'entrer le nombre à transformer.
# Selon le choix, implémenter le code pour permettre de faire l'opération adéquate.

# INDICES :
#   1. Pour la transformation de Décimal à Binaire, il faut faire un modulo (%) 2 de son nombre 
#      pour avoir le restant de la division. Il faut également faire une division arrondi vers le bas (//) 
#      jusqu'a avoir 0 (utilisation du while).
#   2. Pour la transformation de Binaire à Décimal, il faut multiplier chaque 1 du nombre par 2 exposant 
#      la position du chiffre dans le nombre.


# Mise en page pour afficher tous les choix possibles.
print("1. Transformer un nombre Décimal en nombre binaire")
print("2. Transformer un nombre Binaire en nombre Décimal")
choix = input("Votre choix : ")


# Demande d'entrer un choix tant que le choix est différent de 1 ou 2.
# Puisque le choix n'a pas été converti en entier (avec int("1")), le choix est une chaîne
# de caractères. Il faut donc comparer la variable choix avec des chaînes comme 
# "1" ou "2".
while choix != "1" and  choix != "2" :
    print("Choix éronné, veuillez réessayer.")
    choix = input("Votre choix : ")

nombre_initial = input("Votre nombre à transformer : ")

# Le choix 1 transforme le nombre initial (décimal) en binaire. Il suffit de faire des divisions
# successives par deux tout en prenant le reste de division pour créer le nombre en binaire.
# Il ne faut pas oublier que le nombre est ajouté à gauche du nombre (avant, pas après).
if(choix == "1") :
    nombre_initial_entier = int(nombre_initial)
    nombre_final = ""

    while nombre_initial_entier :
        nombre_final = "1" + nombre_final if(nombre_initial_entier % 2) else "0" + nombre_final
        nombre_initial_entier //= 2

# Puisque que la validation a déjà été fait, si le choix n'est pas 1, c'est que le choix est 2.
# Pour transformer un nombre binaine (nombre_initial) en décimal, il faut multiplier chaque
# nombre par 2 exposant son rang. Son rang sera la longueur du mot. Il faut donc faire 
# len(nombre_initial) pour avoir la longeur du mot, et soustraire 1 puisqu'il faut avoir un rang
# de 0 à X plutôt que 1 à X. Il faut ensuite reduire de 1 l'exposant.
else :
    nombre_final = 0
    exposant = len(nombre_initial) -1
    for i in nombre_initial :
        if i =="1" : nombre_final += 2**exposant
        exposant -= 1

# On affiche le resultat. Pour etre plus clair, il est également pertinant d'afficher le 
# nombre initial -> nombre final.
print(nombre_initial,"->",nombre_final)