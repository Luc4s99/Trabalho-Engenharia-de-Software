from tkinter import *
from tkinter import ttk


class Venda:
    def __init__(self):
        self.tela_venda2 = Tk()
        self.tela_venda2.geometry("600x400")
        self.tela_venda2.title("Operação de Venda")
        self.tela_venda2.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_venda2, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_produto_label = Label(self.tela_venda2, text="Produto:")
        nome_produto_label.place(x=70, y=100)
        combo_produtos = ttk.Combobox(self.tela_venda2,
                                      values=[
                                          "Aqui vem uma",
                                          "query SQL",
                                          "que mostra",
                                          "as opções"])
        combo_produtos.place(x=130, y=100)

        nome_rua_label = Label(self.tela_venda2, text="Unidade:")
        nome_rua_label.place(x=70, y=160)
        combo_unidade = ttk.Combobox(self.tela_venda2,
                                     values=[
                                         "Kg",
                                         "Caminhão"])
        combo_unidade.place(x=135, y=160)

        # Depois verificar aqui
        if combo_unidade.get() == 'Kg':
            unidade_label = Label(self.tela_venda2, text="Quantidade(Kg):")
            unidade_label.place(x=70, y=200)
            unidade_entrada = Entry(self.tela_venda2, width=43)
            unidade_entrada.place(x=170, y=220)

        salvar = Button(self.tela_venda2, text="Olá")
        salvar.place(x=150, y=330)
        voltar = Button(self.tela_venda2, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=330)

        self.tela_venda2.mainloop()

    def voltar(self):
        self.tela_venda2.destroy()
