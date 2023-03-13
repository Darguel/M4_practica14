class gato:
    def __init__(self, nombre, edad, peso, raza):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.raza = raza

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getPeso(self):
        return self.peso
    def setPeso(self, peso):
        self.peso = peso

    def getRaza(self):
        return self.raza
    def setRaza(self, raza):
        self.raza = raza

    def salutacio(self):
        print("El nombre es: " + self.nombre)
        print("Tengo " + self.edad + " años")
        print("Mi peso es: " +self.peso)
        print("Mi raza es: " + self.raza)

    def to_dict(self):
        return{
            "nombre":self.nombre,
            "edad":self.edad,
            "peso":self.peso,
            "raza":self.raza
        }