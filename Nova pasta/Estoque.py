from tkinter import *

valor = DoubleVar
nome_produto_bd = StringVar
codigo_produto_bd = int
total_estoque_produto_bd = float
estoque_minimo_produto_bd = float
preco_compra_produto_bd = "12"
preco_venda_produto_bd = float
class principal(Frame):

    def __init__(self):
        top = Tk()
        top.title("Estoque")
        top.geometry("600x450")
        top.configure(background='#D3D3D3')

        canvas = Canvas(top, width=800, height=500, background='#DFFFD3')

        r1 = canvas.create_rectangle(50, 50, 550, 400, fill="white")
        canvas.place(x=0, y=0)

        nome_produto_label = Label(text="Nome do Produto: ")
        nome_produto_label.place(x=70, y=100)

        nome_produto = Label(text=nome_produto_bd)
        nome_produto.place(x=220, y=100)


        codigo_produto_label = Label(text="Codigo do Produto: ")
        codigo_produto_label.place(x=320, y=100)

        codigo_produto = Label(text=codigo_produto_bd)
        codigo_produto.place(x=430, y=100)


        total_estoque_produto_label = Label(text="Total em Estoque: ")
        total_estoque_produto_label.place(x=70, y=150)

        total_estoque_produto = Label(text=total_estoque_produto_bd)
        total_estoque_produto.place(x=220, y=150)


        estoque_minimo_produto_label = Label(text="Estoque Minimo: ")
        estoque_minimo_produto_label.place(x=70, y=200)

        estoque_minimo_produto = Label(text=estoque_minimo_produto_bd)
        estoque_minimo_produto.place(x=220, y=200)


        proco_compra_produto_label = Label(text="Preço de Compra R$: ")
        proco_compra_produto_label.place(x=70, y=250)

        proco_compra_produto_label = Label(text=preco_compra_produto_bd)
        proco_compra_produto_label.place(x=220, y=250)


        proco_venda_produto_label = Label(text="Preço de Venda R$: ")
        proco_venda_produto_label.place(x=70, y=300)

        proco_venda_produto_label = Label(text=preco_venda_produto_bd)
        proco_venda_produto_label.place(x=220, y=300)

        salvar_tela_estoque = Button(text="SALVAR")  # ,command=Caixa)
        salvar_tela_estoque.place(x=150, y=350)

        fechar_tela_estoque = Button(text="FECHAR")  # ,command=Caixa)
        fechar_tela_estoque.place(x=400, y=350)


        top.mainloop()


principal()

