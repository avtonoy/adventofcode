import numpy as np 

with open('input', 'r') as f: 
    text=f.readlines()
    f.close()
    

# Rucksack[*,0]: erstes Kompartment
# Rucksack[*,1]: zweiter Kompartment 
# Rucksack[*,2]: Items ins beiden Komparments 
# Rucksack init 
Rucksaecke=np.empty([len(text),3],dtype=str)
    
s2 = text[0][len(text[0]) // 2 : ]
s1 = text[0][:len(text[0]) // 2]

for Index,Eintrag in enumerate(text): 
    Rucksaecke[Index,0]=Eintrag[len(Eintrag) // 2 : ]


