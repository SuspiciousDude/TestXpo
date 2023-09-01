import random
words = ['reddit', 'instagram','whatsapp','snapchat','twitter','facebook','pneumatic', 'psycotic', 'khandelwal']

state1 = '''---------
|   |
|   O
|
|
|
|
|__________
'''

state2 = '''---------
|   |
|   O
|   |
|
|
|
|__________'''

state3 = '''---------
|   |
|   O
|  /|
|
|
|
|__________'''

state4 = '''---------
|   |
|   O
|  /|\\
|
|
|
|__________'''

state5 = '''---------
|   |
|   O
|  /|\\
|   |
|
|
|__________'''

state6 = '''---------
|   |
|   O
|  /|\\
|   |
|   |
|
|__________'''

state7 = '''---------
|   |
|   O
|  /|\\
|   |
|  /|
|
|__________'''

state8 = '''---------
|   |
|   O
|  /|\\
|   |
|  /|\\
|
|__________'''

hangman_states = {1:state1, 2:state2, 3:state3, 4:state4, 5:state5, 6:state6, 7:state7, 8:state8}

def word_to_list(word):
    converted_word_list = []
    for i in word:
        converted_word_list.append(i)
    return converted_word_list

def list_to_dotted(word_list):
    converted_word_list = []
    for i in range(len(word_list)):
        converted_word_list.append('_ ')
    return converted_word_list

def list_to_word(world_list):
    converted_word_str = ''
    for i in world_list:
        converted_word_str+=i
    return converted_word_str

selectedWord = random.choice(words)

actualWordList = word_to_list(selectedWord)

actualDottedList = list_to_dotted(actualWordList)
dotted = list_to_word(actualDottedList)
print(dotted)

guessed_list = []
hang_state = 1
chances = len(selectedWord)+5
while chances:
    print(f'You got {chances} chances')
    alphabetGuess = input('Try guessing the word using any alphabet - ')
    assert len(alphabetGuess) == 1, "Enter a letter, not a word"
    
    if alphabetGuess not in guessed_list:
        guessed_list.append(alphabetGuess)
    else:
        print('You already used this letter. Try another one')
        chances+=1

    if alphabetGuess in actualWordList:
        for i in range(len(selectedWord)):
            if actualWordList[i] == alphabetGuess:
                actualDottedList[i] = alphabetGuess
    else:
        print(hangman_states[hang_state])
        hang_state+=1
        if hang_state == 9:
            print(f"You couldn't guess it. The word was {selectedWord}")
            break
    dotted_query = list_to_word(actualDottedList)
    print(dotted_query)
    chances-=1

    if '_ ' not in actualDottedList:
        print('Good Job, you guessed it right')
        break
else:
    print(f"You couldn't guess it. The word was {selectedWord}")