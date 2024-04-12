import fonctions_toute_faite as ftf

def recherche_produit_par_nom(liste, nom):

    for element in liste :
        if nom == element["nom"] :
            return element

    return {}

def comparer_produits(liste,nom1,nom2):

    element1 = recherche_produit_par_nom(liste,nom1)
    element2 = recherche_produit_par_nom(liste,nom2)

    if element1["prix"] < element2["prix"]:
        return element1
    else:
        return element2


panier = ftf.get_data()

comparer_produits(panier,"Lait","Oeufs")