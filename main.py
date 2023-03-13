import json

from integrante_B.animal import animal
from integrante_B.cat import gato

animals = [
    animal("gato", "2", "mamifero", "felino", "4", "si"),
    animal("perro", "3", "mamifero", "canino", "4", "si"),
    animal("lobo", "1", "mamifero", "canino", "4", "si"),
    animal("tigre", "5", "mamifero", "felino", "4", "si"),
    animal("leon", "4", "mamifero", "felino", "4", "si")
]

animal_list = [animal.to_dict() for animal in animals]

gatos = [
    gato("michi","2","23","Abisinio"),
    gato("rocky","4","30","Asiático"),
    gato("chispas","5","35","Balinés"),
    gato("bigotes","4","29","Bengalí"),
    gato("zarpitas","1","20","Azul ruso")
]

gato_list = [gato.to_dict() for gato in gatos]


data = {"animals":animal_list, "gatos":gato_list}

with open("jsonAPI/animals.json",'w') as file:
    json.dump(data, file)