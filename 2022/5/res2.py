
with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    
# tex2="""    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

# text=tex2.split()


# header wird gelesen und aus der Anweisungsfolge entfernt 
header=[]
header.append( text.pop(0))

# header ist mit einer Leerzeile von der Anweisungsfolge getrennt 
while header[-1] != '':
    header.append( text.pop(0))
    
header.pop() # Leerzeile wird gelöscht 

# Vektor für Aufbaumatrix 
Vektoraufbaustr=header.pop().split()
Aufbau={}

# Erzeuge Aufbau Bibliothek nur mit Keys ohne inhalt 
for index in range(len(Vektoraufbaustr)): 
    Aufbau.update({int(Vektoraufbaustr[index]):[]}) 

# Befüllung der Aufbau Bibliothek 
for line in reversed(header):
    
    # Schreibe ein |X| rein um Lückenzweifelsfrei zu markieren
    Reihe=line.replace('    ',' |X| ').split()

    for index,Reiheneintrag in enumerate(Reihe): 
        if Reiheneintrag != '|X|':
            Aufbau[index+1].append(Reiheneintrag)



for Anweisungstext in text: 
        Anweisung=Anweisungstext.split()
        Anzahl=int(Anweisung[1])
        Von=int(Anweisung[3])
        Nach=int(Anweisung[5])
        
        Zwischenaufbau=[]
        for aktion in range(Anzahl): 
            Zwischenaufbau.append(Aufbau[Von].pop())
            
        for aktion in range(Anzahl): 
            Aufbau[Nach].append(Zwischenaufbau.pop())


stringout=''
keys=list(Aufbau.keys())

# Ermittle die oben liegenden Elemente
for key in keys: 
    stringout+=Aufbau[key][-1]

# Entferne die Klammern um die Bustaben 
stringout=stringout.replace('[', '')
stringout=stringout.replace(']', '')


print(Aufbau)
print(stringout)