import tkinter as tk
from tkinter import messagebox

class InterfazBancaria:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Banco")

        # Widgets
        tk.Label(root, text="Número de cuenta:").grid(row=0, column=0)
        self.entrada_cuenta = tk.Entry(root)
        self.entrada_cuenta.grid(row=0, column=1)

        tk.Label(root, text="Monto:").grid(row=1, column=0)
        self.entrada_monto = tk.Entry(root)
        self.entrada_monto.grid(row=1, column=1)

        tk.Button(root, text="Crear cuenta", command=self.crear_cuenta).grid(row=2, column=0)
        tk.Button(root, text="Depositar", command=self.depositar).grid(row=2, column=1)
        tk.Button(root, text="Retirar", command=self.retirar).grid(row=3, column=0)
        tk.Button(root, text="Consultar saldo", command=self.consultar_saldo).grid(row=3, column=1)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

    def crear_cuenta(self):
        try:
            cuenta = self.entrada_cuenta.get()
            self.controlador.crear_cuenta(cuenta)
            self.mostrar_mensaje("Cuenta creada exitosamente.")
        except Exception as e:
            self.mostrar_mensaje(str(e))

    def depositar(self):
        try:
            cuenta = self.entrada_cuenta.get()
            monto = float(self.entrada_monto.get())
            self.controlador.depositar(cuenta, monto)
            self.mostrar_mensaje("Depósito realizado exitosamente.")
        except Exception as e:
            self.mostrar_mensaje(str(e))

    def retirar(self):
        try:
            cuenta = self.entrada_cuenta.get()
            monto = float(self.entrada_monto.get())
            self.controlador.retirar(cuenta, monto)
            self.mostrar_mensaje("Retiro realizado exitosamente.")
        except Exception as e:
            self.mostrar_mensaje(str(e))

    def consultar_saldo(self):
        try:
            cuenta = self.entrada_cuenta.get()
            saldo = self.controlador.consultar_saldo(cuenta)
            self.mostrar_mensaje(f"Saldo disponible: {saldo}")
        except Exception as e:
            self.mostrar_mensaje(str(e))
