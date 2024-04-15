def afficher_dessin() :
    dessin = r"""
                        |\
                /| \
                / |  \
                .'. |   \  
                '.|_(()))))
                ((((/.(
                ,))) _/
                ((((_(              
                )/  \\             
                    \__/-)                     /\__
                    \_\(\                   .'\ \ '.
                    )\ \\\            ___..' o \ \.'
                    /  \ \\\           ''---.    \_\
                /    '.\\\    . ' ,       '--.'\_
                /.    .| \-'---- O -           \/O'.
                (_/    \ \| )   ' . '           |O O \___
                /.'.__.'._.'                    | O|_O O/
                /.'.   .'. |                     |O |O O/)
            / O '._.' '.|                     |_O|_O'/
            /         O  |                      ||/  /
            /'._________.'|                      \ )_/ 
            /''.-.-.-.-.-.-|                       '. \
            '.____________.'                        \ _\
                    |/ /mrf                        __'\\
                __(,\_\_ _______  ____   __  ____(_'--_)__
                """
    print(dessin)

def calculer_aire_rectancle(x,y) :
    print(x*y)

def aire_rectangle(x,y) :
    aire = x * y
    return aire

def aire_rectangle_ou_carre(x, y = False) :
    if(not y):
        y = x

    aire = x * y
    return aire

# afficher_dessin()

# calculer_aire_rectancle(2,2)
# calculer_aire_rectancle(5,2)
# calculer_aire_rectancle(10,50)

x = aire_rectangle(4,4)
print(aire_rectangle(5,5))



y = aire_rectangle_ou_carre(2)
print(aire_rectangle_ou_carre(2))

