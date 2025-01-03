
frase = "O Python e uma otima linguagem de programação!"

letter = ""
letter_count = 0
for i in range(0,len(frase)):
    letter_current = frase[i]
    letter_current_count = frase.count(letter_current)
    
    if letter_current == " ":
        continue
    
    
    if letter_current_count > letter_count:
        letter_count = letter_current_count
        letter = letter_current
        

print(f'A letra mais presente na frase e "{letter}" e apareceu {letter_count} vezes')