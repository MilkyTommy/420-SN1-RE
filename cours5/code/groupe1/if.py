# Demander a l'utilisateur d'entrer deux nombres.
# Si le nombre A est plus grand que le nombre B, 
#   afficher le nombre A
# Si le nombre B est plus grand que le nombre A,
#   afficher le nombre B
# Si le nombre A est égal au nombre B, 
#   Afficher A+B

# Important : Utiliser les elif
a = int(input("Entre un premier nombre : "))
b = int(input("Entre un second nombre : "))

if(a > b) :
  print(a)
elif(b > a) :
  print(b)
else : 
  print(a+b) #10 + 10 = 20 // "10" + "10" = "1010"
