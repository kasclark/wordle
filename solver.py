from operator import index
import re
import string

badLetters = list()
goodLetters = list()
goodPositions = ['','','','','']
badPositions = ['','','','','']

# load word list
def load_word_list():
    wordlist = list()
    with open("fiveletters.txt") as f:
        for line in f:
            wordlist.append(line.rstrip('\n'))
    print(len(wordlist), "words loaded")
    return wordlist

# filter for good positions
def filter_good_positions(wordlist):
    badWords = list()
    for word in wordlist:
        w=[]
        w[:0]=word
        for x,y in zip(w,goodPositions):
            if y != '':
                if x != y:            
                    badWords.append(word)  
                    break  

    wordlist = [r for r in wordlist if r not in badWords]
    print(len(wordlist), "words left")
    return wordlist

# filter out bad letters
def filter_bad_letters(wordlist):
    badWords = list()
    for word in wordlist:
        for letter in badLetters:
            #print("testing", letter, "in", word)
            if letter in word:
                #print("found ", letter, " in ", word)
                badWords.append(word)
                break
            
    wordlist = [r for r in wordlist if r not in badWords]
    print(len(wordlist), "words left")
    return wordlist

# filter for good letters
def filter_good_letters(wordlist):
    badWords = list()
    for word in wordlist:
        for letter in goodLetters:
            if letter not in word:
                #print(letter, "not in ", word)
                badWords.append(word)
                #print("removed", word, "cuz no", letter)
                break

    wordlist = [r for r in wordlist if r not in badWords]
    print(len(wordlist), "words left")
    return wordlist

# filter bad positions
def filter_bad_positions(wordlist):
    badWords = list()
    for word in wordlist:
        w=[]
        w[:0]=word
        for x,y in zip(w,badPositions):
            if x == y:
                badWords.append(word)

    wordlist = [r for r in wordlist if r not in badWords]
    print(len(wordlist), "words left")
    return wordlist 

# print list to file
def save_output(wordlist):
    output = open("output.txt", 'w')
    for word in wordlist:
        output.write("{0}\n".format(word))
    output.close()
    if(len(wordlist)<20):
        print('\n'.join(wordlist))


# main loop
myWordlist = load_word_list()
myChoice = 1
while(True):
    myChoice = input("Enter choice (0 - Exit, 1 - Guess): ")
    if(myChoice == '0'):
        print("Exiting...")
        break
    elif(myChoice != '1'):
        print("Choice not recognized...")
        break
    else:
        myGuess = list(input("What is your 5 letter guess?: "))
        if(len(myGuess) != 5):
            print("Your guess must be 5 letters.")
            continue
        myResults = list(input("What were the results? (g - green, y - yellow, b - black): "))
        if(len(myResults) != 5):
            print("Your results must be 5 letters.")
            continue
        for letter in myGuess:
            if(myResults[myGuess.index(letter)] == 'g'):
                goodPositions[myGuess.index(letter)] = letter
                goodLetters.append(letter)
            elif(myResults[myGuess.index(letter)] == 'y'):
                badPositions[myGuess.index(letter)] = letter
                goodLetters.append(letter)
            elif(myResults[myGuess.index(letter)] == 'b'):
                badLetters.append(letter)
            else:
                print("Your results must be 'g', 'y', or 'b'.")

        # # testing
        # print("goodPositions:", goodPositions)
        # print("goodLetters:", goodLetters)
        # print("badPositions:", badPositions)
        # print("badLetters:", badLetters)

        # update the wordlist
        myWordlist = filter_good_positions(myWordlist)
        myWordlist = filter_bad_letters(myWordlist)
        myWordlist = filter_good_letters(myWordlist)
        myWordlist = filter_bad_positions(myWordlist)
        save_output(myWordlist)


