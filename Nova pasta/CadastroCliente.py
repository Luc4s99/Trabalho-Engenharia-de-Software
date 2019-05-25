from tkinter import *

nome_cliente_cadastro = StringVar
endereco_cliente_cadastro = StringVar
telefone_cliente_cadastro = StringVar
cnpj_cliente_cadastro = StringVar


class CadastroCliente(Frame):

    def __init__(self):
        tela_cadastro_cliente = Tk()
        tela_cadastro_cliente.title("Cadastro Cliente")
        tela_cadastro_cliente.geometry("600x400")
        tela_cadastro_cliente.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_cadastro_cliente, width=800, height=500, background='#DFFFD3')

        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white")
        caixa_canvas.place(x=0, y=0)

        nome_cliente_label = Label(tela_cadastro_cliente, text="Nome do Cliente")
        nome_cliente_label.place(x=120, y=100)

        nome_cliente_entrada = Entry(tela_cadastro_cliente, textvar=nome_cliente_cadastro)
        nome_cliente_entrada.place(x=250, y=100)
        #####################################################
        endereco_cliente_label = Label(tela_cadastro_cliente, text="Endereço do Cliente")
        endereco_cliente_label.place(x=120, y=150)

        endereco_cliente_entrada = Entry(tela_cadastro_cliente, textvar=endereco_cliente_cadastro)
        endereco_cliente_entrada.place(x=260, y=150)
        ####################################################
        telefone_cliente_label = Label(tela_cadastro_cliente, text="Telefone do Cliente")
        telefone_cliente_label.place(x=120, y=200)

        telefone_cliente_entrada = Entry(tela_cadastro_cliente, textvar=telefone_cliente_cadastro)
        telefone_cliente_entrada.place(x=260, y=200)
        ####################################################
        CPF_cliente_label = Label(tela_cadastro_cliente, text="CPF do Cliente")
        CPF_cliente_label.place(x=120, y=250)

        CPF_cliente_entrada = Entry(tela_cadastro_cliente, textvar=cnpj_cliente_cadastro)
        CPF_cliente_entrada.place(x=260, y=250)
        ####################################################

        salvar = Button(tela_cadastro_cliente, text="Salvar")  # ,command=Caixa)
        salvar.place(x=150, y=330)

        voltar = Button(tela_cadastro_cliente, text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=330)

        tela_cadastro_cliente.mainloop()


CadastroCliente()
