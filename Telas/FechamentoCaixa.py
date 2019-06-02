from tkinter import *


total_vendas = float
saldo_inicial = float
saldo_final = float


class Fechamento_Caixa(Frame):

    def __init__(self):
        tela_fechamento_caixa = Tk()
        tela_fechamento_caixa.title("Fechamento Caixa")
        tela_fechamento_caixa.geometry("600x350")
        tela_fechamento_caixa.configure(background='#D3D3D3')

        canvas = Canvas(tela_fechamento_caixa, width=1366, height=768, background='#DFFFD3')

        r1 = canvas.create_rectangle(50, 50, 550, 300, fill="white")
        canvas.place(x=0, y=0)

        total_vendas_label = Label(tela_fechamento_caixa, text="Total de vendas: ")
        total_vendas_label.place(x=70, y=100)

        total_vendas_label2 = Label(tela_fechamento_caixa, text=total_vendas)
        total_vendas_label2.place(x=320, y=100)


        saldo_inicial_label = Label(tela_fechamento_caixa, text="Saldo Inicial: ")
        saldo_inicial_label.place(x=70, y=150)

        saldo_inicial_label2 = Label(tela_fechamento_caixa, text=saldo_inicial)
        saldo_inicial_label2.place(x=320, y=150)


        saldo_final_label = Label(tela_fechamento_caixa, text="Saldo Final: ")
        saldo_final_label.place(x=70, y=200)

        saldo_final_label2 = Label(tela_fechamento_caixa, text=saldo_final)
        saldo_final_label2.place(x=320, y=200)


        encerrar_fechamento_caixa = Button(tela_fechamento_caixa, text="Encerrar")  # ,command=Caixa)
        encerrar_fechamento_caixa.place(x=150, y=250)

        desistir_fechamento_caixa = Button(tela_fechamento_caixa, text="Desistir")  # ,command=Caixa)
        desistir_fechamento_caixa.place(x=400, y=250)


        tela_fechamento_caixa.mainloop()

