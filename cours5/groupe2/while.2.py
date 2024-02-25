# age = 18
# while age <= 65 :
#     print("Tu as actuellement :",age, "an(s)")

#     if(age == 65) :
#         print("Bonne retraite !")

#     age = age + 1

validation_entrer = False

while not validation_entrer :
    choice = input("Choisi entre 1 et 2 : ")

    if(choice == "1" or choice == "2") :
       validation_entrer = True 

print(choice)