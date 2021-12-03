import pandas as pd 
import random
import numpy as np

# Import csv file
file_verbs = pd.read_csv('./raw_verbos.csv', 
                    delimiter= ';', 
                    header= 0, 
                    names= ['quechua','espanol'])   
file_nouns = pd.read_csv('./raw_sustantivos.csv', 
                    delimiter= ';', 
                    header= 0, 
                    names= ['quechua','espanol'])   
file_phrases = pd.read_csv('./raw_frases.csv', 
                    delimiter= ';', 
                    header= 0, 
                    names= ['quechua','espanol'])   

# Open application
print('Bienvenido!\nPractiquemos quechua!\n')

# Select mode 
print('Selecciona el modo:')
print('1) Quechua a español\n2) Español a quechua\n')
mode = input()
mode = int(mode)

print('Que grupo de palabras quieres practicar ?')
print('1) Verbos\n2) Sustantivos\n3) Frases')
groupe = input()
groupe = int(groupe)

# Convert file's type and select groupe of words
groupe_exist = 1
if groupe == 1: 
    data = pd.DataFrame(data= file_verbs)
elif groupe == 2: 
    data = pd.DataFrame(data= file_nouns)
elif groupe == 3:
    data = pd.DataFrame(data= file_phrases)
else: 
    groupe_exist = 0

# Set numbers of entries
nb_data_rows = int(data.size/2) # 2 columns

to_be_continued = 1
while to_be_continued == 1 and groupe_exist == 1:

    # Get number of trials
    nb_trials = input('\nCuantas palabras quieres practicar ?\n')
    if nb_trials == '': 
        print('Nos vemos pronto !')
        break
    else:
        nb_trials = int(nb_trials)

    # Instructions
    print('\nIntrucciones : \nSelecciona la alternativa correcta.\n')

    if mode == 1 or mode == 2: 
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
                    print(str(counter) + ') ' + data.espanol[alternative])
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

        if mode == 2: 

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
        
        # Ask if user wants to continue
        print('Desea continuar el ejercicio ?')
        print('\n1) Si\n2) No')
        to_be_continued = input()
        
        if user_answer == '': 
            print('Nos vemos pronto !')
            break
        else:
            to_be_continued = int(to_be_continued)

    else: 
        print('Respuesta no reconocida')
        break

    