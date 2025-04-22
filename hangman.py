import random #Python has a built in Random module, which is great because iterating 
#through arrays makes my head hurt

word_list = ['dork', 'weasel', 'jabroni', 'snollygoster', 'Cockalorum', 'suckup', 'lickspittle', 'pillock', 'ninnyhammer']
#This array sets up the list of insults that will get you hanged

word = random.choice(word_list)#uses built in random module to randomly select one word
word_letters = set(word) #converts the word into a set of unique letters
#set is another built in data structure.
#It supports membership tests which helps us track guessed letters.
#So hello would break down into ['h', 'e', 'l', 'l', 'o']
guessed_letters = set() #converts guesses into a set
incorrect_guesses = set() #converts incorrect guesses into a set
attempts = 6 #number of guesses

print('Welcome to Hangman!')
print(f'The word has {len(word)} letters.') #starting message.
#f = formatted string literal
#F-strings allow you to embed expressions inside string literals.  
#Formatted strings were in JS as well 
#Fstrings allows us to include variables or expressions inside strings.


#main game loop
#Keeps looping while the user has attempts >0 and hasn't guessed the word
while attempts > 0 and word_letters:
    display =[letter if letter in guessed_letters else '_' for letter in word]
    #builds list of letters to show which letters have been guessed so far.
    #displays _ if guess hasn't been guessed yet.
    print('word:', "".join(display)) #displays progress

    print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))}")
    #shows incorrect guesses.
    print(f"You have {attempts} guesses left")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) !=1:
        print("please enter a single valid letter.")
        continue
    if guess in guessed_letters or guess in incorrect_guesses:
        print("You've already guessed that letter.")
        continue
    if guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("Good guess!")
        continue
    else:
        incorrect_guesses.add(guess)
        attempts -= 1
        print("Wrong guess.")

    print("-" * 40)

if not word_letters:
    print(f"Congratulations! You guessed the word: {word}")

else: 
    print(f"Out of guesses! The Word was: {word}")