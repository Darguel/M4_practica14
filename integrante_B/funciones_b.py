import requests

def getAnimal():
    response = requests.get('http://localhost:3000/animal')
    return print(response.json())

def getCat():
    response2 = requests.get('http://localhost:3000/cat')
    return print(response2.json())

def postAnimal():
    newLines = {
        'nombre': "bigotitos",'edad': "3",'reproduccion': "mamifero",'tipo': "felino",'patas': "4",'cola': "si",'id': "6"
    }
    r = requests.post('http://localhost:3000/animal', data=newLines)

    return print(r.text)


def postCat():
    newLines = {
        'nombre': "bigototes",'edad': "2",'peso': "24",'raza': "mestizo",'id': "6"
    }
    r2 = requests.post('http://localhost:3000/animal', data=newLines)

    return print(r2.text)


