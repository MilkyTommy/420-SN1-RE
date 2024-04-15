Height = float(input("Enter your height: "))
age = float(input("Enter your size: "))



if Height > 6.0:
    if age < 18:
        print("You're a minor & tall")
    else:
        print("You're a minor and tall")
else:
    if age < 100:
        print("You're major and short")
    else:
        print("You're major and short")