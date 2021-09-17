import random

print("""H A N G M A N\n""")
lista = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(lista)
print( word.replace(word,"-" * len(word)))
intento = 0
nueva_palabra = list(word.replace(word,"-" * len(word)))
while True:
    jugador = input("Input a letter: ")
    
    if jugador in word:
        if jugador in nueva_palabra:
            print("No improvements")
            intento += 1
            if intento ==8:
                print("You lost!")
                break
            print()
            
            
        else:
            i = 0
            while i < len(word):
                if jugador == word[i]:
                    nueva_palabra[i] = jugador
                i += 1
            print()
                
            
            if "".join(nueva_palabra) == word:
                    print("".join(nueva_palabra))
                    print("You guessed the word!\nYou survived!")
                    break

    else:
        print("That letter doesn't appear in the word")
        
        intento += 1
        if intento == 8:
            print("You lost!")
            break
        print()

    

    
    print("".join(nueva_palabra))

