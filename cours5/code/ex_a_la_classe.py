# parcourir 100 elements.
# Si multiple de 3 : 
#     afficher le mot "pomme"
# Si multiple de 5 : 
#     afficher le mot "banane"
# Si multiple de 3 et 5 :
#     afficher le mot "orange"

for n in range(1,100+1):

    if not(n%3 or n%5):
        print("orange")
    elif not n%3 :
        print("pomme")
    elif not n%5:
        print("banane")