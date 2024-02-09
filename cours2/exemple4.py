Height = float(input("Enter your height: "))
size = float(input("Enter your size: "))



if Height > 6.0:
    if size < 100:
        print("You're skinny and tall")
    else:
        print("You're fat and tall")
else:
    if size < 100:
        print("You're skinny and short")
    else:
        print("You're fat and short")