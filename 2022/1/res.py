import pandas as pd 
import numpy as np 

with open('input','r') as f:
    text=f.readlines()
    f.close()

ListeOfCalorine=np.array(text)

NichtLeereEintraege=ListeOfCalorine != '\n'
AnzahlderElfen=sum(np.invert(NichtLeereEintraege))+1
ElfenCalorine=np.zeros(AnzahlderElfen,dtype=int)

Zwischensumme=0
Elfenzaehler=0

for index,Eintrag in enumerate(NichtLeereEintraege): 
    if Eintrag: 
        Zwischensumme=Zwischensumme+int(ListeOfCalorine[index])
    else:
        ElfenCalorine[Elfenzaehler]=Zwischensumme
        Elfenzaehler += 1
        Zwischensumme=0
        
ElfenCalorine[Elfenzaehler]=Zwischensumme

print(ElfenCalorine.max())

ElfenCalorine[::-1].sort()

print(sum(ElfenCalorine[0:3]))