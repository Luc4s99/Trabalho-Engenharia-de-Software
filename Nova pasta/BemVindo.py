from tkinter import *
import AberturaCaixa

valorInicialCaixa = DoubleVar


class Principal(Frame):
    def __init__(self, **kw):
        top = Tk()
        top.title("Bem Vindo")
        top.geometry("800x500")
        top.configure(background='#D3D3D3')

        canvas = Canvas(top, width=800, height=500, background='#DFFFD3')

        r1 = canvas.create_rectangle(50, 100, 250, 400, fill="white")
        r2 = canvas.create_rectangle(300, 100, 700, 220, fill="white")
        r3 = canvas.create_rectangle(300, 250, 700, 400, fill="white")
        canvas.place(x=0, y=0)

        caixa = Button(text="Caixa", command=self.ChamaCaixa)
        caixa.place(x=90, y=150)

        estoque = Button(text="Estoque")  # ,command=Caixa)
        estoque.place(x=90, y=190)

        pedidos = Button(text="Pedidos")  # ,command=Caixa)
        pedidos.place(x=90, y=230)

        cadastros = Button(text="Cadastros")  # ,command=Caixa)
        cadastros.place(x=90, y=270)

        recebimentos = Button(text="Recebimentos")  # ,command=Caixa)
        recebimentos.place(x=90, y=310)
        top.mainloop()

    def ChamaCaixa(self):
        AberturaCaixa.AberturaCaixa()


Principal()

