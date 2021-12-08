class ContaCorrente:

    def __init__(self, valor):
        self.valor = valor

    def saldo(self):
        print(f'Seu saldo é: {self.valor}')

    def mudar_valor(self, novo_valor):
        self.valor = novo_valor
        print("Valor alterado")