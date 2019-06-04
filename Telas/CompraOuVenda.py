from tkinter import *


class CompraOuVenda(Frame):
    def __init__(self):
        tela_compra_ou_venda = Tk()
        tela_compra_ou_venda.geometry("600x400")
        tela_compra_ou_venda.title("Pedido")
        tela_compra_ou_venda.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_compra_ou_venda, width=800, height=500, background='#ccd7ff')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        bt1 = Button(tela_compra_ou_venda, text="Comprar Materiais", width=15)
        bt1.place(x=120, y=150)
        bt2 = Button(tela_compra_ou_venda, text="Vender Materiais", width=15)
        bt2.place(x=360, y=150)

        salvar = Button(tela_compra_ou_venda, text="Salvar")  # ,command=Caixa)
        salvar.place(x=150, y=330)
        voltar = Button(tela_compra_ou_venda, text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=330)

        tela_compra_ou_venda.mainloop()


CompraOuVenda()