# |------------|
# | 0 | 1  | 2 |
# |------------|
# | 3 | 4  | 5 |
# |------------|
# | 6 | 7  | 8 |
# |------------|

def dessiner(tableau):
    print('|------------|')
    print('| ' + tableau[0]+ ' | ' + tableau[1]+ '  | ' + tableau[2]+ ' |')
    print('|------------|')
    print('| ' + tableau[3]+ ' | ' + tableau[4]+ '  | ' + tableau[5]+ ' |')
    print('|------------|')
    print('| ' + tableau[6]+ ' | ' + tableau[7]+ '  | ' + tableau[8]+ ' |')

    print('|------------|')

tableau = ["","","",
           "","","",
           "","",""]

dessiner(tableau)

