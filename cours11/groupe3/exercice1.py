import data

def comparer_produits(liste_produits, nom_produit_1, nom_produit_2):

    produit_1 = data.rechercher_produit_pas_nom(liste_produits, nom_produit_1)
    produit_2 = data.rechercher_produit_pas_nom(liste_produits, nom_produit_2)

    if produit_1["prix"] < produit_2["prix"] :
        return produit_1
    
    return produit_2

panier = data.get_data()

nom_produit_1 = input("Entrer un nom de produit (1) :")
nom_produit_2 = input("Entrer un nom de produit (2) :")

produit = comparer_produits(panier, nom_produit_1.title(), nom_produit_2.title())

print(produit)