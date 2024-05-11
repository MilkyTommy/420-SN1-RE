from random import choice, randint, shuffle

def generate_password(len = 8):

    if len < 4 : 
        print("Le mot de passe sera de 8 caractères")
        len = 8

    password = []
    sp = "!@#$%^&*()_+-><"
    char = "qwertyuiopasdfghjklzxcvbnm"

    has_char_lower = False
    has_char_upper = False
    has_digit = False
    has_sp = False

    for e in range(len):
        letter = ""

        if e >= len -4 :
            if not has_sp:
                letter = choice(sp)
                has_sp = True
            elif not has_digit:
                letter = str(randint(0,9))
                has_digit = True
            elif not has_char_lower:
                letter = choice(char)
                has_char_lower = True
            elif not has_char_upper:
                letter = choice(char).upper()
                has_char_upper = True
        
        if letter == "":
            randomNumber = randint(0,3)

            if randomNumber == 0 :
                letter = choice(sp)
                has_sp = True
            elif randomNumber == 1:
                letter = str(randint(0,9))
                has_digit = True
            elif randomNumber == 2:
                letter = choice(char)
                has_char_lower = True
            else:
                letter = choice(char).upper()
                has_char_upper = True

        password.append(letter)

    shuffle(password)

    return "".join(password)

choix = int(input("longueur du mot de passe : "))
print(generate_password(choix))