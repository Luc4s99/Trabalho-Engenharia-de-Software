from tkinter import *
import Telas.Compra
import Telas.InicioVenda


class CompraOuVenda(Frame):
    def __init__(self):
        self.tela_compra_ou_venda = Tk()
        self.tela_compra_ou_venda.geometry("600x400")
        self.tela_compra_ou_venda.title("Compra ou Venda")
        self.tela_compra_ou_venda.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_compra_ou_venda, width=800, height=500, background='#ccd7ff')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        bt1 = Button(self.tela_compra_ou_venda, text="Comprar Materiais", width=15, command=self.ChamaCompra)
        bt1.place(x=120, y=150)
        bt2 = Button(self.tela_compra_ou_venda, text="Vender Materiais", width=15, command=self.ChamaVenda)
        bt2.place(x=360, y=150)

        salvar = Button(self.tela_compra_ou_venda, text="Salvar")  # ,command=Caixa)
        salvar.place(x=150, y=330)
        voltar = Button(self.tela_compra_ou_venda, text="Voltar", command=self.voltar)  # ,command=Caixa)
        voltar.place(x=400, y=330)

        self.tela_compra_ou_venda.mainloop()

    def voltar(self):
        self.tela_compra_ou_venda.destroy()

    def ChamaCompra(self):
        Telas.Compra.Compra()

    def ChamaVenda(self):
        Telas.InicioVenda.Venda()
