from tkinter import *
import CadastroFornecedor
import Cad_Rua
import Cad_Bairro
import CadastroCliente


class Cadastros(Frame):

    def __init__(self):
        self.tela_cadastros = Tk()
        self.tela_cadastros.title("Tela de cadastros")
        self.tela_cadastros.geometry("600x300")
        self.tela_cadastros.configure(background='#D3D3D3')

        caixa_canvas = Canvas(self.tela_cadastros, width=800, height=500, background='#DFFFD3')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 200, fill="white")
        caixa_canvas.place(x=0, y=0)

        botao_cadastro_fornecedores = Button(self.tela_cadastros, text="Cadastrar Fornecedor", width=18, command=self.ChamaCadastroFornecedor)
        botao_cadastro_fornecedores.place(x=110, y=60)

        botao_cadastro_mercadorias = Button(self.tela_cadastros, text="Cadastrar Mercadoria", width=18)  # ,command=Caixa)
        botao_cadastro_mercadorias.place(x=110, y=110)

        botao_cadastro_clientes = Button(self.tela_cadastros, text="Cadastrar Clientes", width=18, command=self.ChamaCadastroCliente)  # ,command=Caixa)
        botao_cadastro_clientes.place(x=110, y=160)

        botao_cadastro_rua = Button(self.tela_cadastros, text="Cadastrar Rua", width=18, command=self.ChamaCadastroRua)
        botao_cadastro_rua.place(x=320, y=60)

        botao_cadastro_bairro = Button(self.tela_cadastros, text="Cadastrar Bairro", width=18, command=self.ChamaCadastroBairro)
        botao_cadastro_bairro.place(x=320, y=110)

        voltar = Button(self.tela_cadastros, text="Voltar", command=self.voltar)  # ,command=Caixa)
        voltar.place(x=400, y=230)

        self.tela_cadastros.mainloop()
        self.tela_cadastros.destroy()

    def ChamaCadastroFornecedor(self):
        CadastroFornecedor.CadastroFornecedor()

    def ChamaCadastroRua(self):
        Cad_Rua.CadastroRua()

    def ChamaCadastroBairro(self):
        Cad_Bairro.CadastroBairro()

    def ChamaCadastroCliente(self):
        CadastroCliente.CadastroCliente()

    def voltar(self):
        self.tela_cadastros.destroy()
