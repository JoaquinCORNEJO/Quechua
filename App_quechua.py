import pandas as pd 
from random import randint

# Import
file = pd.read_csv('./raw_quechua.csv', 
                    delimiter=';', 
                    header=0, 
                    names=['quechua','espanol'])   
# Convert data type
data = pd.DataFrame(data=file)

# Set numbers of entries
nb_rows = int(data.size/2) # 2 columns

# Initialize
print('Bienvenido! Practiquemos quechua!\n')

for i in range(5): 
    
    # Create random number
    row = randint(0, nb_rows-1)
    
    # Interface
    answer = input('Que significa ' + '"' + data.quechua[row] + '":')

    if answer == data.espanol[row]: 
        print('Muy bien!')
    else: 
        print('La respuesta es ' + data.espanol[row])

    print('\n')