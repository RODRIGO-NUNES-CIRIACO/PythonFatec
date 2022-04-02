import json


arquivo = open("db.csv", "a")


json.dump("elefantebranco", arquivo)


arquivo.close()