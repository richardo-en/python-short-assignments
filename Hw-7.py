#   THIS IS HOMEWORK FOR SETS
#   THIS IS HOMEWORK FOR SETS
#   THIS IS HOMEWORK FOR SETS

music = []
music_set = {}

def add_to_set():
    genre = str(input("What genre do you like to choose: "))
    interprets = int(input("How many interprets do like in this genre: "))
    music.append(genre)
    if genre not in music_set:
        music_set[genre] = interprets
        print(music_set)
    else:
        print("This genre is already in set")

            
def to_guess():
    genre_to_guess = str(input("Write genre you guess is in set: "))
    if genre_to_guess in music_set:
        interprets_to_guess = int(input("Right! You guessed right genre now guess how many interprets are good: "))
        x = int(music_set[genre_to_guess])
        if interprets_to_guess == x:
            print("You are super right you guessed 2 out of 2")
        else:
            print("wrong guess of good interprets")
    else:
        print("You guessed wrong genre. you can try it again!")

add_to_set()
to_guess()
