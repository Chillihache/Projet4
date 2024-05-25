import json
import os.path
class Object:
    attribut1 = "eorhgioh"
    attribut2 = "oghiozeghengio"


objet_test = Object()
with open("../data/data_test", "w") as file:
    json.dump([objet_test], file, indent=4)
print(objet_test.attribut1)



