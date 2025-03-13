from banco import Banco

class ControladorBanco:
    def __init__(self):
        self.banco = Banco()

    def crear_cuenta(self, numero_cuenta):
        self.banco.crear_cuenta(numero_cuenta)

    def depositar(self, numero_cuenta, monto):
        self.banco.depositar(numero_cuenta, monto)

    def retirar(self, numero_cuenta, monto):
        self.banco.retirar(numero_cuenta, monto)

    def consultar_saldo(self, numero_cuenta):
        return self.banco.obtener_saldo(numero_cuenta)
