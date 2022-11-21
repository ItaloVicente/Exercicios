from cliente import Cliente
class Conta:
    def __init__(self,cliente,saldo,limite):
        self.cliente=cliente
        self.saldo=saldo
        self.limite=limite
    def sacar(self, quantidade):
        if((self.saldo-quantidade)>self.limite):
            self.saldo-=quantidade
        else:
            print("Saldo e limite insuficientes")
    def depositar(self, quantidade):
        self.saldo+=quantidade
    def consultarSaldo(self):
        return self.saldo
