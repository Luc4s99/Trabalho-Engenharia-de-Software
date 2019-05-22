from tkinter import *

valorInicialCaixa = DoubleVar





def ChamaCaixa():
    caix = Tk()
    caix.title("Abertura do Caixa")
    caix.geometry("600x300")
    caix.configure(background='#D3D3D3')

    canvas = Canvas(caix, width=800, height=500, background='#DFFFD3')

    r1 = canvas.create_rectangle(50, 50, 550, 200, fill="white")
    canvas.place(x=0, y=0)

    caixa = Label(caix, text="Saldo Inicial")
    caixa.place(x=120, y=100)

    ValorInicial = Entry(caix, textvar=valorInicialCaixa)
    ValorInicial.place(x=250, y=100)

    abrircaixa = Button(caix, text="Abrir Caixa")  # ,command=Caixa)
    abrircaixa.place(x=150, y=230)

    voltar = Button(caix, text="Voltar")  # ,command=Caixa)
    voltar.place(x=400, y=230)

    caix.mainloop()


def __init__(self):
    top = Tk()
    top.title("Bem Vindo")
    top.geometry("800x500")
    top.configure(background='#D3D3D3')






    canvas = Canvas(top, width=800, height=500, background='#DFFFD3')

    r1 = canvas.create_rectangle(50, 100, 250, 400, fill="white")
    r2 = canvas.create_rectangle(300, 100, 700, 220, fill="white")
    r3 = canvas.create_rectangle(300, 250, 700, 400, fill="white")
    canvas.place(x=0, y=0)

    caixa = Button(text="Caixa",command=ChamaCaixa)
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



principal()

