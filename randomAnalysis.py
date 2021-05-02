import pandas
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

random = pandas.read_csv('random2.csv')
output = {}

def split(word):
    return [char for char in word] 

for i in range(len(random)):
    tempString = random['random'][i].upper()
    randomCharacters = split(tempString)
    for char in randomCharacters:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1

plt.bar(*zip(*output.items()))
plt.show()


