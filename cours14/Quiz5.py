def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def sum_of_factorials(numbers):
    total = 0
    for num in numbers:
        total += factorial(num)
    return total

print(sum_of_factorials([1, 2, 3]))



def message_positif():
    return "Content d'apprendre que vous avez aimé !"

def message_negatif(str):
    return message_positif()


def cours_de_prog(reponse : str):
    print("Avez-vous aimé le cours ?") 

    if reponse.lower() == "oui":
        print(message_negatif(message_positif()))


cours_de_prog("oui")

ark = [{'nom': 'Tommy', 'genre': 'M', 'surnom': [{'nom': 'Tom'}, {'nom': 'Toto'}]}, {'nom': 'Robert', 'genre': 'O', 'surnom': [{'nom': 'Robby'}, {'nom': 'Bob'}]}, {'nom': 'Béatrice', 'genre': 'F', 'surnom': [{'nom': 'Béa'}, {'nom': 'Bé'}]}]

for personne in ark :
    for surnom in personne['surnom']:
        print(surnom['nom'])

def fontion_a_deux_parametres(un,deux):
    return [un,deux]

fontion_a_deux_parametres(1,2)


def true():
    return not True or True and True or True and not not True
def false():
    return "False"

print(true() and True or not false() == "True" or bool("True") and bool("False"))