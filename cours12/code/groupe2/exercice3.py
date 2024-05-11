def ajouter_nom(liste : list,nom : str) -> list:
    liste.append({"nom": nom.lower()})
    return liste


panier = [{"nom":"tommy"},{"nom":"bob"}]

panier.append({"nom":"John"})

print(ajouter_nom(panier,"Maxime"))
