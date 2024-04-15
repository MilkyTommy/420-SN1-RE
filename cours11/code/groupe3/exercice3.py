import data 

panier = data.get_data()

nom_produit = input("entre un nom de produit : ")

produit = data.rechercher_produit_pas_nom(panier,nom_produit.title())

print(produit["nom"])