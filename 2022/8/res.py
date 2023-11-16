import numpy as np 



with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    
stringx=[]
for element in text[0]:
    stringx.append(element)

# Waldmatrix wird initialisiert 
Waldmat=np.zeros([len(stringx),len(text)])
# Initialisierung Waldmatrixsichtbar
WaldmatVis=np.copy(Waldmat)
# Initialisierung Waldvaluematrix 
WaldmatValue=np.copy(Waldmat)

# Befüllung der Waldmatrix mit Bäumen 
for IndexY,line in enumerate(text):
    for IndexX,element in enumerate(line): 
        Waldmat[IndexY,IndexX]=int(element)
        

# Strahlen werden in den Wald von außen geschoßen
# von links nach rechts 


for index0 in range(Waldmat.shape[0]):
    # init höhe
    maxhoch=-1
    for index1 in range(Waldmat.shape[1]):
        if Waldmat[index0,index1]>maxhoch:
            maxhoch=Waldmat[index0,index1]
            WaldmatVis[index0,index1]=1
            
# von rechts nach linke
for index0 in range(Waldmat.shape[0]):
    # init höhe
    maxhoch=-1
    for index1 in reversed(range(Waldmat.shape[1])):
        if Waldmat[index0,index1]>maxhoch:
            maxhoch=Waldmat[index0,index1]
            WaldmatVis[index0,index1]=1
            
            
# von oben nach unten
for index1 in reversed(range(Waldmat.shape[1])):
    # init höhe
    maxhoch=-1
    for index0 in range(Waldmat.shape[0]):
        if Waldmat[index0,index1]>maxhoch:
            maxhoch=Waldmat[index0,index1]
            WaldmatVis[index0,index1]=1
            
# von unten nach oben 
for index1 in reversed(range(Waldmat.shape[1])):
    # init höhe
    maxhoch=-1
    for index0 in reversed(range(Waldmat.shape[0])):
        if Waldmat[index0,index1]>maxhoch:
            maxhoch=Waldmat[index0,index1]
            WaldmatVis[index0,index1]=1
            
            
print(sum(sum(WaldmatVis)))


def ScoreCalc(index0,index1): 
    hightscoretree=Waldmat[index0,index1]
    # Init calculation: 
    value=[]
    calc=0
    # nach rechts Kalkuliere
    for index11 in range(index1+1,Waldmat.shape[1]):        
        calc+=1
        if Waldmat[index0,index11]>=hightscoretree: 
            break
    value.append(calc)
    # nach unten 
    calc=0
    for index01 in range(index0+1,Waldmat.shape[1]):
          calc+=1
          if Waldmat[index01,index1]>=hightscoretree:
            break 
    value.append(calc)
    # nach links 
    calc=0
    for index10 in reversed(range(0,index1)):
        calc+=1
        if Waldmat[index0,index10]>=hightscoretree:
            break 
    value.append(calc)
    #nach oben 
    calc=0
    for index00 in reversed(range(0,index0)):
        calc+=1
        if Waldmat[index00,index1]>=hightscoretree:
            break 
    value.append(calc)
    
    score=1
    for number in value: 
            score=score*number 
    
    return score




for index0 in range(Waldmat.shape[0]):
    for index1 in range(Waldmat.shape[1]):
        WaldmatValue[index0,index1]=ScoreCalc(index0,index1)
            
            
print(WaldmatValue.max())