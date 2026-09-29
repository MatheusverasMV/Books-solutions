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
    print("Pressione 1 para ligar a televisão")
    print("Pressione 2 para desligar a televisão")
    print("Pressione 3 para mudar o canal para cima")
    print("Pressione 4 para mudar o canal para baixo")
    opcao = input("Escolha uma opção: ")
    
    tv = televisao()
    if opcao == "1":
        tv.ligada = True
        print("Tv ligada")
        if opcao == "1" and tv.ligada:
            print("A televisão já está ligada\n")
    elif opcao == "2":
        if tv.ligada == True:
            print("Desligando a televisão...\n")
            tv.ligada = False
    elif opcao == "2" and tv.ligada == False:
        print("A televisão já está desligada\n")
    elif opcao == "3":
        if tv.ligada == True:
            tv.muda_canal_pra_cima()
            print(f"Canal atual: {tv.canal}")
        if tv.ligada == False:
            print("A televisão está desligada\n")
    elif opcao == "4":
        if tv.ligada == True:
            tv.muda_canal_pra_baixo()
            print(f"Canal atual: {tv.canal}")
        if tv.ligada == False:
            print("A televisão está desligada\n")
    elif opcao == "67":
        print("Six SEVENNNNNN!\n")