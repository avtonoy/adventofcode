import numpy as np




with open('input2', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip()
    
# tex2="""2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""

# text=tex2.split()


PaarMatrix=np.zeros((len(text),4),dtype=int)


for index,line in enumerate(text): 

    Paarsplit=line.split(',')
    ObenUnten=[]

    for Paar in Paarsplit: 
        ObenUnten.append(Paar.split('-'))
    PaarMatrix[index,0]=int(ObenUnten[0][0]) # Erste Gruppe untere Grenze 
    PaarMatrix[index,1]=int(ObenUnten[0][1]) # Erste Gruppe obere Grenze 
    PaarMatrix[index,2]=int(ObenUnten[1][0]) # Zweite Gruppe untere Grenze  
    PaarMatrix[index,3]=int(ObenUnten[1][1]) # Zweiter Gruppe obere Grenze 
    
    
# Prüfe Einschluss der zweiten Gruppe von der ersten Gruppe
LogischerEinschlussGruppe1=np.logical_and( PaarMatrix[:,1]>=PaarMatrix[:,2],PaarMatrix[:,1]<=PaarMatrix[:,3])
# Prüfe Einschluss der ersten Gruppe seitens der zweitens Gruppe 
LogischerEinschlussGruppe2=np.logical_and( PaarMatrix[:,3]>=PaarMatrix[:,0],  PaarMatrix[:,3] <= PaarMatrix[:,1])
# Doppelte Einschlüsse vermeiden
LogischerEinschluss=np.logical_or( LogischerEinschlussGruppe1, LogischerEinschlussGruppe2)

print(sum(LogischerEinschluss))