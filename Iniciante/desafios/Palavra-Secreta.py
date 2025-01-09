import requests
print("Jogo da palavra secreta")
print(30 * "=")
res = requests.get("https://api.dicionario-aberto.net/random").json()
secret_word = res["word"].lower()
letters = ""



while True:
    letter = input("Digite uma letra: ").lower()
    
    if len(letter) > 1:
        print("Digite apenas uma letra")
        continue
    
    if letter in secret_word:
        letters += letter
    
    for letter_secret in secret_word:

        if letter_secret in letters:
            print(letter_secret)
        else:
            print("*")

        
            


