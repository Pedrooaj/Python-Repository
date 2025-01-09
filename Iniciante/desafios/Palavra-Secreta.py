import requests
import os
print("Jogo da palavra secreta")
print(30 * "=")
res = requests.get("https://api.dicionario-aberto.net/random").json()
secret_word = res["word"].lower()
letters = ""
attemps_number = 0



while True:
    letter = input("Digite uma letra: ").lower()
    attemps_number += 1
    if len(letter) > 1:
        print("Digite apenas uma letra")
        continue
    
    if letter in secret_word:
        letters += letter
    
    current_word = ""
    
    for letter_secret in secret_word:

        if letter_secret in letters:
            current_word += letter_secret
        else:
             current_word += "*"
    
    print("Palavra formada: ", current_word)
    
    if current_word == secret_word:
        print(f"Você ganhou. A palavra secreta era: {secret_word}")
        res = requests.get("https://api.dicionario-aberto.net/random").json()
        secret_word = res["word"].lower()
        letters = ""
        attemps_number = 0
        os.system("cls")
        
    

        
            


