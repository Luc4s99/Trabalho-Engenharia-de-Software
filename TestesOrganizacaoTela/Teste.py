from tkinter import *


class Tela:

    def __init__(self):
        self.principal = Tk()
        self.bt1 = Button()

        self.bt1 = Button(self.principal, width=40, bg="blue", command=self.muda_cor_botao)
        self.bt1.place(x="100", y="50")

        self.principal.geometry("800x600+200+200")
        self.principal.mainloop()

    def muda_cor_botao(self):
        self.bt1["bg"] = "red"

# telinha = Tela()
