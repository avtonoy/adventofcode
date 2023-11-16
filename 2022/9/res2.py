import numpy as np
import matplotlib.pyplot as plt


with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    
class Rope:
    def __init__(self,Position,i) -> None:
        self.Identity=i
        self.Position=Position
        self.LastPosition=np.zeros((2),dtype=int)
        self.LastMove=np.zeros((2),dtype=int)
        self.Tension=int
        self.scoreTail=1
        self.PositionLogTail=Position
        self.LastMoveDiagonal=False
        
    def CalcLastmove(self):
        self.LastMove=self.Position-self.LastPosition    
         
    def move(self,direction): 
        self.LastPosition=self.Position
        match direction:
            case 'R':
                self.Position=np.array([self.Position[0]+1,self.Position[1]])
            case 'U': 
                self.Position=np.array([self.Position[0],self.Position[1]+1])
            case 'L': 
                self.Position=np.array([self.Position[0]-1,self.Position[1]])
            case 'D': 
                self.Position=np.array([self.Position[0],self.Position[1]-1])
        self.LastMoveDiagonal=False
        self.CalcLastmove()
         
    def RopeTension(self,HeadRope): 
        Delta=HeadRope.Position-self.Position
        # Über Pythagoras 
        self.Tension=np.sqrt(np.square(Delta[0])+np.square(Delta[1]))
        
    def PositionTailupdate(self,HeadRope):
        if self.Tension ==2: 
         # Wird Tail wird geraden verschoben
            self.LastPosition=self.Position
            self.Position=(HeadRope.Position - self.Position)/2+self.Position
            self.scoreTail+=1
            self.LastMoveDiagonal =False
        elif self.Tension > 2 and HeadRope.LastMoveDiagonal != True: 
            # Diagonale Verschiebung hinter head 
            self.LastPosition=self.Position
            self.Position=HeadRope.LastPosition  
            self.scoreTail+=1
            self.LastMoveDiagonal = True
        elif self.Tension > 2 and HeadRope.LastMoveDiagonal == True: 
            # Es wird der gleiche Schritt durchgeführt wie der vorgänger 
            self.LastPosition=self.Position 
            self.Position=self.Position + HeadRope.LastMove
            self.scoreTail+=1
            self.LastMoveDiagonal = True
        else:
            self.LastMoveDiagonal = False

            
        self.CalcLastmove()          
        self.PositionLogTail=np.vstack((self.PositionLogTail,self.Position))
                
HeadRope=Rope(np.array([0,0],dtype=int),0)
NumberofTails=9
TailList=[]

# Lege eine Anzahl an Tails objecten an 
for i in range(NumberofTails):
    TailList.append(Rope(np.array([0,0],dtype=int),i+1))

def plotter(): 
        for i in TailList: 
            plt.plot(i.Position[0],i.Position[1],'bo')
    
        plt.plot(HeadRope.Position[0],HeadRope.Position[1],'rD')
        plt.show()
    

for line in text: 
    [movedirect,movelineNumber]=[line.split()[0],int(line.split()[1])]
    for movement in range(movelineNumber): 
        HeadRope.move(movedirect)
        TailList[0].RopeTension(HeadRope)
        TailList[0].PositionTailupdate(HeadRope)
        for i in range(1,NumberofTails):
            TailList[i].RopeTension(TailList[i-1])
            TailList[i].PositionTailupdate(TailList[i-1])
        if movedirect=='L':
            ...
            # plotter()

print(len(np.unique(TailList[NumberofTails-1].PositionLogTail,axis=0,return_counts=True)[1]))