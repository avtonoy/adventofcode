import numpy as np



with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    
class Rope:
    def __init__(self,Position) -> None:
        self.Position=Position
        self.LastPosition=np.zeros((2),dtype=int)
        self.Tension=int
        self.scoreTail=1
        self.PositionLogTail=Position
        
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
    
    def RopeTension(self,HeadRope): 
        Delta=HeadRope.Position-self.Position
        # Über Pythagoras 
        self.Tension=np.sqrt(np.square(Delta[0])+np.square(Delta[1]))
        
    def PositionTailupdate(self,HeadRope):
        if self.Tension >= 2:
            # Wird Tail bewegt und Score gezaehlt
            self.Position=HeadRope.LastPosition  
            self.scoreTail+=1
        self.PositionLogTail=np.vstack((self.PositionLogTail,self.Position))
                
HeadRope=Rope(np.array([0,0],dtype=int))
TailRope=Rope(np.array([0,0],dtype=int))

for line in text: 
    [movedirect,movelineNumber]=[line.split()[0],int(line.split()[1])]
    for movement in range(movelineNumber): 
        HeadRope.move(movedirect)
        TailRope.RopeTension(HeadRope)
        TailRope.PositionTailupdate(HeadRope)

print(TailRope.scoreTail)

print(len(np.unique(TailRope.PositionLogTail,axis=0,return_counts=True)[1]))