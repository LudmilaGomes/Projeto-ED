from tkinter import *
import ListaDupEncImplem

class InterfaceGrafica:
    def __init__(self, master):
        self.lista_duplamente_encadeada = ListaDupEncImplem.ListaDuplamenteEncadeada()

        master.title("Lista Duplamente Encadeada")

        self.label = Label(master, text="Lista Duplamente Encadeada", font=("Arial", 15))
        self.label.pack(padx=20, pady=20)

        self.frame_caixas = Frame(master)
        self.frame_caixas.pack(side=TOP, pady=10)

        self.label_inserir_valor = Label(self.frame_caixas, text="Valor")
        self.label_inserir_valor.grid(row=0, column=0, padx=5)
        self.caixa_inserir_valor = Entry(self.frame_caixas)
        self.caixa_inserir_valor.grid(row=0, column=1)
        self.label_inserir_posicao = Label(self.frame_caixas, text="Posição")
        self.label_inserir_posicao.grid(row=1, column=0, padx=5)
        self.caixa_inserir_posicao = Entry(self.frame_caixas)
        self.caixa_inserir_posicao.grid(row=1, column=1)
        self.button_inserir = Button(self.frame_caixas, text="Inserir", command=self.inserir)
        self.button_inserir.grid(row=0, column=2, rowspan=2, padx=15)
        self.label_erro_inserir = Label(self.frame_caixas, text="", fg="red")
        self.label_erro_inserir.grid(row=0, column=3, rowspan=2)

        self.label_remover_posicao = Label(master, text="Posição")
        self.label_remover_posicao.pack()
        self.caixa_remover_posicao = Entry(master)
        self.caixa_remover_posicao.pack()
        self.button_remover = Button(master, text="Remover", command=self.remover_por_posicao)
        self.button_remover.pack(pady=10)
        self.label_erro_remover_posicao = Label(master, text="", fg="red")
        self.label_erro_remover_posicao.pack()
        
        self.label_remover_valor = Label(master, text="Valor a ser removido")
        self.label_remover_valor.pack()
        self.caixa_remover_valor = Entry(master)
        self.caixa_remover_valor.pack()
        self.button_remover_valor = Button(master, text="Remover", command=self.remover_por_valor)
        self.button_remover_valor.pack(pady=10)
        self.label_erro_remover_valor = Label(master, text="", fg="red")
        self.label_erro_remover_valor.pack()

        self.label_consulta_valor = Label(master, text="Consultar por Valor")
        self.label_consulta_valor.pack()
        self.caixa_consulta_valor = Entry(master)
        self.caixa_consulta_valor.pack()
        self.button_consulta = Button(master, text="Consultar", command=self.consulta_por_valor)
        self.button_consulta.pack(pady=10)
        self.label_resultado_consulta = Label(master, text="", fg="green")
        self.label_resultado_consulta.pack()

        self.label_consulta_posicao = Label(master, text="Consultar por Posição")
        self.label_consulta_posicao.pack()
        self.caixa_consulta_posicao = Entry(master)
        self.caixa_consulta_posicao.pack()
        self.button_consulta_posicao = Button(master, text="Consultar", command=self.consulta_por_posicao)
        self.button_consulta_posicao.pack(pady=10)
        self.label_resultado_consulta_posicao = Label(master, text="", fg="green")
        self.label_resultado_consulta_posicao.pack()

        self.label_tamanho = Label(master, text="Tamanho")
        self.label_tamanho.pack()
        self.label_valor_tamanho = Label(master, text="")
        self.label_valor_tamanho.pack()

        self.frame_lista = Frame(master)
        self.frame_lista.pack(pady = 10)

        i = self.lista_duplamente_encadeada.obter_tamanho()
        while i:
            print( self.lista_duplamente_encadeada.consulta_por_posicao(i) )
            i -= 1
        
        # Criando o canvas para desenhar as caixas e linhas
        self.canvas = Canvas(master, bg="white", width=500, height=102, scrollregion=(0, 0, 5000, 0))
        self.canvas.pack(padx=10, pady=10)
        hbar=Scrollbar(self.canvas,orient=HORIZONTAL)
        hbar.pack(side=BOTTOM,fill=X)
        hbar.config(command=self.canvas.xview)
        vbar=Scrollbar(self.canvas,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(width=300,height=300)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT,expand=True,fill=BOTH)
        # Desenhando as caixas iniciais
        self.desenhar_caixas()

    def inserir(self):
        valor = self.caixa_inserir_valor.get()
        posicao = int(self.caixa_inserir_posicao.get())
        if self.lista_duplamente_encadeada.inserir(valor, posicao):
            self.label_erro_inserir.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            self.label_erro_inserir.config(text="ERROR")

    def remover_por_posicao(self):
        posicao = int(self.caixa_remover_posicao.get())
        if self.lista_duplamente_encadeada.remover_por_posicao(posicao):
            self.label_erro_remover_posicao.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            self.label_erro_remover_posicao.config(text="ERROR")
    
    def remover_por_valor(self):
        valor = int(self.caixa_remover_valor.get())
        if self.lista_duplamente_encadeada.remover_por_valor(valor):
            self.label_erro_remover_valor.config(text="")
            #self.atualizar_lista()
            self.desenhar_caixas()
        else:
            self.label_erro_remover_valor.config(text="ERROR")

    def consulta_por_valor(self):
        valor = self.caixa_consulta_valor.get()
        posicoes = self.lista_duplamente_encadeada.consulta_por_valor(valor)
        if posicoes is not None:
            self.label_resultado_consulta.config(text="Valor encontrado na(s) posição(ões): {}".format(posicoes))
        else:
            self.label_resultado_consulta.config(text="Valor não encontrado")

    def consulta_por_posicao(self):
        posicao = int(self.caixa_consulta_posicao.get())
        valor = self.lista_duplamente_encadeada.consulta_por_posicao(posicao)
        if valor is not None:
            self.label_resultado_consulta_posicao.config(text="Valor na posição {}: {}".format(posicao, valor))
        else:
            self.label_resultado_consulta_posicao.config(text="Posição inválida")

    def desenhar_caixas(self):
        # Limpando o canvas e redesenhando as caixas e linhas
        self.canvas.delete("all")

        x, y = 50, 10
        valores = self.lista_duplamente_encadeada.obter_valores()

        if self.lista_duplamente_encadeada.obter_tamanho() != 0:
            caixa = self.canvas.create_rectangle(x, y, x+50, y+30, fill="white", outline="black")
            self.canvas.create_text(x+25, y+15, text="Cabeça")
            x2, y2 = x+50, y+10
            x3, y3 = x+100, y+10
            self.canvas.create_line(x2, y2, x3, y3, arrow="last")
            self.canvas.create_line(x2, y2+10, x3, y3+10, arrow="first")
            x += 50

        for i, valor in enumerate(valores):
            # Desenhando a caixa
            caixa = self.canvas.create_rectangle(x, y, x+50, y+30, fill="white", outline="black")
            self.canvas.create_text(x+25, y+15, text=valor)

            # Desenhando as linhas para a caixa seguinte, se houver
            if i < self.lista_duplamente_encadeada.obter_tamanho()-1:
                x2, y2 = x+50, y+10
                x3, y3 = x+100, y+10
                self.canvas.create_line(x2, y2, x3, y3, arrow="last", fill="blue")
                self.canvas.create_line(x2, y2+10, x3, y3+10, arrow="first", fill="red")

            x += 100
            if i is self.lista_duplamente_encadeada.obter_tamanho()-1:
                caixa = self.canvas.create_rectangle(x-50, y, x, y+30, fill="white", outline="black")
                self.canvas.create_text(x-25, y+15, text="Cauda")

root = Tk()
root.geometry("500x750")
app = InterfaceGrafica(root)
root.mainloop()