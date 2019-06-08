from tkinter import *
from tkinter import ttk


class Venda:
    def __init__(self, unidade):
        self.tela_venda2 = Tk()
        self.tela_venda2.geometry("600x400")
        self.tela_venda2.title("Operação de Venda")
        self.tela_venda2.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_venda2, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_rua_label = Label(self.tela_venda2, text="Tipo produto:")
        nome_rua_label.place(x=70, y=100)
        combo_unidade = ttk.Combobox(self.tela_venda2,
                                     values=[
                                         "Query",
                                         "Com os tipos"])
        combo_unidade.place(x=160, y=100)

        if unidade == 'Caminhão':
            unidade_label = Label(self.tela_venda2, text="Nº caminhões:")
            unidade_label.place(x=70, y=140)
            unidade_entrada = Entry(self.tela_venda2)
            unidade_entrada.place(x=170, y=140)
        else:
            unidade_label = Label(self.tela_venda2, text="Quantidade(Kg):")
            unidade_label.place(x=70, y=140)
            unidade_entrada = Entry(self.tela_venda2)
            unidade_entrada.place(x=180, y=140)

        total_label = Label(self.tela_venda2, text="Total(R$):")
        total_label.place(x=70, y=190)
        total_saida = Entry(self.tela_venda2)
        total_saida.place(x=136, y=190)

        salvar = Button(self.tela_venda2, text="Finalizar")
        salvar.place(x=150, y=330)
        voltar = Button(self.tela_venda2, text="Voltar", command=self.voltar)
        voltar.place(x=400, y=330)

        self.tela_venda2.mainloop()

    def voltar(self):
        self.tela_venda2.destroy()
