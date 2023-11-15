import numpy as np 

Modus=''
AktuellesDir=['/']
Katalog={'/': {'name': '/', 
               'type': 'dir', 
               'parent': 'none',
               'child': [],
               'size': np.nan}}
LastCmd=[]


with open('input', 'r') as f:
    text=f.readlines() 
    f.close()
    
# Entferne \n 
for line in range(len(text)): 
    text[line]=text[line].rstrip('\n')
    

def Modusbestimmung(line): 
    global Modus
    Arg=line.split()
    if Arg[0]=='$':
        Modus='CMD'
        Arg.pop(0)
    else:
        Modus='OUT'
    
    return Arg

def CMDInterpreter(Shell): 
    global AktuellesDir
    global LastCmd
    if Shell[0]=='cd':
        match Shell[1]:
            case '/':
                AktuellesDir=['/']
            case '..':
                AktuellesDir.pop()
            case other: 
                AktuellesDir.append(AktuellesDir[-1]+Shell[1]+'/')
                
    if Shell[0]=='ls':
        ...
        
    LastCmd=Shell
    return 
                    
def OUTInterpreter(Shell):
    
    Parent=AktuellesDir[-1]
    dirName=Shell[1]
    # Es wird ein Ordner angezeigt
    if Shell[0]=='dir':         
        Type='dir'
        memory = np.nan        
   #ansonsten ist nur noch ein file mögclih 
    else:  
        Type='file'
        memory=int(Shell[0])
        
    Katalogupdate(dirName,Type,Parent,memory)
        
    
def Katalogupdate(*args):
    Name=args[0]
    Type=args[1]
    Parent=args[2]
    memory=args[3]
    
    if Type=='dir':
        Name=Parent+Name+'/'    
    else:
        Name=Parent+Name
        
    Katalog.update({Name: {'name': Name,
                           'type': Type,
                           'parent': Parent,
                           'child': [],
                           'size': memory}})
    # Füge Kinder zu den Eltern hinzu 
    Katalog[Parent]['child'].append(Name)

def sizeupdate_dir(nameofdir):
    
    if np.isnan(Katalog[nameofdir]['size']):
        memory=0
        for Child in Katalog[nameofdir]['child']: 
            if np.isnan(Katalog[Child]['size']):
                sizeupdate_dir(Katalog[Child]['name'])
                memory=memory+Katalog[Child]['size']
            else: 
                memory=memory+Katalog[Child]['size']
    
        Katalog[nameofdir]['size']=memory

                
for index in range(len(text)):
    line=text[index]
    Shell=Modusbestimmung(line)
    if Modus=='CMD':
        CMDInterpreter(Shell)
    if Modus=='OUT': 
        OUTInterpreter(Shell)
    

sizeupdate_dir('/')

Speicher=0
Speicherkatalog100000=dict()
for key in Katalog.keys():
    if Katalog[key]['size']<=100000 and Katalog[key]['type']=='dir': 
        Speicherkatalog100000.update({key: Katalog[key]['size']})
        Speicher=Speicher+Katalog[key]['size']

totalspace=70000000
needspace=30000000
avlspace=totalspace-Katalog['/']['size']
candspace=totalspace #InitKandspace

for key in Katalog.keys(): 
    if Katalog[key]['type'] == 'dir': 
        if avlspace+Katalog[key]['size']>=needspace and candspace>=Katalog[key]['size']:
            candspace=Katalog[key]['size']
            cand=key
print(cand)
print(candspace)