from tkinter import *

nome_fornecedor_cadastro = StringVar
endereco_fornecedor_cadastro = StringVar
telefone_fornecedor_cadastro = StringVar
cnpj_fornecedor_cadastro = StringVar

class CadastroFornecedor(Frame):

    def __init__(self):
        tela_cadastro_fornecedor = Tk()
        tela_cadastro_fornecedor.title("Cadastro Fornecedor")
        tela_cadastro_fornecedor.geometry("600x400")
        tela_cadastro_fornecedor.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_cadastro_fornecedor, width=800, height=500, background='#DFFFD3')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white")
        caixa_canvas.place(x=0, y=0)

        nome_fornecedor_label = Label(tela_cadastro_fornecedor, text="Nome do Fornecedor")
        nome_fornecedor_label.place(x=120, y=100)

        nome_fornecedor_entrada = Entry(tela_cadastro_fornecedor, textvar=nome_fornecedor_cadastro)
        nome_fornecedor_entrada.place(x=250, y=100)
#####################################################
        endereco_fornecedor_label = Label(tela_cadastro_fornecedor, text="Endereço do Fornecedor")
        endereco_fornecedor_label.place(x=120, y=150)

        endereco_fornecedor_entrada = Entry(tela_cadastro_fornecedor, textvar=endereco_fornecedor_cadastro)
        endereco_fornecedor_entrada.place(x=260, y=150)
####################################################
        telefone_fornecedor_label = Label(tela_cadastro_fornecedor, text="Telefone do Fornecedor")
        telefone_fornecedor_label.place(x=120, y=200)

        telefone_fornecedor_entrada = Entry(tela_cadastro_fornecedor, textvar=telefone_fornecedor_cadastro)
        telefone_fornecedor_entrada.place(x=260, y=200)
####################################################
        CNPJ_fornecedor_label = Label(tela_cadastro_fornecedor, text="CNPJ do Fornecedor")
        CNPJ_fornecedor_label.place(x=120, y=250)

        CNPJ_fornecedor_entrada = Entry(tela_cadastro_fornecedor, textvar=cnpj_fornecedor_cadastro)
        CNPJ_fornecedor_entrada.place(x=260, y=250)
####################################################


        salvar = Button(tela_cadastro_fornecedor, text="Salvar")  # ,command=Caixa)
        salvar.place(x=150, y=330)

        voltar = Button(tela_cadastro_fornecedor, text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=330)

        tela_cadastro_fornecedor.mainloop()
