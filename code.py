# --------------
#  Read the data of the format .yaml type
import json
import yaml

# using with open command to read the file
with open(path) as f:
    data = yaml.load(f)

#  Women who got the first Nobel Prize?
#print(data)
res = [ sub['Full Name'] for sub in data if sub['Sex']=='Female'] 
nb = res[0]

print('The women who got the first Nobel Prize is', nb)

#  How many have come from india?
ic = []
#  Calculate category wise number of prizes for the people who came from India?
#   Which country has produced the highest number of Nobel winners for category `Chemistry`?
from collections import Counter
import operator



#  Which Organization won the most nobel prizes in the category "Physics" and "Chemistry" ?

#  What was the Motivation for awarding the Nobel Prize for Marie Curie, nÃ©e Sklodowska?
moti =[sub['Motivation'] for sub in data if sub['Full Name']=='Marie Curie, nÃ©e Sklodowska']
print('The motivation for awarding the Nobel prize to Marie is', moti)
#  In which category people got Noble Prize in the year 1994?


