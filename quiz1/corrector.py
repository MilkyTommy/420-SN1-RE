import argparse
import pandas as pd
import warnings
import glob, os, sys

DEFAULT_SCORE = 15
PATH_OF_SCRIPT = sys.path[0]

warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

def getAnwsersFromAFile(filename, isHeaderRequired = False) -> list[str]:
    df = pd.read_excel(filename,sheet_name=1)
    anwsers = []
    
    for i in range(5,5+max_score) :
        anwsers.append(df.iloc[i, 2])

    if isHeaderRequired :
        return {'firstname' : df.iloc[1,1],
                'lastname' : df.iloc[1,2],
                'id' : df.iloc[1,3],
                'group' : df.iloc[1,4],
                'anwsers' : anwsers
                }

    return {'anwsers' : anwsers}

def getTotalFromAnwsers(input, output) -> int:
    total = 0

    for i in range(0, max_score) :
        # Tranform the Weird behaviour that Sometimes, 'Vrai' and 'Faux' are translate by True and False
        if type(input[i]) is bool :
            if input[i] :
                input[i] = 'Vrai'
            else :
                input[i] = 'Faux'

        total += int(input[i] == output[i])
    return total

def getSingleScore(input_filename, output_filename)-> dict:
    anwsers = getAnwsersFromAFile(input_filename, True)
    correctedAnwsers = getAnwsersFromAFile(output_filename)

    anwsers['total'] = getTotalFromAnwsers(anwsers['anwsers'],correctedAnwsers['anwsers'])
    return anwsers

def writeAnwsersToFile(data, filename) -> str :
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Export the DataFrame to an Excel file
    df.to_excel(filename + '.xlsx', index=False)

    return PATH_OF_SCRIPT + filename + '.xlsx'

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--score", help="Choos max score",type=int)
    parser.add_argument("type", help="Choose between solo or all files",type=str, choices=["single","all"])
    parser.add_argument("-i", "--input", help="select a input file")
    parser.add_argument("-a", "--anwser", help="select a anwser file")
    parser.add_argument("-o", "--output", help="Choose a output file")
    args = parser.parse_args()

    if args.score :
        max_score = args.score
    else :
        max_score = DEFAULT_SCORE

    if args.type == "single" :
        if args.input and args.anwser:
            student = getSingleScore(args.input, args.anwser)
            if args.output :
                finalOutput = {
                    'Nom' : [student['lastname']],
                    'Prenom' : [student['firstname']],
                    'DA' : [student['id']],
                    'Groupe' : [student['group']],
                    'Réponses' : ' ' .join(student['anwsers']),
                    'Score Total' : [student['total']]
                }

                writeAnwsersToFile(finalOutput,str(args.output))
            else : 
                print("Nom :",student['lastname']) 
                print("Prenom :",student['firstname']) 
                print("DA :", student['id'])
                print("Groupe :", student['group'])
                print("réponses :", student['anwsers'])
                print("Score :",student['total'],"/",max_score)
        else :
            parser.error("single requires --input and --anwser.")         
    elif args.type =="all" :
        filename = os.chdir(PATH_OF_SCRIPT + "/solution/")
        correct_anwsers = []

        for filename in glob.glob("*.xlsx"):
            correct_anwsers =getAnwsersFromAFile(filename)
        
        filename = os.chdir(PATH_OF_SCRIPT + "/etudiant/")
        nom = []
        prenom = []
        id = []
        groupe = []
        anwsersOfSingleStudent = []
        totalOfSingleStudent = []

        for filename in glob.glob("*.xlsx"):
            anwsers =getAnwsersFromAFile(filename,True)

            nom.append(anwsers['lastname'])
            prenom.append(anwsers['firstname'])
            id.append(anwsers['id'])
            groupe.append(anwsers['group'])
            anwsersOfSingleStudent.append(' '.join(str(anwsers['anwsers'])))
            totalOfSingleStudent.append(getTotalFromAnwsers(anwsers['anwsers'],correct_anwsers['anwsers']))
            

        finalOutput = {
            'Nom' : nom,
            'Prenom' : prenom,
            'DA' : id,
            'Groupe' : groupe,
            'Réponses' : anwsersOfSingleStudent,
            'Score Total' : totalOfSingleStudent
        }

        if args.output :
            writeAnwsersToFile(finalOutput,'../' + str(args.output))
        else :
            print(finalOutput)