import Teste
from tkinter import *


class Principal:

    def __init__(self):
        self.principal = Tk()

        self.bt1 = Button(self.principal, width=40, bg="green", command=self.chama_tela)
        self.bt1.place(x="100", y="50")

        self.principal.geometry("800x600")
        self.principal.mainloop()

    def chama_tela(self):
        Teste.Tela()


Principal()
