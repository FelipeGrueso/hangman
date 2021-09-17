import random

print("""H A N G M A N
The game will be available soon.""")
lista = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(lista)
print("Guess the word: "+ word[0:3] + word[3:].replace(word[3:],"-" * len(word[3:])))
jugador = input()

if jugador == word:
    print("You survived!")
else:
    print("You lost!")
