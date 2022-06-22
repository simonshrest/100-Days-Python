#Hangman Game
import random
import hangman_art
import hangman_words
import clear

print(hangman_art.logo)

#List of words to play from

#Randomly chosen word from the list
chosen_word = random.choice(hangman_words.word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Creating an empty list to store same numbers of dashes '_' as letters in the chosen word.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = list()
for letters in chosen_word:
  display += "_"
print(f"{' '.join(display)}")

#Boolean variable to check the end of game
end_of_game = False
#Assign 6 Lives to player wehn the game starts
lives = 6
guess_list = []

#Loop through each position in the chosen_word;
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
while not end_of_game:
  guess = input("\nGuess a letter: ").lower()
  #Clear the screen after guess.
  clear()
#Insert guessed letters in a list guess_list and check for reoccurrence. 
  if guess in guess_list:
      print("You have already guessed this letter.")
      lives += 1
  else:
      guess_list += guess
#Print the guessed letter in the correct position and every other letter replace with "_".
  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = guess
    
  print(f"{' '.join(display)}")
  #If guessed letter is not present in the chosen word then decrease player's live by 1
  if guess not in chosen_word:
    lives -=1
    print(f"You have {lives} lives left.")
    #If players guesses wrong more than 6 times, they loose.
    if lives == 0:
      end_of_game = True
      print("You Lost!")
  
  #If player guessed all the letters, player wins i.e all '_' replaced with correct letters
  if "_" not in display:
    end_of_game = True
    print("You win.")
  #Print different stages of hangman throughout the game. If player looses a life, it prints stages[lives]
  print(hangman_art.stages[lives])
  