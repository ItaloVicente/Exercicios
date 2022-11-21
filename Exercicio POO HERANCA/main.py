from cliente import Cliente
from conta import Conta

verificador=False
L=[]
Contas=[]
while verificador!=True:
    print("O que voce deseja fazer?")
    print("1.Criar cliente")
    print("2.Criar conta")
    print("3.Sacar")
    print("4.Depositar")
    print("5.Verificar Saldo")
    print("6.Encerrar o programa")
    escolha = int(input())
    if(escolha==1):
        nome = input("Insira o nome do cliente")
        cpf = input("Insira o CPF do cliente")
        idade = input("Insira a idade do cliente")
        cliente = Cliente(nome,cpf,idade)
        L.append(cliente)
    if (escolha==2):
        nome = input("Insira o nome do cliente")
        for i in L:
            if (i.nome==nome):
                cliente = i
                saldo = float(input("Insira o saldo"))
                limite = float(input(("Insira o limite (negativo)")))
                conta = Conta(cliente, saldo, limite)
                Contas.append(conta)
            else:
                print("Cliente nao encontrado")
    if(escolha==3):
        nome = input("Insira o nome do dono da conta")
        for i in Contas:
            if(i.cliente.nome==nome):
                conta = i
                quantidade = float(input("Insira a quantidade"))
                conta.sacar(quantidade)
            else:
                print("Conta inexistente")
    if (escolha==4):
        nome = input("Insira o nome do dono da conta")
        for i in Contas:
            if (i.cliente.nome == nome):
                conta = i
                quantidade = float(input("Insira a quantidade"))
                conta.depositar(quantidade)
            else:
                print("Conta inexistente")
    if (escolha==5):
        nome = input("Insira o nome do dono da conta")
        for i in Contas:
            if (i.cliente.nome == nome):
                conta = i
                print(conta.consultarSaldo())
            else:
                print("Conta inexistente")
    if (escolha == 6):
        verificador=True
