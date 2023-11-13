import numpy as np 

with open('input2', 'r') as f: 
    text=f.readlines()
    f.close()
    
# Spielbuch als array 
# Spielbuch [*,0] = Ergebnisscodierung 1: Ich habe gewonne 2: Gegner hat gewonnen 3: Draw
# [*,1]=Punktzahl aktuelle Runde Gegener 
# [*,2]=Gegnerzug 
# [*,3]= Ich zug 
# [*,4]= Ich Punktezahl aktueller Runde 
# 

Spielbuch=np.zeros((len(text),5),dtype=int)

# Züge werden ins Spielbuch eingetragen 
# Züge codiert 1: Stein 2: Papier 3: Schere 
for index,Zug in enumerate(text): 
    
    match Zug.split()[0]: # Gegner
        case 'A': 
            Spielbuch[index,2]=1
        case 'B': 
            Spielbuch[index,2]=2
        case 'C':
            Spielbuch[index,2]=3
            
    match Zug.split()[1]: # Ich
        case 'Z':         # Need to win            
            if Spielbuch[index,2]<3: 
                Spielbuch[index,3]=Spielbuch[index,2]+1
            if Spielbuch[index,2]==3: 
                Spielbuch[index,3]=1
                
        case 'Y':          # Need to draw
            Spielbuch[index,3]=Spielbuch[index,2]
            
        case 'X':          # Need to loose 
            
            if Spielbuch[index,2]==1:
                Spielbuch[index,3]=3
            if Spielbuch[index,2]>1: 
                Spielbuch[index,3]=Spielbuch[index,2]-1
            
            

# Verteile Punkt nach Zug Wertiggkeit 
Spielbuch[:,1]=Spielbuch[:,2] #  für Gegener
Spielbuch[:,4]=Spielbuch[:,3] #  für mich

# Logisches ich habe gewonnen:
# entweder habe ich eins höher gezogen oder ich habe seine Schere geschlagen
LogikIchgewonnen=np.logical_or (Spielbuch[:,2]+1==Spielbuch[:,3] , Spielbuch[:,2]-2==Spielbuch[:,3])

# Logisches Draw 
LogikDraw=Spielbuch[:,2]==Spielbuch[:,3]

# Logisches Gegner hat gewonnen. 
# Entweder hat der Gegner eins höher gezogen oder seine Stein hat meine Schere zerschlagen
LogikGegnergewonnen=np.logical_or(Spielbuch[:,3]+1==Spielbuch[:,2] , Spielbuch[:,3]-2==Spielbuch[:,2])



# Test der Logik hier werden die Logikvektoren addiert diesen müssen exakt der länge des Spielbuches betragen 

print(sum(LogikGegnergewonnen)+sum(LogikDraw) + sum(LogikIchgewonnen))


## Eintrag ins Spielbuch für die gewinner 

# Codierung des Spiels das ich gewonnen habe  
Spielbuch[LogikIchgewonnen,0]=1
# Rechne mir die Punkte an für einen Sieg
Spielbuch[LogikIchgewonnen,4]+=6 

# Codierung des Spiels dass der Gegner gewonnen hat 
Spielbuch[LogikGegnergewonnen,0]=2
# Rechne dem Gegner die Punkte an
Spielbuch[LogikGegnergewonnen,1]+=6 

# Codierung des Spiels bei Draw
Spielbuch[LogikDraw,0]=3
# Rechner beiden Spieler ein Draw an 
Spielbuch[LogikDraw,1]+=3
Spielbuch[LogikDraw,4]+=3


print(sum(Spielbuch[:,4]))