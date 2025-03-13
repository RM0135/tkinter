from tkinter import Tk
from views.interfaz import InterfazBancaria
from controllers.controlador import ControladorBanco

if __name__ == "__main__":
    controlador = ControladorBanco()
    root = Tk()
    app = InterfazBancaria(root, controlador)
    root.mainloop()
