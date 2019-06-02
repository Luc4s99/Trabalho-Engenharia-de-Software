from tkinter import *

valor = DoubleVar


class AberturaCaixa(Frame):

    def __init__(self):
        tela_caixa = Tk()
        tela_caixa.title("Abertura do Caixa")
        tela_caixa.geometry("600x300")
        tela_caixa.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_caixa, width=800, height=500, background='#DFFFD3')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 200, fill="white")
        caixa_canvas.place(x=0, y=0)

        saldo_inicial_label = Label(tela_caixa, text="Saldo Inicial")
        saldo_inicial_label.place(x=120, y=100)

        valor_inicial_label = Entry(tela_caixa, textvar=valor)
        valor_inicial_label.place(x=250, y=100)

        abrircaixa = Button(tela_caixa, text="Abrir Caixa")  # ,command=Caixa)
        abrircaixa.place(x=150, y=230)

        voltar = Button(tela_caixa, text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=230)

        tela_caixa.mainloop()
