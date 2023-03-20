class animal:
    def __init__(self, nombre, edad, reproduccion, tipo, patas, cola, id):
        self.nombre = nombre
        self.edad = edad
        self.reproduccion = reproduccion
        self.tipo = tipo
        self.patas = patas
        self.cola = cola
        self.id = id
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad

    def getRepreoduccion(self):
        return self.Reproduccion
    def setReproduccion(self, reproduccion):
        self.reproduccion = reproduccion

    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo

    def getPatas(self):
        return self.Patas
    def setPatas(self, patas):
        self.patas=patas

    def getCola(self):
        return self.cola
    def setCola(self, cola):
        self.cola = cola

    def salutacio(self):
        print("El nombre es: " + self.nombre)
        print("Tengo " + self.edad + " años")
        print("Mi reproducción es: " +self.reproduccion)
        print("Mi tipo es: " + self.tipo)
        print("Tengo " + self.patas + " patas")
        print("Tengo cola: " + self.cola)

    def to_dict(self):
        return{
            "nombre":self.nombre,
            "edad":self.edad,
            "reproduccion":self.reproduccion,
            "tipo":self.tipo,
            "patas":self.patas,
            "cola":self.cola,
        }