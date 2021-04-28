#here you have to choose what board size you want
what_to_chose = input("if you want squer board say SQUER if you want custom size say CUSTOM: ")

def choose():
    #you choose squer
    if what_to_chose == "SQUARE":
        #we want x * x board so we need just one number
        column = int(input("choose how many columns: "))
        #printing all that gaming board
        for i in range(1 , column + 1):
            print(str(i) + "|" + "__|" * int(column))
        print("write AGAIN if you want do it again")
    #you choose custom
    if what_to_chose == "CUSTOM":
        #we want custom size board so we need 2 parameters
        column = int(input("choose how many columns: "))
        rows = int(input("choose how many rows: "))
        if column == rows:
            print("you should choose SQUARE")
        #printing that board
        for i in range(1 , rows + 1):
            print(str(i) + "|" + "__|" * int(column))
        print("write AGAIN if you want do it again")

choose()

#here i am calling back choose function 
while input() == "AGAIN":
    what_to_chose = input("if you want squer board say SQUER if you want custom size say CUSTOM: ")
    choose()
    
