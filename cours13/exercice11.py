def transformation(l: list, b:bool) -> list:
    if b :
        l.reverse() # inverse la liste "l"
        liste = sorted(l) # tri la liste "l"
    else :
        liste = sorted(l) # tri la liste "l"
        liste.reverse() # inverse la liste "liste"
    
    return liste

print(transformation([3, 1, 4, 1, 5, 9, 2],False))

