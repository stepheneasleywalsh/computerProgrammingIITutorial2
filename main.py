# We need random to pick a word at random
import random

# This will store the list of names
vocab = []

# This is to LOAD the names into the list called vocab
# When the user inputs a blank, it is done loading
while True:
    name = input("Give me a name: ")
    if not name == "":
        vocab.append(name)
    else:
        print("OK :) I will pick a name at random. ")
        break

# This picks a random item from the list from 0 to length-1
n = random.randint(0,len(vocab)-1)

# Now, time to guess.
while True:
    guess = input("What is the name I am thinking of? ")
    if guess.lower() == vocab[n].lower():
        print("Correct")
        quit()
    elif guess.lower() < vocab[n].lower():
        print("No but it comes after", guess)
    else:
        print("No but it comes before", guess)
