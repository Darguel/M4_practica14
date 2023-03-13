class car:
    def __int__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año


    def getMarca(self):
        return self.maraca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getAño(self):
        return self.año

    def setAño(self, año):
        self.año = año


    def info(self):
        print("Los datos del car son: \n marca" + self.marca)
        print("Modelo: " + self.modelo)
        print("Color : " + self.color)
        print("año: " + self.año)

    def to_dict(self):
        return {
            "marca":self.marca,
            "modelo":self.modelo,
            "color":self.color,
            "año":self.año,
        }