import numpy as np
import matplotlib.pyplot as plt
import math


with open('inputtest', 'r') as f:
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
        
        self.boredlevel=3
        
    
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
                if Operation == '+':
                    C=A+B 
                    
                # bored in account 
                C=math.floor(C/self.boredlevel)
                # Bestimmung wohin gethrowt wird                
                
                if C%self.test == 0: 
                    throw=self.truethrow
                else: 
                    throw=self.falsethrow 
                
                self.itemschecks+=1
                
                Monkeys[throw].items.append(C)
            # Itemliste wird geleert
            self.items=[]
            
                    

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

    return Monkeyhouse

Monkeys=builtMonkeyhouse(text)

# Monkeys[0].do(Monkeys)
# Monkeys[1].do(Monkeys)
# Monkeys[2].do(Monkeys)
for round in range(20):
    for Monkey in Monkeys:
        Monkey.do(Monkeys)

A=[]
for Monkey in Monkeys: 
    print(Monkey.itemschecks)
    A.append(Monkey.itemschecks)

A.sort()
print (A[-1]*A[-2])