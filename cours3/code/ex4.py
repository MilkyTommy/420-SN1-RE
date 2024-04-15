a = 100
b = 1

print("b avant : ",b)

# print((a > b))
# print((a == 100))
# print((b < 0))

# & = and, | = or
if (a < b) or (a == 100 and b < 0):
    b -= 2

#    ( vrai  ) ou non (vrai    et  vrai) 
#    ( vrai  ) ou (        faux        ) 
if a > b or not (a == 100 and b > 0):
    b += 3


print("b après : ",b)