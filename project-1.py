#0 1 2 3 4 5 6 7 8
#| X | X | X | X |


playing_field = [ [ " "  , " "  , " "  , " "  , " "  , " "  , " "  , ] ,
                  [ " "  , " "  , " "  , " "  , " "  , " "  , " "  , ] ,
                  [ " "  , " "  , " "  , " "  , " "  , " "  , " "  , ] ,
                  [ " "  , " "  , " "  , " "  , " "  , " "  , " "  , ] ,
                  [ " "  , " "  , " "  , " "  , " "  , " "  , " "  , ] ,
                  [ " "  , " "  , " "  , " "  , " "  , " "  , " "  , ] ]
def drwa_field(field):
    
    print("  1|2|3|4|5|6|7|")
    print("----------------")
    for row in range(12):
        if row % 2 ==0:
            row_control = int(row/2)
            
            print(str(row_control +1)  + "|", end = "")
            for column in range(14):
                if column % 2 ==0:
                    column_control = int(column/2)
                    if column !=13:
                        print(field[row_control][column_control],end = "")
                    else:
                        print(field[row_control][column_control])
                else:
                    print("|" , end = "")

        else:
            print("\n----------------")

drwa_field(playing_field)

player = 1

while(True):
    if player == 1:
        #if player gets input 7 you have to go trough list 5 , 4 ... till you find clean field 
        field_num=int(input("Now is players one turn! Write field you want input:\n"))
        field_num -= 1
        for i in range(1 ,7):
            if player == 1:
                if playing_field[-i][field_num] == " ":
                    playing_field[-i][field_num] = u'\u2605'
                    print(playing_field[0][field_num])
                    player += 1
                elif playing_field[0][field_num] == u'\u2605' or playing_field[0][field_num] == u'\u2B24':
                    print("This column is full!\n")
                    player = 1
    else:
        field_num=int(input("Now is players two turn! Write field you want input:\n"))
        field_num -= 1
        for i in range(1 ,7):
            if player == 2:
                if playing_field[-i][field_num] == " ":
                    playing_field[-i][field_num] = u'\u2B24'
                    print(playing_field[0][field_num])
                    player -= 1
                elif playing_field[0][field_num] == u'\u2605' or playing_field[0][field_num] == u'\u2B24':
                    print("This column is full!\n")
                    player = 2
    drwa_field(playing_field)



print(u'\u2B24')
