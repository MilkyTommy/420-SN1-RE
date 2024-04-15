import fonctions_toute_faite


def recherche_produit_par_nom(liste, nom):

    for element in liste :
        if nom == element["nom"] :
            return element

    return {}

panier = fonctions_toute_faite.get_data()

nom_produit = input("Entrer un nom de produit :").title()

produit_trouvé = recherche_produit_par_nom(panier, nom_produit)

print(produit_trouvé)

