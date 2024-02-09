age = int(input("Enter age: "))

height = int(input("Enter height: "))

first_name = input("Enter first name: ")

is_member = input("Are you a member ? (Yes/no): ")

is_man = input("What is your gender ? (Man/Woman/Other): ")

category = "A"

if is_member == "Yes":
    is_member = True
else:
    is_member = False

if is_man == "Man":
    is_man = True
else:
    is_man = False

if age > 65 and height > 140 and is_member and is_man:
    category = "Boomer"
else:
    if age >65  and is_member and not is_man:
        category = "Karen"
    else:
        category = "B"

print(category)