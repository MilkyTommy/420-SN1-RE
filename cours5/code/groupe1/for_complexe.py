a = 1 # nombre entier
b = 1.0 # nombre decimal
c = True # variable booléen
d = "abc" # chaîne de charactères (string)
e = [] # Tableau (List) vide
f = [0,1] # Tableau (List) avec 0 et 1
fruits = ["pomme","banane","orange"] # Tableau (List) avec des fruits

# affiche tous les fruits dans la liste de fruits
for fruit in fruits :
    print(fruit)

cars = ["volvo", 
        "Mercedes", 
        "Cadilac", 
        "BMW", 
        "Fiat",
        "Honda",
        "Jeep"]

for car in cars :
    if(car == "Jeep") :
        print("You are ... a ",car, " owner !")
    else :
        print("nice ", car)

    if(not car == "Ferrari") :
        print("Too bad")