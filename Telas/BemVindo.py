from tkinter import *


import SelecaoCaixa
import Estoque
import Cadastros
import CompraOuVenda
import FechamentoCaixa
#import Fornecedores

valorInicialCaixa = DoubleVar


class Principal(Frame):
    def __init__(self, **kw):
        #super().__init__(**kw)
        tela_bem_vindo = Tk()
        tela_bem_vindo.title("Bem Vindo")
        tela_bem_vindo.geometry("800x500")
        tela_bem_vindo.configure(background='#D3D3D3')

        canvas = Canvas(tela_bem_vindo, width=800, height=500, background='#DFFFD3')

        r1 = canvas.create_rectangle(50, 100, 250, 400, fill="white")
        r2 = canvas.create_rectangle(300, 100, 700, 220, fill="white")
        r3 = canvas.create_rectangle(300, 250, 700, 400, fill="white")

        # img = PhotoImage(file="logo_provisoria2.jpg")
        # canvas.create_image(0, 0, image=img, anchor=NW)

        canvas.place(x=0, y=0)

        caixa = Button(tela_bem_vindo, text="Caixa", command=self.ChamaCaixa)
        caixa.place(x=90, y=150)

        estoque = Button(tela_bem_vindo, text="Estoque", command=self.ChamaEstoque)
        estoque.place(x=90, y=190)

        pedidos = Button(tela_bem_vindo, text="Compra/Venda", command=self.ChamaCompraVenda)  # ,command=Caixa)
        pedidos.place(x=90, y=230)

        cadastros = Button(tela_bem_vindo, text="Cadastros", command=self.ChamaCadastros)
        cadastros.place(x=90, y=270)

        recebimentos = Button(tela_bem_vindo, text="Listar")  # ,command=Caixa)
        recebimentos.place(x=90, y=310)
        tela_bem_vindo.mainloop()

    def ChamaCaixa(self):
        SelecaoCaixa.SelecaoCaixa()

    def ChamaEstoque(self):
        Estoque.Estoque()

    def ChamaCadastros(self):
        Cadastros.Cadastros()

    def ChamaCompraVenda(self):
        CompraOuVenda.CompraOuVenda()

