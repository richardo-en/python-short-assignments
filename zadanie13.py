def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
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
            if odpoved == "nie":
                exit()
            elif odpoved == "ano":
                break
            else:
                pass