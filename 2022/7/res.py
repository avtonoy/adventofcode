
with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    
# Transferiere Text Liste in String 
text=text[0]
    
# Wie viel aufeinander folgende Buchstaben dürfen nicht gleich sein. 
Anzahlverschieden=4
Vergleichstring=''


for index,Buchstabe in enumerate(text): 
    Vergleichstring+=Buchstabe # hinzufügen eines weitern Buchstabens 
    # Es werden immer nur eine bestimmt Anzahl von Buchstaben miteinandern vergliehcen  
    LngVergleich=len(Vergleichstring) 
    
    if LngVergleich>Anzahlverschieden: 
        Vergleichstring=Vergleichstring[1:]
        LngVergleich-=1

    # Die ersten Durchläufe werden nicht bewertet da kein Sinn 
    if LngVergleich == Anzahlverschieden: 
        UnGleich=True
        vonHintenmax=LngVergleich
        vonVorneMax=LngVergleich-1 
        for hinten in reversed(range(vonHintenmax)):
            vonVorneMax=hinten
            for vorne in range(vonVorneMax):
                if Vergleichstring[hinten]==Vergleichstring[vorne]:
                    UnGleich=False
                    break
        if UnGleich: 
            print(index+1)
            break