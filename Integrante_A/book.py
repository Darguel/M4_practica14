class book:
    def __init__(self, autor, volumen, numHojas, tapa, genero, publicacion):
        self.autor = autor
        self.volumen = volumen
        self.numHojas = numHojas
        self.tapa = tapa
        self.genero = genero
        self.publicacion = publicacion

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getvolumen(self):
        return self.volumen

    def setvolumen(self, volumen):
        self.volumen = volumen

    def getNumHojas(self):
        return self.numHojas

    def setNumHojas(self, numHojas):
        self.numHojas = numHojas

    def getTapa(self):
        return self.tapa

    def setTapa(self, tapa):
        self.tapa = tapa

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getPublicacion(self):
        return self.publicacion

    def setPublicacion(self, publicacion):
        self.publicacion = publicacion

    def info(self):
        print("Los datos del book son: \n autor" + self.autor)
        print("Volumen: " + self.volumen)
        print("Numero de hojas : " + self.numHojas)
        print("Tapa: " + self.tapa)
        print("Jenero: " + self.genero)
        print("Año de publicacion: " + self.publicacion)

    def to_dict(self):
        return {
            "autor":self.autor,
            "volumen":self.volumen,
            "numHoja":self.numHojas,
            "tapa": self.tapa,
            "genero": self.genero,
            "publicacion": self.publicacion,
        }

    

