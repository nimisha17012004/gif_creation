import random
word_bank=['hi','world','coffee','river','sea']
word=random.choice(word_bank)
guessword=['_'] * len(word)
attempts=10

while attempts > 0:
    print('\n Current word: ' + ' '.join(guessword))

    guess = input('Guess a letter: ')
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessword[i] = guess
        print("Great Guess!")
    else:
        attempts-=1
        print("Wrong Guess! Attempts left: " + str(attempts))
    
    if '_' not in guessword:
        print('\nCongratulations!! You guessed the word: ' + word)
    break
else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
    