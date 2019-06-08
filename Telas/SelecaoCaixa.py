from tkinter import *
import Telas.FechamentoCaixa
import Telas.AberturaCaixa


class SelecaoCaixa(Frame):
    def __init__(self):
        self.tela_selecao_caixa = Tk()
        self.tela_selecao_caixa.geometry("600x400")
        self.tela_selecao_caixa.title("Selecao de Caixa")
        self.tela_selecao_caixa.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_selecao_caixa, width=800, height=500, background='#ccd7ff')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        bt1 = Button(self.tela_selecao_caixa, text="Abrir Caixa", width=15, command=self.ChamaAberturaCaixa)
        bt1.place(x=120, y=150)
        bt2 = Button(self.tela_selecao_caixa, text="Fechar Caixa", width=15, command=self.ChamaFechamentoCaixa)
        bt2.place(x=360, y=150)

        salvar = Button(self.tela_selecao_caixa, text="Salvar")  # ,command=Caixa)
        salvar.place(x=150, y=330)
        voltar = Button(self.tela_selecao_caixa, text="Voltar", command=self.voltar)  # ,command=Caixa)
        voltar.place(x=400, y=330)

        self.tela_selecao_caixa.mainloop()

    def voltar(self):
        self.tela_selecao_caixa.destroy()

    def ChamaAberturaCaixa(self):
        Telas.AberturaCaixa.AberturaCaixa()

    def ChamaFechamentoCaixa(self):
        Telas.FechamentoCaixa.Fechamento_Caixa()
