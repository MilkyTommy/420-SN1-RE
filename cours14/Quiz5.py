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