from tkinter import *

nome_material = StringVar
qtd_material = 0


class Compra(Frame):

    def __init__(self):
        tela_compra = Tk()
        tela_compra.geometry("600x400")
        tela_compra.title("Comprar Materiais")
        tela_compra.configure(background='#D3D3D3')

        caixa_canvas = Canvas(tela_compra, width=800, height=500, background='#DFFFD3')
        r1 = caixa_canvas.create_rectangle(50, 50, 550, 300, fill="white")
        caixa_canvas.place(x=0, y=0)

        nome_material_label = Label(tela_compra, text="Material")
        nome_material_label.place(x=65, y=100)
        nome_material_entrada = Entry(tela_compra, textvar=nome_material)
        nome_material_entrada.place(x=125, y=100)

        qtd_material_label = Label(tela_compra, text="Quantidade")
        qtd_material_label.place(x=310, y=100)
        qtd_material_entrada = Entry(tela_compra, textvar=qtd_material)
        #qtd_material = int(Entry.get(self))
        qtd_material_entrada.place(x=390, y=100)


        salvar = Button(tela_compra, text="Comprar")  # ,command=Caixa)
        salvar.place(x=150, y=330)
        voltar = Button(tela_compra, text="Voltar")  # ,command=Caixa)
        voltar.place(x=400, y=330)

        tela_compra.mainloop()


Compra()
