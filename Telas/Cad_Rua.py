from tkinter import *
from tkinter import ttk


class CadastroBairro(Frame):

    def __init__(self):
        tela_cad_rua = Tk()
        tela_cad_rua.geometry("600x400")
        tela_cad_rua.title("Cadastrar Rua")
        tela_cad_rua.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_cad_rua, width=800, height=500, background='#ccd7ff')
        caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white", outline='red', width=3)
        caixa_canvas.place(x=0, y=0)

        nome_rua_label = Label(tela_cad_rua, text="Nome da Rua:")
        nome_rua_label.place(x=70, y=100)
        nome_rua_entrada = Entry(tela_cad_rua, width=43)
        nome_rua_entrada.place(x=170, y=100)

        nome_bairro_label = Label(tela_cad_rua, text="Bairro:")
        nome_bairro_label.place(x=70, y=160)
        combo_bairros = ttk.Combobox(tela_cad_rua,
                                    values=[
                                        "Aqui vem uma",
                                        "query SQL",
                                        "que mostra",
                                        "as opções"])
        combo_bairros.place(x=120, y=160)

        salvar = Button(tela_cad_rua, text="Cadastrar")
        salvar.place(x=150, y=330)
        voltar = Button(tela_cad_rua, text="Voltar")
        voltar.place(x=400, y=330)

        tela_cad_rua.mainloop()


CadastroBairro()
