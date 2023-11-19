import numpy as np
import matplotlib.pyplot as plt
import math


with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    
    
    

class monkey():
    def __init__(self) -> None:
        self.name=''
        self.items=[]
        self.operation=[]
        self.truethrow=int 
        self.falsethrow=int 
        self.test=int 
        
        
        self.itemschecks=0 
        
        self.boredlevel=1
        self.supermoduli=int 
        
        
    
    def do(self,Monkeys):
        if len(self.items)>0: 
            Items=self.items.copy()
            # Liste der throws

        
            for item in Items:
                # Operand A 
                if self.operation[2]=='old': 
                    A=item
                else: 
                    A=int(self.operation[2])
                
                # Operand B
                if self.operation[4]=='old': 
                    B=item
                else: 
                    B=int(self.operation[4])
                    
                # Oberation 
                Operation = self.operation[3]
                if Operation == '*': 
                    C=A*B
                    Cmod=A*(B%self.test)
                if Operation == '+':
                    C=A+B 
                    Cmod=A+(B%self.test)
                # bored in account 
                # C=math.floor(C/self.boredlevel)
                # Bestimmung wohin gethrowt wird                
                
                
                if C%self.test == 0: 
                    throw=self.truethrow
                else: 
                    throw=self.falsethrow 
                
                self.itemschecks+=1
                
                Monkeys[throw].items.append(C%self.supermoduli)
            # Itemliste wird geleert
            self.items=[]
            # self.boredlevel+=1
            
                    

def builtMonkeyhouse(text): 
    
    Monkeyhouse=[]
        
    for line in text: 
        if len(line.split())>=2:
            
            if line.split()[0].__contains__('Monkey'): 
                Monkeyhouse.append(monkey())
                Monkeyhouse[-1].name = line.split()[1].split(':')[0]

            elif line.split(':')[0].__contains__('Starting items'):
                items=line.split(':')[1].split(',')
                for item in items:
                    Monkeyhouse[-1].items.append(int(item))
                    
            elif line.split(':')[0].__contains__('Operation'):
                items=line.split(':')[1].split(' ')
                items.pop(0)
                for item in items: 
                    Monkeyhouse[-1].operation.append(item)
            
            elif line.split(':')[0].__contains__('Test'):
                Monkeyhouse[-1].test=int(line.split()[3])
                
            elif line.split(':')[0].__contains__('If true'):
                Monkeyhouse[-1].truethrow=int(line.split()[5])
                
            elif line.split(':')[0].__contains__('If false'):
                Monkeyhouse[-1].falsethrow=int(line.split()[5])
    
    # calc and set supermoduli
    supermoduli=1
    for Monkey in Monkeyhouse:
        supermoduli=Monkey.test*supermoduli
    for Monkey in Monkeyhouse: 
        Monkey.supermoduli=supermoduli
        
    return Monkeyhouse

def monkeycircle(nRound):
    Monkeys=builtMonkeyhouse(text)
    for round in range(nRound):
        for Monkey in Monkeys:
            Monkey.do(Monkeys)
    A=[]
    for Monkey in Monkeys: 
        A.append(Monkey.itemschecks)
        A.sort()
    print(A[-1]*A[-2])
        
    return Monkeys[2].itemschecks

print(monkeycircle(10000))



# for round in range(20):
#     for Monkey in Monkeys:
#         Monkey.do(Monkeys)

# # A=[]
# # for Monkey in Monkeys: 
#     print(Monkey.itemschecks)
#     A.append(Monkey.itemschecks)

# # A.sort()
# # print()
# # print (A[-1]*A[-2])