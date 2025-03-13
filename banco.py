class Banco:
    def __init__(self):
        self.cuentas = {}

    def crear_cuenta(self, numero_cuenta, saldo_inicial=0):
        if numero_cuenta in self.cuentas:
            raise ValueError("La cuenta ya existe.")
        self.cuentas[numero_cuenta] = saldo_inicial

    def depositar(self, numero_cuenta, monto):
        if numero_cuenta not in self.cuentas:
            raise ValueError("La cuenta no existe.")
        self.cuentas[numero_cuenta] += monto

    def retirar(self, numero_cuenta, monto):
        if numero_cuenta not in self.cuentas:
            raise ValueError("La cuenta no existe.")
        if self.cuentas[numero_cuenta] < monto:
            raise ValueError("Fondos insuficientes.")
        self.cuentas[numero_cuenta] -= monto

    def obtener_saldo(self, numero_cuenta):
        if numero_cuenta not in self.cuentas:
            raise ValueError("La cuenta no existe.")
        return self.cuentas[numero_cuenta]
