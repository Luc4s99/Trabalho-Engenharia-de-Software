from tkinter import *
import CadastroFornecedor

class Cadastros(Frame):

    def __init__(self):
        tela_cadastros = Tk()
        tela_cadastros.title("Tela de cadastros")
        tela_cadastros.geometry("600x300")
        tela_cadastros.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_cadastros, width=800, height=500, background='#DFFFD3')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 200, fill="white")
        caixa_canvas.place(x=0, y=0)


        botao_cadastro_fornecedores = Button(tela_cadastros, text="Cadastrar Fornecedor",command=self.ChamaCadastroFornecedor)
        botao_cadastro_fornecedores.place(x=150, y=50)

        botao_cadastro_mercadorias = Button(tela_cadastros, text="Cadastrar Mercadoria")  # ,command=Caixa)
        botao_cadastro_mercadorias.place(x=150, y=100)

        botao_cadastro_clientes = Button(tela_cadastros, text="Cadastrar Clientes")  # ,command=Caixa)
        botao_cadastro_clientes.place(x=150, y=150)

        voltar = Button(tela_cadastros, text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=230)

        tela_cadastros.mainloop()
        self.tela_cadastros.destroy()

    def ChamaCadastroFornecedor(self):
        CadastroFornecedor.CadastroFornecedor()
