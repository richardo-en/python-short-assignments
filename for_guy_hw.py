x=[]
print("zadaj spz: ")
spz = input()

for i in str(spz):
    x.append(i)

print(x)
def check_city():
    if x[0] == "b" or x[0] == "B":
        print("bratislava")
    else:
        print("toto neni bratislava")

check_city()
