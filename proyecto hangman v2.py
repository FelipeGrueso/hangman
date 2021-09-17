import random

print("""H A N G M A N
""")
lista = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(lista)
print( word.replace(word,"-" * len(word)))
intento = 1
nueva_palabra = list(word.replace(word,"-" * len(word)))
while True:
    jugador = input("Input a letter: ")
    if jugador in word:
        i = 0
        while i < len(word):
            if jugador == word[i]:
                nueva_palabra[i] = jugador
                 
            i += 1
            
        print("".join(nueva_palabra))
        if "".join(nueva_palabra) == word:
                print("You guessed the word!\nYou survived!")
                break
        
    else:
        print("That letter doesn't appear in the word")
        print()
        intento += 1
    

    if intento == 9:
        print("Thanks for playing!")
        
        break


print("We'll see how well you did in the next stage")
