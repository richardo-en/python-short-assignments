import random
import string
result_str = ""
def get_random_string(length):
    # choose from all lowercase letter
    letters = (string.ascii_lowercase + string.punctuation + string.digits)
    for i in range(length):
        result_str = ''.join(random.choice(letters))
    print("Random string of length " , length , " is:", result_str)

get_random_string(5)


