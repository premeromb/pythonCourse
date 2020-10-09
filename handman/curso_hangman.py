import random

print("H A N G M A N ")

words = 'python', 'java', 'kotlin', 'javascript'

word = random.choice(words)

wordSet = set(word)

gessedSet = set()  #añadir con gessedSet.add('')

for i in range(8):

    print("")

    #print current caracters
    for i in range(len(word)):
        if word[i] in gessedSet:
            print(word[i], end="")
        else:
            print("-", end="")

    print("")

    read = input("Input a letter: ")

    if read in word:
        gessedSet.add(read)
    else:
        print("That letter doesn't appear in the word")

    
print("\nThanks for playing! \nWe'll see how well you did in the next stage")


#if set(wordSet) == set(wordSet):
#    print("You Win!")
#else:
#    print("You Lost!")

