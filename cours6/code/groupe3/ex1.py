mot_secret = "cul"
vies = 6

while vies > 0 and len(mot_secret) != 0:
    print("nombre de vies : ",vies)
    print("longueur du mot restant  : ",len(mot_secret))
    lettre_trouve = False
    lettre_ecrit_au_clavier = input("Entre une lettre : ")

    for lettre in mot_secret :
        if (lettre == lettre_ecrit_au_clavier) :
            lettre_trouve = True
            mot_secret = mot_secret.replace(lettre_ecrit_au_clavier,"")

    if not lettre_trouve :
        vies -= 1

if vies == 0 :
    print("Dead")
else : 
    print("Win")