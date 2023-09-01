import random

numberGenerate = random.randint(1000,9999)
numberGenerateList = [int(digit) for digit in str(numberGenerate)]

def bulls(generatedNumberList, guessedNumberList):
    bulls_count = 0
    for i in range(len(generatedNumberList)):
        if generatedNumberList[i] == guessedNumberList[i]:
            bulls_count+=1
    print(f'Bulls - {bulls_count}')

def cows(generatedNumberList, guessedNumberList):
    cows_count = 0
    for i in range(len(generatedNumberList)):
        for j in guessedNumberList:
            if j in generatedNumberList and generatedNumberList[i] != guessedNumberList[i]:
                cows_count+=1
    print(f'Cows - {cows_count//3}')

while True:
    chances = 0
    numberGuess = int(input('Try guesssing the number - '))
    numberGuessList = [int(digit) for digit in str(numberGuess)]
    bulls(numberGenerateList, numberGuessList)
    cows(numberGenerateList, numberGuessList)
    if numberGuess == numberGenerate:
        print(f'You guessed it right. The number was {numberGenerate}')
        print(f'It took you {chances} chances')
        break
    else:
        print('Try again')
    chances += 1