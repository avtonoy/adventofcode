
with open('inputtest', 'r') as f:
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
    
    # der letzt hinzugefügte Buchstaben wird mit allen vorangegangen Buchstaben verglichen. 
    for AnzahluebringeBuchstaben in range(LngVergleich):
        for Vergleichsindex in reversed(range(len(Vergleichstring)-AnzahluebringeBuchstaben-1)): 
            if Vergleichstring[AnzahluebringeBuchstaben]!=Vergleichstring[Vergleichsindex]:
               print('Ungleich') 