import numpy as np
import matplotlib.pyplot as plt


with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    
# Wird auf True gesetzt sobald ein Programm aktiv ist 
handle=False
# Startwert für X
X=1

class clock_class: 
    def __init__(self) -> None:
        self.state='low'    #low ascend high descend
        self.cyclecounter=0 
        
    
    def tick(self):
        match self.state:
            case 'low':
                self.state='ascend'  # fetch and cycle up 
                self.cyclecounter+=1
            case 'ascend': 
                self.state='high'  # FRQ logging
            case 'high': 
                self.state='descend' # Excecute
            case 'descend':
                self.state='low'
            
    # low -> ascend: fetching

class decoder_class: 
    def __init__(self,text) -> None:
        self.Interuptor=False
        self.CMD=text
    
    def fetch(self,worker):
        if len(self.CMD)>0:
            return worker(self.CMD.pop(0))
        else: 
            self.Interuptor=True
        
        
class worker_class: 
    def __init__(self,CMD) -> None:
        global handle
        handle = True
        A=CMD.split()
        if A[0]=='addx':
            self.type='adder'
            self.AddValue=int(A[1])
            self.cycle=0 
            self.cycletowork=2
        
        if A[0]=='noop':
            self.type='noop'
            self.cycle=0
            self.cycletowork=1
    
    def do(self,clock): 
        if clock.state=='ascend': 
            self.cycle+=1
        if clock.state=='descend': 
            if self.type=='noop': 
                self.noop()
            if self.type=='adder':
                self.adder()
                
                
    def noop(self): 
        if self.cycle >= self.cycletowork: 
            # do nothing return handel 
            global handle 
            handle = False
    
    def adder(self): 
        if self.cycle >= self.cycletowork: 
            global X
            X=X+self.AddValue
            global handle 
            handle = False
            
class frqlogger_class(): 
    def __init__(self) -> None:
        self.nextmeasure=20
        self.frqsteps=40
        self.frq=[]
        self.frqmeasure=[]
        self.signalstrenght=[]

    def measure(self,clock):
        if clock.cyclecounter >= self.nextmeasure and clock.state=='high':
            global X
            self.frq.append(clock.cyclecounter)
            self.frqmeasure.append(X)
            self.signalstrenght.append(clock.cyclecounter * X)
            self.nextmeasure += self.frqsteps
        
            


    
decoder=decoder_class(text)
clock=clock_class()
frqlogger=frqlogger_class()

while decoder.Interuptor!=True:
    clock.tick()
    if handle !=True and clock.state=='ascend': 
        worker=decoder.fetch(worker_class)
        if decoder.Interuptor:
            break
    worker.do(clock)
    frqlogger.measure(clock)
    
print(X)
print(clock.cyclecounter)

print(frqlogger.frq)
print(frqlogger.frqmeasure)
print(frqlogger.signalstrenght)
print(sum(frqlogger.signalstrenght))
