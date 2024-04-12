def calcul_prix_total(liste):
    total = 0
    for element in liste :
        if element["taxes"]:
            total += element["prix"] * 1.15
        else :
            total += element["prix"]

    return total   

panier = [
  {
    "nom_produit": "Pain",
    "code_barre": "1234567890",
    "prix": 1.99,
    "taxes": False
  },
  {
    "nom_produit": "Lait",
    "code_barre": "0987654321",
    "prix": 2.49,
    "taxes": True
  },
  {
    "nom_produit": "Pommes",
    "code_barre": "5678901234",
    "prix": 3.99,
    "taxes": True
  },
  {
    "nom_produit": "Beurre",
    "code_barre": "2468013579",
    "prix": 2.29,
    "taxes": False
  },
  {
    "nom_produit": "Oeufs",
    "code_barre": "1357924680",
    "prix": 4.49,
    "taxes": True
  },
  {
    "nom_produit": "Fromage",
    "code_barre": "3141592653",
    "prix": 5.99,
    "taxes": True
  },
  {
    "nom_produit": "Jus d'orange",
    "code_barre": "9876543210",
    "prix": 2.79,
    "taxes": False
  },
  {
    "nom_produit": "Yaourt",
    "code_barre": "0123456789",
    "prix": 1.69,
    "taxes": True
  },
  {
    "nom_produit": "Céréales",
    "code_barre": "8765432109",
    "prix": 3.29,
    "taxes": False
  },
  {
    "nom_produit": "Eau en bouteille",
    "code_barre": "5432109876",
    "prix": 0.99,
    "taxes": False
  },
  {
    "nom_produit": "Chips",
    "code_barre": "9876543210",
    "prix": 1.79,
    "taxes": True
  },
  {
    "nom_produit": "Soda",
    "code_barre": "0123456789",
    "prix": 1.29,
    "taxes": True
  },
  {
    "nom_produit": "Poulet",
    "code_barre": "8765432109",
    "prix": 6.99,
    "taxes": False
  },
  {
    "nom_produit": "Riz",
    "code_barre": "5432109876",
    "prix": 2.89,
    "taxes": True
  },
  {
    "nom_produit": "Pâtes",
    "code_barre": "1234567890",
    "prix": 1.49,
    "taxes": False
  },
  {
    "nom_produit": "Sauce tomate",
    "code_barre": "0987654321",
    "prix": 2.19,
    "taxes": True
  },
  {
    "nom_produit": "Café",
    "code_barre": "5678901234",
    "prix": 4.99,
    "taxes": True
  },
  {
    "nom_produit": "Thé",
    "code_barre": "2468013579",
    "prix": 3.49,
    "taxes": False
  },
  {
    "nom_produit": "Miel",
    "code_barre": "1357924680",
    "prix": 5.79,
    "taxes": True
  },
  {
    "nom_produit": "Confiture",
    "code_barre": "3141592653",
    "prix": 2.99,
    "taxes": True
  },
  {
    "nom_produit": "Pain de mie",
    "code_barre": "9876543210",
    "prix": 1.99,
    "taxes": False
  },
  {
    "nom_produit": "Saucisson",
    "code_barre": "0123456789",
    "prix": 3.79,
    "taxes": True
  },
  {
    "nom_produit": "Chocolat",
    "code_barre": "8765432109",
    "prix": 2.49,
    "taxes": False
  },
  {
    "nom_produit": "Bonbons",
    "code_barre": "5432109876",
    "prix": 0.99,
    "taxes": True
  },
  {
    "nom_produit": "Biscuits",
    "code_barre": "1234567890",
    "prix": 2.29,
    "taxes": True
  },
  {
    "nom_produit": "Pain aux raisins",
    "code_barre": "0987654321",
    "prix": 1.79,
    "taxes": False
  },
  {
    "nom_produit": "Salade",
    "code_barre": "5678901234",
    "prix": 3.49,
    "taxes": True
  },
  {
    "nom_produit": "Tomates",
    "code_barre": "2468013579",
    "prix": 1.99,
    "taxes": False
  },
  {
    "nom_produit": "Poivrons",
    "code_barre": "1357924680",
    "prix": 2.49,
    "taxes": True
  },
  {
    "nom_produit": "Carottes",
    "code_barre": "3141592653",
    "prix": 1.29,
    "taxes": False
  }
]

chiens = [
  {
    "nom_race": "Labrador Retriever",
    "code_barre": "1234567891",
    "prix": 500,
    "taxes": True
  },
  {
    "nom_race": "Bulldog anglais",
    "code_barre": "1234567892",
    "prix": 700,
    "taxes": True
  },
  {
    "nom_race": "Berger allemand",
    "code_barre": "1234567893",
    "prix": 600,
    "taxes": True
  },
  {
    "nom_race": "Golden Retriever",
    "code_barre": "1234567894",
    "prix": 550,
    "taxes": True
  },
  {
    "nom_race": "Beagle",
    "code_barre": "1234567895",
    "prix": 450,
    "taxes": True
  },
  {
    "nom_race": "Boxer",
    "code_barre": "1234567896",
    "prix": 650,
    "taxes": True
  },
  {
    "nom_race": "Caniche",
    "code_barre": "1234567897",
    "prix": 600,
    "taxes": True
  },
  {
    "nom_race": "Chihuahua",
    "code_barre": "1234567898",
    "prix": 400,
    "taxes": True
  },
  {
    "nom_race": "Dogue allemand",
    "code_barre": "1234567899",
    "prix": 800,
    "taxes": True
  },
  {
    "nom_race": "Dalmatien",
    "code_barre": "1234567800",
    "prix": 550,
    "taxes": True
  }
]

total = calcul_prix_total(panier)

print("Le prix total de votre panier est de:", total, "dollars.")