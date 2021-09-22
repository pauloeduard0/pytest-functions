def enviar(destinatario, saldo, qtd):
    msg = f'{destinatario}, saldo = {round(saldo - qtd, 8)}'
    print(msg)
    return msg


class Wallet:
    def __init__(self, destinatarios, saldo):
        self.saldo = saldo
        self.destinatarios = destinatarios

    def adicionar_destinatario(self, destinatario):
        self.destinatarios.append(destinatario)

    def enviar_btc(self, qtd):
        var = self.saldo
        for destinatario in self.destinatarios:
            x = enviar(destinatario, var, qtd)
            return x
