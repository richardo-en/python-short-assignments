
#prva uloha
hodnoty=[5,11,-7,5,-6,7,9,1,-4]
print(hodnoty)
    
first = hodnoty[2] + hodnoty[0]
print(first)

second = 8+len(hodnoty)
print(second)

third = hodnoty[0]+hodnoty[3]
print(third)

fourth = 0-hodnoty[1]+hodnoty[5]
print(fourth)



hodnoty[2]= first
hodnoty[0]= second
hodnoty[4]= third
hodnoty[6]= fourth
print(hodnoty)
print("\n")

#druha uloha

pocet_otestovanych = 2644
kolko_krat = 0
for i in range(pocet_otestovanych):
    if i > 1200:
        kolko_krat = i

print(kolko_krat)
print("\n")

#tretia uloha
teploty=[ 5 , 12 , 11 , 4 , 3 , 9 , 15 , 4 , 14 , 18 , 12 , 18 , 16 , 9 , 10]

print(teploty)

for i in range(1 , len(teploty) + 1 ):
    print(teploty[-i])

print("\n")

#stvrta uloha
counter = 0
cislo = 0


while cislo < 250 :
    cislo += 13
    counter +=1
print("vsetkych nasobkov je " + str(counter))
