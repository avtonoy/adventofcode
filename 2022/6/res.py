
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
Zaehlerungleich=0

for index,Buchstabe in enumerate(text): 
    Vergleichstring+=Buchstabe # hinzufügen eines weitern Buchstabens 
    # Es werden immer nur eine bestimmt Anzahl von Buchstaben miteinandern vergliehcen  
    Gleich = False
    if len(Vergleichstring)>Anzahlverschieden: 
        Vergleichstring=Vergleichstring[1:]
    
    # der letzt hinzugefügte Buchstaben wird mit allen vorangegangen Buchstaben verglichen. 
    for Vergleichsindex in range(len(Vergleichstring)-1): 
        Vergleichsbuchstabe=Vergleichstring[Vergleichsindex]
        if Vergleichsbuchstabe==Buchstabe:
            Gleich=True 
            break
    
    if Gleich != True: 
        Zaehlerungleich+=1
        if Zaehlerungleich ==4:
            print(index)
    else: 
        Zaehlerungleich-=1