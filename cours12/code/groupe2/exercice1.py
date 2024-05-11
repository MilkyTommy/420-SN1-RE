def recherche_produit_par_nom(liste, nom):

    for element in liste :
        if nom.lower() == element["nom"].lower() :
            return element

    return {"nom": "", "prix": 0, "quantite_stock": 0}

def comparer_produits(liste,nom1,nom2):

    element1 = recherche_produit_par_nom(liste,nom1)
    element2 = recherche_produit_par_nom(liste,nom2)

    if element1["prix"] < element2["prix"]:
        return element1
    else:
        return element2

panier = [
            {"nom": "Lait", "prix": 2.5, "quantite_stock": 100},
            {"nom": "Pain", "prix": 1.0, "quantite_stock": 150},
            {"nom": "Oeufs", "prix": 3.0, "quantite_stock": 80},
            {"nom": "Fromage", "prix": 4.0, "quantite_stock": 120},
            {"nom": "Jus d'orange", "prix": 2.0, "quantite_stock": 90},
            {"nom": "Pâtes", "prix": 1.5, "quantite_stock": 200},
            {"nom": "Riz", "prix": 2.0, "quantite_stock": 180},
            {"nom": "Tomates", "prix": 1.8, "quantite_stock": 120},
            {"nom": "Pommes de terre", "prix": 1.2, "quantite_stock": 150},
            {"nom": "Poulet", "prix": 5.0, "quantite_stock": 100},
            {"nom": "Boeuf", "prix": 8.0, "quantite_stock": 80},
            {"nom": "Saumon", "prix": 7.0, "quantite_stock": 90},
            {"nom": "Bananes", "prix": 2.0, "quantite_stock": 100},
            {"nom": "Carottes", "prix": 1.2, "quantite_stock": 120},
            {"nom": "Pommes", "prix": 1.5, "quantite_stock": 130},
            {"nom": "Poires", "prix": 1.8, "quantite_stock": 110},
            {"nom": "Yaourts", "prix": 1.0, "quantite_stock": 200},
            {"nom": "Céréales", "prix": 3.0, "quantite_stock": 150},
            {"nom": "Biscuits", "prix": 2.5, "quantite_stock": 180},
            {"nom": "Chocolat", "prix": 3.5, "quantite_stock": 160},
            {"nom": "Café", "prix": 4.0, "quantite_stock": 140},
            {"nom": "Thé", "prix": 3.0, "quantite_stock": 170},
            {"nom": "Légumes surgelés", "prix": 2.8, "quantite_stock": 110},
            {"nom": "Pizzas", "prix": 6.0, "quantite_stock": 90},
            {"nom": "Glaces", "prix": 3.0, "quantite_stock": 120},
            {"nom": "Chips", "prix": 2.0, "quantite_stock": 200},
            {"nom": "Soda", "prix": 1.5, "quantite_stock": 180},
            {"nom": "Eau minérale", "prix": 1.0, "quantite_stock": 220}
        ]

produit_final = comparer_produits(panier,input("entrer un nom :"),input("entrer un deuxieme nom :"))

print(produit_final)