# List kam sa to bude ukladat
x = []
print('Enter number:')

# dostaneme cislo

n = input()

#chceme ho pridat do listu x

for i in str(n):
    x.append(i)
    
#skontrolujeme ci sa pridal do listu
    
print(x)

# TATO DEFINICIA BUDE DAVAT MEDZERU MEDZI NIMI PODLA POCTU

#dlzka zoznamu listu
dlzka_zoz = len(x)

def separation():
#kedze sa prida medzera do zoznamu tak sa posunie cele umiestnenie zoznamu o 1
#co znamena ak pouzijeme .append alebo .insert vo for loope tak po kazdom pridani medzeri musim pripocitat k
# i-cku jednu .... v priebehu sa to da pochopit preco

    was_added = 1





#rozdelime si vo funkci zoznam na 3 if statmenty aby sme vedeli rozlisit ci sa jedna o  tisice 10-tisice
# miliony alebo ci uz 6-ciferne cisla
    if dlzka_zoz % 3 == 1:
        print("print moznost 1")
#tuto sme si osetrili aby ked niekto tam da 1-ciferne cislo aby funkcia k tomu nepridala podciarku    
        if dlzka_zoz > 1:
            x.insert(1, "_")
        else:
            pass
#dalej som si spravil for loop ktory ide OD TROCH!  z dovodu ze horny if statement nam spravi
# podciarku na tisicke ale nam dalej staci ked bude za kazdym 3-tim cislom davat medzeru 
        for i in range(3 , dlzka_zoz):
            if i % 3 == 1:
                x.insert(i + was_added, "_")
                was_added += 1
            else:
                pass




            
#tento if statment nam rozdeluje kazde 3-tie cislo zabudol som pripomenut ze x.insert( 1 / 2 / 3 , "_")
#som vyuzil na to aby som vedel odlisit ci cislo bude zacina s 1-cifernym cislom 2-oj alebo 3-oj
# zachvilu vysvetlim preco som pouzil 3 moznost pred prvou       
    elif dlzka_zoz % 3 == 0:
        print("print moznost 3")
        x.insert(3,"_")
        for i in range(4 , dlzka_zoz):
            if i % 3 == 0:
                x.insert(i + was_added , "_")
                was_added += 1





                
#ak si vsimneme ze v prva a treita moznost sa zacina v if statmente dlzka_zoz % 3 == 1 / 0 tak povodne som
# to mal tak ze tato druha moznost mala v sebe dlzka_zoz % 4 == 1 / 0 a nakoniec som dospel k vysledku
# ze dlzka_zoz % 4 == 0 / 1 / 2 / 3 cize obsahovala vsetky 4 moznosti vysledku preto som posunul moznost 3 
# nad moznost 2 z dovodu ze moznost 3 mala 1 konkretny if statment a tato moznsot 2 mala 4. Nakoniec som ju zmenil na else
    else:
        x.insert(2,"_")  
        print("print moznost 2")
#tieto if statmenty su tu cisto z dovovdu ze pridavanim medzier pretoze for loop sa dostal do maxima
# a i uz nemalo taku hodnotu aby bolo schopne pridat elementu 17 a vyssiemu medzeru .
#ak by sme odobrali tieto if statmenty tak nezvladnu 17-ty a 20-ty element . momentalne
#nezvladnu viac ako 20 lebo list je uz prilis velky . ALE ostatne if statmenty to v pohode zvladnu

        if dlzka_zoz == 17:
            x.insert(-3 , "_")
        elif dlzka_zoz == 20:
            x.insert(-3 , "_")
#to iste co predtym
        for i in range(4 , dlzka_zoz):
            if i % 4 == 1:
#od nejakeho 8-ho elementu npotrebujeme aby pridaval k was_added 1 cize sme mu povedali ak je viac ako 1
# nech ho zmeni na 1
                if was_added > 1:
                    was_added = 1
                x.insert(i + was_added, "_")
                was_added += 1

                
#tuto som si len skusal ci pridava cisla a co vykonava was added
    print (was_added)
#uz len vypiseme do konzoly cely list
    
    print (''.join(x))
#zavolame funkciu a sme vybaveny
    
separation()

#ako som pisal funguje to na vsetky elemnty neviem do akych cisel az to vie vystupat bohuzial ta
# druha moznost funguje len do 20-teho elementu ostatne netusim
