from tkinter import *
from tkinter import ttk

nome_material = StringVar
qtd_material = 0


class Compra(Frame):

    def __init__(self):
        tela_compra = Tk()
        tela_compra.geometry("600x400")
        tela_compra.title("Comprar Materiais")
        tela_compra.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_compra, width=800, height=500, background='#ccd7ff')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        ####################################################

        produto_label = Label(tela_compra, text="Produto", width=15)
        produto_label.place(x=70, y=60)

        combo_produto = ttk.Combobox(tela_compra,
                                     values=["Aqui vem uma",
                                             "query SQL",
                                             "que mostra",
                                             "as opções"])

        combo_produto.place(x=200, y=60)

        ####################################################

        fornecedor_label = Label(tela_compra, text="Fornecedor", width=15)
        fornecedor_label.place(x=70, y=90)

        combo_fornecedor = ttk.Combobox(tela_compra,
                                        values=["Aqui vem uma",
                                                "query SQL",
                                                "que mostra",
                                                "as opções"])

        combo_fornecedor.place(x=200, y=90)

        ####################################################

        data_label = Label(tela_compra, text="Data da compra", width=15)
        data_label.place(x=70, y=120)

        data_entrada = Entry(tela_compra)
        data_entrada.place(x=200, y=120)

        ####################################################

        quantidade_label = Label(tela_compra, text="Quantidade", width=15)
        quantidade_label.place(x=70, y=150)

        quantidade_entrada = Entry(tela_compra)
        quantidade_entrada.place(x=200, y=150)

        ####################################################

        valor_label = Label(tela_compra, text="Valor da compra", width=15)
        valor_label.place(x=70, y=180)

        valor_entrada = Entry(tela_compra)
        valor_entrada.place(x=200, y=180)

        ####################################################

        status_label = Label(tela_compra, text="Estatus da compra", width=15)
        status_label.place(x=70, y=210)

        status_entrada = Entry(tela_compra)
        status_entrada.place(x=200,y=210)

        ####################################################

        pagamento_label = Label(tela_compra, text="Tipo de Pagamento", width=15)
        pagamento_label.place(x=70, y=240)

        combo_pagamento = ttk.Combobox(tela_compra,
                                       values=["Dinheiro",
                                               "Cartão",
                                               "Cheque"])
        combo_pagamento.place(x=200, y=240)

        ####################################################

        descricao_label = Label(tela_compra, text="Descrição", width=15)
        descricao_label.place(x=70, y=270)

        descricao_entrada = Entry(tela_compra, width=55)
        descricao_entrada.place(x=200,y=270)


        # nome_material_label = Label(tela_compra, text="Material")
        # nome_material_label.place(x=65, y=100)
        # nome_material_entrada = Entry(tela_compra, textvar=nome_material)
        # nome_material_entrada.place(x=125, y=100)
        #
        # qtd_material_label = Label(tela_compra, text="Quantidade")
        # qtd_material_label.place(x=310, y=100)
        # qtd_material_entrada = Entry(tela_compra, textvar=qtd_material)
        # #qtd_material = int(Entry.get(self))
        # qtd_material_entrada.place(x=390, y=100)

        salvar = Button(tela_compra, text="Comprar")  # ,command=Caixa)
        salvar.place(x=150, y=330)
        voltar = Button(tela_compra, text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=330)

        tela_compra.mainloop()


Compra()
