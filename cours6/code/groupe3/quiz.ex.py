#1 
print(True and True or False and True and not (True or True or not False))
print(True and True or False and True and not True or True or not False)

#2
a = 10
b = 100
c = a*b**a
x = 31

if (a > c) :
    x **= 45 #-> x = x + 45
else :
    if ( c > a) :
        x -= 45 #-> x = x - 45
    else :
        x = 22

print(x)

# 3
fruits = ["banane","orange","pomme"]

for e in fruits :
    for x in range(100) :
        for y in range(100) :
            print(e, x, y)

#4
a = 10
b = 100
c = 32
d = 666

print(a) if a > b else print(b) if a < b else print(c) if a < b else print(d)

#5
while a < b  :
    a += 1
    print("allo")

