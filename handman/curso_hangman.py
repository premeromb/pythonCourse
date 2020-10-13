import random

print("H A N G M A N ")

words = 'python', 'java', 'kotlin', 'javascript'

word = random.choice(words)

wordSet = set(word)

gessedSet = set()  

failedSet = set()

lives = 8
win = False

while lives != 0:

    print("")

    #print current caracters
    for i in range(len(word)):
        if word[i] in gessedSet:
            print(word[i], end="")
        else:
            print("-", end="")

    print("")

    if set(wordSet) == set(gessedSet):
        print("You guessed the word!")
        print("You survived!")
        break

    read = input("Input a letter: ")

    if 0 < len(read) > 1:
        print("You should input a single letter")
        continue
    if read.islower() == False:
        print("Please enter a lowercase English letter")
        continue
    if read in gessedSet or read in failedSet:
        print("You've already guessed this letter")
        continue
    elif read in word:
        gessedSet.add(read)
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
        failedSet.add(read)

else:
    print("You lost!")

