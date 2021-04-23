MAXIMUM_ROWS_ALLOWED = 49
MAXIMUM_COLUMNS_ALLOWED = 204

def createPlayingBoard(rows, columns):
    if type(rows) != int or type(columns) != int:
        return False
   
    if rows <= 1 or columns <= 1:
        return False

    if rows > MAXIMUM_ROWS_ALLOWED or columns > MAXIMUM_COLUMNS_ALLOWED:
        return False

    for row in range(0, rows):
        if row % 2 == 0:
            for column in range(0, columns):
                if column % 2 == 0:
                    endChar = ""
                    if column == columns - 1:
                        endChar = "\n"
                    print(" ", end = endChar)
                else:
                    print("|", end="")

        else:
            for column in range(0, columns):
                endChar = ""
                if column == columns - 1:
                    endChar = "\n"
                print("-", end=endChar)
    print("")
    return True
    


def playingBoardCreated(rows, columns):
    if(createPlayingBoard(rows, columns)):
        print('Here is your playing board.')
    else:
        print('Err, No playing board for you.')


playingBoardCreated(5, 5)