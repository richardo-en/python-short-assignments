"""
Create a note-taking program. When a user starts it up, it should prompt them for a filename.

If they enter a file name that doesn't exist, it should prompt them to enter the text they
want to write to the file. After they enter the text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents of the file on the screen.
If the user wants to start over then the file should be deleted and another empty one made in its place.
If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 

My Notes: what we have to do is we create some file.txt where will be saved name of created files
and print them to let user know what is already exist

Second step: we ask user what does he want to do create a new file rewrite old one
Third oprions for read , start over and for append

"""
import os

print("These files already exists\n")

if os.path.exists("Files.txt"):
    FilePlace = open("Files.txt" , "r")

    for i in FilePlace:
        print(i + "\n")
    FilePlace.close()
else:
    FilePlace = open("Files.txt" , "x")
    FilePlace.close()


reading = []


def next_step():
    #choose what do you want to do
    WhatIsNext = input("If you want to read file write READ. If you want to overwrite file write OVER. If you want add something to file write ADD. If you want create new file write CREATE.\n")
    #write file name you want work with
    FileName = input("Write filename you want to work with: ")
    if WhatIsNext == "READ":
        
        FilePlace = open("{}".format(FileName) , "r")
        
        for i in FilePlace:
            print(i)
                
        FilePlace.close()
        return next_step()

        
    elif WhatIsNext == "OVER" or WhatIsNext == "CREATE":

        if WhatIsNext == "OVER":
            if os.path.exists(FileName):
              os.remove(FileName)
              print("removed")
            else:
              print("The file does not exist")
              return next_step()
        elif WhatIsNext == "CREATE":
            FilePlace = open("{}".format(FileName) , "x")
            FilePlace.close()

            FilePlace = open("Files.txt", "a")
            FilePlace.write("{}\n".format(FileName) )
            FilePlace.close()
          

        FilePlace = open("{}".format(FileName) , "a")
        HowMuch = int(input("How much notes do you want to input: "))
        for i in range(HowMuch):
            note = input("Write note you want to input: ")
            FilePlace.write(note)
            FilePlace.write("\n")
        FilePlace.close()
        return next_step()
          

    elif WhatIsNext == "ADD":
        if os.path.exists(FileName):

            FilePlace = open("{}".format(FileName) , "a")
            HowMuch = int(input("How much notes do you want to input: "))
            
            for i in range(HowMuch):
                note = input("Write note you want to input: ")
                FilePlace.write(note)
                FilePlace.write("\n")
            FilePlace.close()
            return next_step()

        else:
            print("This file doesnt exist. You have to create it")
            return next_step()
        return next_step()
    else:
        return next_step()

next_step()
