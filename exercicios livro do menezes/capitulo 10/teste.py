class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número

    def resumo(self):
        print("CC Número: %s Saldo: %10.2f" % (self.número, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor


Cliente_um = Cliente("João da Silva", "777-1234")
Conta_um = Conta([Cliente_um], "12345", 1000.0)