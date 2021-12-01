import pandas as pd 
import random
import numpy as np

# Import csv file
file = pd.read_csv('./raw_quechua.csv', 
                    delimiter=';', 
                    header=0, 
                    names=['quechua','espanol'])   

# Convert file's type
data = pd.DataFrame(data= file)

# Set numbers of entries
nb_data_rows = int(data.size/2) # 2 columns

# Open application
print('Bienvenido!\n Practiquemos quechua!\n')

# Select mode 
print('Selecciona el modo: \n')
print('1) Quechua a español\n2) Español a quechua\n')
mode = input()
mode = int(mode)

# Get number of trials
nb_trials = input('\nCuantas palabras quieres practicar ?\n')
nb_trials = int(nb_trials)

# Instructions
print('\nIntrucciones : \nSelecciona la alternativa correcta.\n')

if mode == 1: 

    for trial in range(nb_trials): 
        
        # Create 3 random numbers
        alternatives = random.sample(range(nb_data_rows-1), 3)

        # Select right answers
        right_answer = random.choice(alternatives)

        # Get indice of right answer
        ind_right_answer = alternatives.index(right_answer) + 1
        
        # Interface
        print('Que significa ' + '"' + data.quechua[right_answer] + '" en español :')

        # Print answers
        counter = 1 
        for alternative in alternatives: 
            print(str(counter) + ') ' + data.espanol[alternative], '\n')
            counter += 1

        # Get user answer
        user_answer = input()
        if user_answer == '': 
            print('Nos vemos pronto !')
            break
        else :
            user_answer = int(user_answer)

        if user_answer == ind_right_answer:
            print('Muy bien !\n')

        else :
            print('La respuesta correcta es : ' + data.espanol[right_answer] + '\n')

elif mode == 2: 

    for trial in range(nb_trials): 
        
        # Create 3 random numbers
        alternatives = random.sample(range(nb_data_rows-1), 3)

        # Select right answers
        right_answer = random.choice(alternatives)

        # Get indice of right answer
        ind_right_answer = alternatives.index(right_answer) + 1
        
        # Interface
        print('Que significa ' + '"' + data.espanol[right_answer] + '" en quechua :')

        # Print answers
        counter = 1 
        for alternative in alternatives: 
            print(str(counter) + ') ' + data.quechua[alternative], '\n')
            counter += 1

        # Get user answer
        user_answer = input()
        user_answer = int(user_answer)

        if user_answer == ind_right_answer:
            print('Muy bien!\n')

        else :
            print('La respuesta correcta es : ' + data.quechua[right_answer] + '\n')

else: 
    print('Respuesta no reconocida')