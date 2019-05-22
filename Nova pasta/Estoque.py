from tkinter import *

valor = DoubleVar
nome_produto_bd = StringVar
codigo_produto_bd = int
total_estoque_produto_bd = float
estoque_minimo_produto_bd = float
preco_compra_produto_bd = "12"
preco_venda_produto_bd = float

class Estoque(Frame):

    def __init__(self):
        tela_estoque = Tk()
        tela_estoque.title("Estoque")
        tela_estoque.geometry("600x450")
        tela_estoque.configure(background='#D3D3D3')

        canvas = Canvas(tela_estoque, width=800, height=500, background='#DFFFD3')

        r1 = canvas.create_rectangle(50, 50, 550, 400, fill="white")
        canvas.place(x=0, y=0)

        nome_produto_label = Label(tela_estoque, text="Nome do Produto: ")
        nome_produto_label.place(x=70, y=100)

        nome_produto = Label(tela_estoque, text=nome_produto_bd)
        nome_produto.place(x=220, y=100)


        codigo_produto_label = Label(tela_estoque, text="Codigo do Produto: ")
        codigo_produto_label.place(x=320, y=100)

        codigo_produto = Label(tela_estoque, text=codigo_produto_bd)
        codigo_produto.place(x=430, y=100)


        total_estoque_produto_label = Label(tela_estoque, text="Total em Estoque: ")
        total_estoque_produto_label.place(x=70, y=150)

        total_estoque_produto = Label(tela_estoque, text=total_estoque_produto_bd)
        total_estoque_produto.place(x=220, y=150)


        estoque_minimo_produto_label = Label(tela_estoque, text="Estoque Minimo: ")
        estoque_minimo_produto_label.place(x=70, y=200)

        estoque_minimo_produto = Label(tela_estoque, text=estoque_minimo_produto_bd)
        estoque_minimo_produto.place(x=220, y=200)


        proco_compra_produto_label = Label(tela_estoque, text="Preço de Compra R$: ")
        proco_compra_produto_label.place(x=70, y=250)

        proco_compra_produto_label = Label(tela_estoque, text=preco_compra_produto_bd)
        proco_compra_produto_label.place(x=220, y=250)


        proco_venda_produto_label = Label(tela_estoque, text="Preço de Venda R$: ")
        proco_venda_produto_label.place(x=70, y=300)

        proco_venda_produto_label = Label(tela_estoque, text=preco_venda_produto_bd)
        proco_venda_produto_label.place(x=220, y=300)

        salvar_tela_estoque = Button(tela_estoque, text="SALVAR")  # ,command=Caixa)
        salvar_tela_estoque.place(x=150, y=350)

        fechar_tela_estoque = Button(tela_estoque, text="FECHAR")  # ,command=Caixa)
        fechar_tela_estoque.place(x=400, y=350)

        tela_estoque.mainloop()

