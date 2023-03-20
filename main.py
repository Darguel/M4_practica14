import json

from integrante_B.animal import animal
from integrante_B.cat import gato
from Integrante_A.book import book
from Integrante_A.car import car
books = [
    book("Jose Luis", "2", "150", "dura", "accion", "2001"),
    book("Pepito Rodriges", "4", "200", "blanda", "ficcion", "2003"),
    book("Pepita Perez", "2", "300", "blanda", "comedia", "1999"),
    book("David Rodriguez", "1", "298", "dura", "comedia", "2008"),
    book("Fernado Aguilar", "5", "240", "blanda", "terror", "2001")
]
book_list = [book.to_dict() for book in books]

cars = [
    car("BMW", "93747", "negro", "2009"),
    car("Ferrari", "45365", "fojo", "2005"),
    car("Porch", "5672", "verde", "2001"),
    car("Tollota", "9753", "amarillo", "2000"),
    car("Zuzuki", "88445", "lila", "2016")
]
car_list = [car.to_dict() for car in cars]

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
data2 = {"books":book_list, "cars":car_list}

with open("jsonAPI/integrante_B.json",'w') as file:
    json.dump(data, file)
with open("jsonAPI/integrante_A.json",'w') as file:
    json.dump(data2, file)