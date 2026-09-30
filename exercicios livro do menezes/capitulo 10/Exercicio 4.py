class Televisão:

    def __init__(self,canal_inicial, min=2, max=14):
        self.ligada = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if(self.canal-1>=self.cmin):
            self.canal-=1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if(self.canal+1<=self.cmax):
            self.canal+=1
        else:
            self.canal = self.cmax

tv = Televisão(2,2,14)
while True:
    print("Aperte 0 para sair\nAperte 1 para ligar ou desligar a tv\nAperte 2 para subir o canal\nAperte 3 para descer o canal")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Você saiu!\n")
        break

    elif opcao == "1":
        if tv.ligada == True:
            tv.ligada = False
            print("TV desligada!\n")
        else:
            tv.ligada = True
            print("TV ligada!\n")

    elif opcao == "2":

        if tv.canal < tv.cmax:
            tv.muda_canal_para_cima()
            print("Você está no canal %d\n" % tv.canal)
        else:
            tv.canal = tv.cmin
            print("Você no canal %d\n" % tv.canal)

    elif opcao == "3":

        if tv.canal > tv.cmin:
            tv.muda_canal_para_baixo()
            print("Você está no canal %d\n" % tv.canal)
        else:
            tv.canal = tv.cmax
            print("Você no canal %d\n" % tv.canal)
        