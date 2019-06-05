from tkinter import *

valor = DoubleVar


class AberturaCaixa(Frame):

    def __init__(self):
        self.tela_caixa = Tk()
        self.tela_caixa.title("Abertura do Caixa")
        self.tela_caixa.geometry("600x300")
        self.tela_caixa.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_caixa, width=800, height=500, background='#DFFFD3')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 200, fill="white")
        caixa_canvas.place(x=0, y=0)

        saldo_inicial_label = Label(self.tela_caixa, text="Saldo Inicial")
        saldo_inicial_label.place(x=120, y=100)

        valor_inicial_label = Entry(self.tela_caixa, textvar=valor)
        valor_inicial_label.place(x=250, y=100)

        abrircaixa = Button(self.tela_caixa, text="Abrir Caixa")  # ,command=Caixa)
        abrircaixa.place(x=150, y=230)

        voltar = Button(self.tela_caixa, text="Voltar", command=self.voltar)  # ,command=Caixa)
        voltar.place(x=400, y=230)

        self.tela_caixa.mainloop()

    def voltar(self):
        self.tela_caixa.destroy()