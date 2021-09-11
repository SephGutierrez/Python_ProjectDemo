import random
def hangman():
    
    word = random.choice(["grizzly" ,  "panda" , "icebear"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessMade = ''
    
    while len(word) > 0:
        main = ""
        missed = 0
        
        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(f"You got it! {main}")
            break
        
        print("Guess the word" , main)
        guess =  input()
        
        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print("Enter valid character")
            guess =  input()
            
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left!")
                print(" ----------- ")
            if turns == 8:
                print("8 turns left!")
                print(" ----------- ")
                print(" -----O---- ")
            if turns == 7:
                print("7 turns left!")
                print(" ----------- ")
                print(" -----O---- ")
                print(" -----|---- ")
            if turns == 6:
                print("6 turns left!")
                print(" ----------- ")
                print(" -----O---- ")
                print(" -----|---- ")
                print(" ----/----- ")
            if turns == 5:
                print("5 turns left!")
                print(" ----------- ")
                print(" -----O---- ")
                print(" -----|---- ")
                print(" ----/-\--- ")
            if turns == 4:
                print("4 turns left!")
                print(" ----------- ")
                print(" -----O---- ")
                print(" ----/|---- ")
                print(" ----/-\--- ")
            if turns == 3:
                print("3 turns left!")
                print(" ----------- ")
                print(" -----O---- ")
                print(" ----/|\--- ")
                print(" ----/-\--- ")
            if turns == 2:
                print("2 turns left!")
                print(" ----------- ")
                print(" -----O---- ")
                print(" ----/|\|-- ")
                print(" ----/-\--- ")
            if turns == 1:
                print("1 turns left!")
                print(" ----------- ")
                print(" ------------O---- ")
                print(" ︻デ═一----/|\-- ")
                print(" ----------/-\--- ")
            if turns == 0:
                print("You lose, you let the man died. ")
                print("̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿")
                break
                

name = input("Please input your name: ")
print(input(f"Welcome: {name}"))
print("-----------------------")
print("Guess the word in less than 10 attempts.")
hangman()
print()

