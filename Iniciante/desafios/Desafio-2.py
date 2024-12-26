from datetime import datetime

data = str(datetime.now()).split(" ")

hora = int(data[1].split(".")[0].split(":")[0])

if hora > 0 and hora < 12:
    print("Bom dia!")
elif hora > 12 and hora < 17:
    print("Boa tarde!")
else:
    print("Boa noite")