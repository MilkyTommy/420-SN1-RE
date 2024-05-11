import fonctions_utilitaire as util

nom_produit = input("entre un nom de produit : ")

produits = util.rechercher_produit_pas_nom(util.liste,nom_produit.title())

print(produits)