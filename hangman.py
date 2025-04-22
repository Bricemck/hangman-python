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
    #f is formatted string literal like the javascript backticks.
    #Everything inside {} will be converted to a string 
    #So the number of incorrect_guesses will be displayed.
    #Join takes a list of strings and glues them together using the string before
    #As a separator.  So I add ', ' and it will print in a readable way.
    #Sorted is helpful for showing the incorrect_guesses in order they were guessed.
    #Otherwise they might return haphazard.
    print(f"You have {attempts} guesses left")
    #Same as above but obviously with attempts instead of incorrect_guesses.
   
    guess = input("Guess a letter: ").lower() #.lower avoids case issues.

    if not guess.isalpha() or len(guess) !=1: #Checks if the input is a single character.
        #If not skips to the next loop.
        #Guess is my input function. isalpha() checks for alphabetical inputs.
        #len(guess) !=1 checks if the length of the guess is not equal to 1.
        #We only one one character guesses so this makes anything else invalid.
        print("please enter a single valid letter.") #error message for the player.
        continue #skips the rest of the loop and goes back to the top for user input.
    if guess in guessed_letters or guess in incorrect_guesses: 
        print("You've already guessed that letter.")
        #prevents duplicate guesses by printing an error message.
        continue
    if guess in word_letters: #If the letter is in the word.
        guessed_letters.add(guess) #add it to guessed letters.
        word_letters.remove(guess) #remove it from word letters.
        print("Good guess!") #success message.
        continue #skip loop, return to top for user input.
    else:
        incorrect_guesses.add(guess) #if guess is wrong add to incorrect logic
        attempts -= 1 #decrease attempts by one.
        print("Wrong guess.") #error message.

    print("-" * 40) #Visual separator for easy 

if not word_letters: #checks to see if all the letters have been guessed.
    print(f"Congratulations! You guessed the word: {word}") #prints win message in another f string.

else: #if loop ends because attempts ran out, print a lose message with the word revealed.
    print(f"Out of guesses! The Word was: {word}")