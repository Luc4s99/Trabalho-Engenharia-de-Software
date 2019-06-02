from tkinter import *
from tkinter import ttk
import ContinuaVenda


class Venda(Frame):

    def __init__(self):
        self.tela_venda = Tk()
        self.tela_venda.geometry("600x400")
        self.tela_venda.title("Operação de Venda")
        self.tela_venda.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_venda, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_produto_label = Label(self.tela_venda, text="Produto:")
        nome_produto_label.place(x=70, y=100)
        combo_produtos = ttk.Combobox(self.tela_venda,
                                      values=[
                                          "Aqui vem uma",
                                          "query SQL",
                                          "que mostra",
                                          "as opções"])
        combo_produtos.place(x=130, y=100)

        nome_rua_label = Label(self.tela_venda, text="Unidade:")
        nome_rua_label.place(x=70, y=160)
        combo_unidade = ttk.Combobox(self.tela_venda,
                                     values=[
                                         "Kg",
                                         "Caminhão"])
        combo_unidade.place(x=135, y=160)

        continuar = Button(self.tela_venda, text="Continuar", command=self.continua_venda)
        continuar.place(x=150, y=330)
        voltar = Button(self.tela_venda, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=330)

        self.tela_venda.mainloop()

    def continua_venda(self):
        ContinuaVenda.Venda()

    def voltar(self):
        self.tela_venda.destroy()

