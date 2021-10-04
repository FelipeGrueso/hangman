import random
print("""H A N G M A N""")
accion = input("""Type "play" to play the game, "exit" to quit:""")

def hangman():    
    lista = ['python', 'java', 'kotlin', 'javascript']
    alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    letras_usadas = set()
    word = random.choice(lista)
    print( word.replace(word,"-" * len(word)))
    intento = 0
    nueva_palabra = list(word.replace(word,"-" * len(word)))
    while True:
        jugador = input("Input a letter: ")
       
        if len(jugador) >1:
            print("You should input a single letter\n")
            print("".join(nueva_palabra))
        elif jugador =="" or jugador == " ":
            print("You should input a single letter\n")
            print("".join(nueva_palabra))

            
        elif jugador not in alfabeto:
            print("Please enter a lowercase English letter\n")
            print("".join(nueva_palabra))
            
        
        else:
            if jugador in letras_usadas:
                print("You've already guessed this letter\n")   
            
            elif jugador in word:
                i = 0
                while i < len(word):
                    if jugador == word[i]:
                        nueva_palabra[i] = jugador
                    i += 1
                
                        
                if "".join(nueva_palabra) == word:
                        print(f"You guessed the word {word}!\nYou survived!")
                        break
                print()
            
            else:
                print("That letter doesn't appear in the word")
                
                intento += 1
                if intento == 8:
                    print("You lost!")
                    break
                print()

            letras_usadas.add(jugador)

            print("".join(nueva_palabra))
            
    accion = input("""\nType "play" to play the game, "exit" to quit:""")
    if accion == "play":
        hangman()

    
if accion == "play":
    hangman()
