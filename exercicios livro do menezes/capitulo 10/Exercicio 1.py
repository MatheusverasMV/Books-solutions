class televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.tamanho = 32
        self.marca = "LG"

tv = televisao()
tv.ligada = True
tv.tamanho = 27
tv.marca = "samsung"
tv_sala = televisao()
tv_sala.ligada = True
tv_sala.tamanho = 42
tv_sala.marca = "Philco"

print("O TV da sala é da marca %s, tem %d polegas" % (tv_sala.marca, tv_sala.tamanho))
print("A tv do quarto é da marca %s, tem %d polegas" % (tv.marca, tv.tamanho))