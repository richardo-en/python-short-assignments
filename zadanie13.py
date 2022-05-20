def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    elif num <1:
        print("toto cislo v binarnej sustave sa rovna dvom")
    list.append(num % 2)
 
while True:
    list = []
    dec_val = int(input("zadaj cislo\n"))
    DecimalToBinary(dec_val)
    
    list.remove(0)
    print(*list , sep="")

    odpoved = str(input("chces pokracovat? ano/nie\n"))

    if odpoved == "nie":
        break
    elif odpoved == "ano":
        pass
    else:
        while True:
            odpoved2 = str(input("zla odpoved! Chces pokracovat? ano/nie\n"))
            if odpoved2 == "nie":
                exit()
            elif odpoved2 == "ano":
                break
            else:
                pass
