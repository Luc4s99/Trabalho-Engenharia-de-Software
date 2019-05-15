from tkinter import *

valor = DoubleVar


class AberturaCaixa(Frame):

    def __init__(self, **kw):
        caixa_top = Tk()
        caixa_top.title("Abertura do Caixa")
        caixa_top.geometry("600x300")
        caixa_top.configure(background='#D3D3D3')

        caixa_canvas = Canvas(caixa_top, width=800, height=500, background='#DFFFD3')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 200, fill="white")
        caixa_canvas.place(x=0, y=0)

        caixa = Label(text="Saldo Inicial")
        caixa.place(x=120, y=100)

        ValorInicial = Entry(textvar=valor)
        ValorInicial.place(x=250, y=100)

        abrircaixa = Button(text="Abrir Caixa")  # ,command=Caixa)
        abrircaixa.place(x=150, y=230)

        voltar = Button(text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=230)

        caixa_top.mainloop()
