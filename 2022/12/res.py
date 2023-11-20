import numpy as np
import matplotlib.pyplot as plt
import math
import string
import copy

def readinput(input): 

    with open(input, 'r') as f:
        text=f.readlines() 
        f.close()
        
    # Entferne \n 
    for line in range(len(text)): 
        text[line]=text[line].rstrip('\n')
    
    return text   
     
def CreateMat (text):
    sy=len(text)
    sx=len(list(text[0]))

    HilMat=np.zeros((sy,sx))

    for y in range(sy):
        line=text[y]
        for x in range(sx): 
            HilMat[y, x]=ord(list(line)[x])
            if HilMat[y,x]== ord('S'):
                startpoint=(y,x)
                # tausche mit klein a aus 
                HilMat[y,x]=ord('a')
            if HilMat[y,x]==ord('E'):
                endpoint=(y,x)
                #tausche mit höchsten elevation aus 
                HilMat[y,x]=ord('z')
    
    maxidxx=sx-1
    maxidxy=sy-1
    return (HilMat,maxidxx, maxidxy,startpoint,endpoint)

class walker_class():
    def __init__(self,HilMat) -> None:
        self.HilMat=HilMat[0]
        self.maxidxx=HilMat[1]
        self.maxidxy=HilMat[2]
        self.starpoint=HilMat[3]
        self.endpoint=HilMat[4]
        
        self.log=[]
        self.log.append((self.starpoint))
        self.possteps='v>^<'        
        self.steps=0
        self.success=False
        self.deadend=False
    
    def step(self,previous,step):
        
        if step == 'v':
            self.log.append((previous.log[-1][0]+1,previous.log[-1][1]))
            self.steps+=1
            
        if step == '>': 
            self.log.append((previous.log[-1][0],previous.log[-1][1]+1))
            self.steps+=1
        
        if step == '^': 
            self.log.append((previous.log[-1][0]-1,previous.log[-1][1]))
            self.steps+=1
            
        if step == '<': 
            self.log.append((previous.log[-1][0],previous.log[-1][1]-1))
            self.steps+=1

            
        if self.step_check():
            if self.steep_check():
                for direction in self.possteps:
                    A.append(copy.deepcopy(self))
                    idx = len(A)-1
                    A[idx].step(self,direction)
                
            
    def steep_check(self): 
        if self.HilMat[self.log[-1]]-self.HilMat[self.log[-2]]>1: 
            self.deadend=True
            return False
        elif self.log[-1]==self.endpoint:
            self.success=True
            return False
            
        else: 
            
            return True
        pass
        
    def step_check(self): 

        
        # Prüfung ob in suchbereich
        if self.log[-1][0] >=0 and \
            self.log[-1][1] >=0 and \
            self.log[-1][0] <= self.maxidxy and \
            self.log[-1][1] <= self.maxidxx: 
                # prüfe ob schonmal dort gewesen
                for index in range(len(self.log)-1):
                    if self.log[index]==self.log[-1]:
                        self.deadend=True
                        return False
                return True 
        else:
            self.deadend=True
            return False
                    
            
        
            
            

                
                
                
text=readinput('inputtest')
walker=walker_class(CreateMat(text))

A=[]
for step in walker.possteps:
    A.append(copy.deepcopy(walker))
    idx=len(A)-1
    A[idx].step(walker,step)
    
inplot=[]
for i in A: 
    if i.success==True:
        inplot.append(i.steps)
    
c=plt.plot(inplot)
plt.show()