file = open("diabetic_data_initial.csv",'r')

header = file.readline().split(",")
data = []

for line in file:
    line.split(',')
    data.append(line.split(','))
    
    

#bardzo nieprofesjonalna wersja, ale działa    
import pandas as pd
import os

headers = []
dane = []
if os.path.isfile('diabetic_data_initial.csv'):
    with open('diabetic_data_initial.csv', "r") as zawartosc:
        count = 0

        for linia in zawartosc:
            if (count == 0):
                headers = linia.split(",")
                count += 1
            else:
                linia = linia.replace("\"", "")
                dane.append(tuple(linia.split(",")))

data = pd.DataFrame(dane)
print(data)
