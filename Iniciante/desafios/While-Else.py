"""
While Else 
"""
i = 0
while i < 10:
    print(i)
    if i == 9:
        break
    
    i += 1
else:
    print("Else executado se o while for false")