class televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.tamanho = 32
        self.marca = "LG"

    def ligar(self):
        self.ligada = True

    def muda_canal_pra_cima(self):
        if self.ligada:
            self.canal +=1
        else:
            return "A televisão está desligada"

    def muda_canal_pra_baixo(self):
        if self.ligada:
            self.canal -=1
        else:
            return "A televisão está desligada"

while True:
    tv = televisao()
    