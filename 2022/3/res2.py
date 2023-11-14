


def asciii2realval(asciival): 
    # Unterscheidung zwischen klein und Großbuchstaben 
    # Bei Großbuchstaben werden folgende priorisierung definiert 
    if asciival < 97: 
        return asciival-65+27 # 27 nach Priorisierung
    # Für Kleinbuchstaben
    if asciival >= 97:
        return asciival-97+1 


with open('input', 'r') as f: 
    text=f.readlines()
    f.close()
    
# tex2="""vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

# text=tex2.split()

Compartment1=[]
Compartment2=[]
Compartment3=[]
GleichItem=[]



for Indextext in range(0,len(text),3):
    # Zerlege die Kompartments nach codierung genau in der hälfte 
    Compartment1.append(text[Indextext][:-1])
    Compartment2.append(text[Indextext+1][:-1])
    Compartment3.append(text[Indextext+2][:-1])
    
    # Vergleiche die Compartment und schreibe buchstaben 
    # die in beiden compartsment vorkommen nieder
    EintraginGleichItem=''
    
    
    for Zeichen1 in Compartment1[-1]:
        for Zeichen2 in Compartment2[-1]:
            for Zeichen3 in Compartment3[-1]:
                if Zeichen2 == Zeichen1==Zeichen3:
                    LogischEintrag=True # Es wird davon ausgegangen dass der Eintrag gemacht wird
                    # Falls der Eintrag schon vorhanden ist wird dieser nicht getätigt 
                    for ZeicheninGleichItem in EintraginGleichItem: 
                        if Zeichen1==ZeicheninGleichItem:
                                LogischEintrag=False
                                break
                    # Fall durch einen Doppelt Eintrag dieser nicht gehindert wird so wird dieser getätigt
                    if LogischEintrag:
                        EintraginGleichItem=EintraginGleichItem+Zeichen1
    
    GleichItem.append(EintraginGleichItem)
    
    ## Bildung der Values für die Priorisierung
    
ValueList=[] # Liste für die Values 
     
for Item in GleichItem: 
    for Index,Buchstabe in enumerate(Item): 
        asciiValue=ord(Buchstabe)
            # hier der ascii Value in einen echten zu priorisierenden
        realValue=asciii2realval(asciiValue)
        if Index==0:

            ValueList.append(realValue)
        else: 
            # Im fall von mehrer Buchstaben die in beiden Compartments gleich sind wird der value dazu
            # addier 
            ValueList[-1]+=realValue

print(sum(ValueList))

