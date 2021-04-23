import random , math
import numpy as np
list_randNum = [random.randrange(1,20) ,random.randrange(21,50)]
x = random.choice(list_randNum)
xx = random.choice(list_randNum)
y = random.randrange(6,20)
z = random.randrange(21,40 , 3)
assignment = ""
result = []
resuktZlozene_cisla=[]
vysledok = 0
number = 0
postup = ""
cislo_dva = random.randrange(1,20 , 2)
'''
        PRVOCISLA
        PRVOCISLA
        PRVOCISLA
'''
def prvocislo(assignment , number , vysledok):
    if x < 21:
        assignment = "VYMENUJ vsetky prvocisla z cisla " + str(x)
        if x >= 3:
            result.append(2)
        for i in range(1 , x + 1):
            if i % 2 == 1:
                result.append(i)
        result.remove(1)
        print(assignment)
        print( "vysledok je: ", result)
    elif x >20:
        assignment = "VYPOCITAJ kolko existuje prvocisiel v cisle " + str(x)
        number
        for i in range(1 , x + 1):
            number += i
        vysledok = number/x+1
        vysledok = math.floor(vysledok)
        print(assignment)
        print("v cisle " +str(x) +" je " + str(vysledok) + " prvocisel" )
prvocislo(assignment, number  , vysledok)


'''
        ZLOZENE CISLA
        ZLOZENE CISLA
        ZLOZENE CISLA
'''

def zlozenecisla(assignment , number ):
    assignment = "VYMENUJ vsetky zlozene cisla z cisla " + str(y)
    for i in range(1 , y + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 6 == 0:
            resuktZlozene_cisla.append(i)
    resuktZlozene_cisla.remove(3)
    resuktZlozene_cisla.remove(5)
    print(assignment)
    print( "vysledok je: ", resuktZlozene_cisla)
zlozenecisla(assignment , number )
'''
        NAJVACSI SPOLOCNY DELITEL
        NAJVACSI SPOLOCNY DELITEL
        NAJVACSI SPOLOCNY DELITEL
'''
def najvacsiSpolocnyDelitel(assignment , vysledok):
    assignment = "VYPOCITAJ  najvacsieho spolocneho delitela "  + str(z) + " a z cisla " + str(cislo_dva)
    print(assignment)
    vysledok = vysledok - vysledok
    vysledok = math.gcd(cislo_dva , z)
    if vysledok == 0 or vysledok == 1:
        print("tieto cisla su nesúdeliteľné")
    else:
        print("tieto cisla su delitelne cislom " +str(vysledok) + " tzn. ze je súdeliteľné.")

najvacsiSpolocnyDelitel(assignment , vysledok)
    


    
    
    
