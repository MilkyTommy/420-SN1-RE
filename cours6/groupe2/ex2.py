a = []
b = ["banane","pomme"]
c = [
        [
            ["pomme","banane","orange"],
            ["tomate","poivron"]
        ],
        [
            ["honda","jeep","fiat"],
            ["samsung","lg","apple"]
        ]
    ]

# Parcourir une liste dan une liste dans une liste
# for lists in c :
#     for list in lists :
#         for element in list :
#             if(element[0] == "p") :
#                 print(element)

mot_secret = "python"

lettre_entre_au_clavier = input("entre une lettre pour trouver le mot : ")

for lettre in mot_secret :
    if(lettre_entre_au_clavier == lettre) :
        print("La lettre",lettre_entre_au_clavier, "est bien dans le mot")