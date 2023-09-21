#Veiculo
class Veiculo:
    def __init__(self, modelo, marca, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def imprimir(self):
        print(self.modelo, self.marca, self.ano, self.cor)

    def __str__(self):
        return self.modelo + " " + self.marca + " " + self.ano + " " + self.cor

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, cor, quantidadeDePortas):
        super().__init__(modelo, marca, ano, cor)
        self.quantidadeDePortas = quantidadeDePortas

    def imprimir(self):
        print(self.modelo, self.marca, self.ano, self.cor, self.quantidadeDePortas)

    def __str__(self):
        return self.modelo + " " + self.marca + " " + self.ano + " " + self.cor + " " + self.quantidadeDePortas
    
class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, cor, cilindrada):
        super().__init__(modelo, marca, ano, cor)
        self.cilindrada = cilindrada

    def imprimir(self):
        print(self.modelo, self.marca, self.ano, self.cor, self.cilindrada)

    def __str__(self):
        return self.modelo + " " + self.marca + " " + self.ano + " " + self.cor + " " + self.cilindrada
    
class Forma:
    def calcularArea(self):
        pass
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return 3.14 * (self.raio * self.raio)
    
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado
    
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2
    
    