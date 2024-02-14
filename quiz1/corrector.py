import argparse
import pandas as pd
import warnings
import glob, os

warnings.filterwarnings('ignore')

SCORE = 15

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="select a input file")
    parser.add_argument("-o", "--output", help="select a output file")
    args = parser.parse_args()

    if args.input and args.output:
        df_in = pd.read_excel(args.input,sheet_name=1)

        firstname = df_in.iloc[1][1]
        lastname = df_in.iloc[1][2]
        id = df_in.iloc[1][3]
        group = df_in.iloc[1][4]

        anwsers = []
        for i in range(5,5+SCORE) :
            anwsers.append(df_in.iloc[i][2])

        df_out = pd.read_excel(args.output,sheet_name=1)
        correct_anwsers = []
        
        for i in range(5,5+SCORE) :
            correct_anwsers.append(df_out.iloc[i][2])
        
        total = 0
        for i in range(SCORE) :
            total += int(correct_anwsers[i] == anwsers[i])

        print("nom :",firstname,lastname, ",id :", id, ",groupe :", group)
        print(total,"/",SCORE)
    else :
        filename = os.chdir("./quiz1/solution/")
        correct_anwsers = []
        print(os.getcwd())

        for filename in glob.glob("*.xlsx"):
            df_solution = pd.read_excel(filename,sheet_name=1)
            for i in range(5,5+SCORE) :
                correct_anwsers.append(df_solution.iloc[i][2])
        
        filename = os.chdir("../quiz1/etudiant/")
        # for filename in glob.glob("*.xlsx"):
        #     df_student = pd.read_excel(filename,sheet_name=1)
        #     print(df_student)
        #     firstname = df_student.iloc[1][1]
        #     lastname = df_student.iloc[1][2]
        #     id = df_student.iloc[1][3]
        #     group = df_student.iloc[1][4]

        #     anwsers = []
        #     for i in range(5,5+SCORE) :
        #         anwsers.append(df_student.iloc[i][2])

        # total = 0
        # for i in range(SCORE) :
        #     total += int(correct_anwsers[i] == anwsers[i])
        
        # print("nom :",firstname,lastname, ",id :", id, ",groupe :", group)
        # print(total,"/",SCORE)

            