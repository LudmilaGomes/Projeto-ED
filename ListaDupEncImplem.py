from tkinter import *

# definimos a classe do nó
class Node:
    # a classe é inicializada
    def __init__(self, valor):
        self.valor = valor      # o conteúdo do nó
        self.proximo = None     # aponta para o próximo nó
        self.anterior = None    # aponta para o nó anterior

# definimos a classe da lista duplamente encadeada
class ListaDuplamenteEncadeada:
    # a classe é inicializada
    def __init__(self):
        self.inicio = None      # primeiro nó
        self.fim = None         # último nó

    # método que retorna True se a lista estiver vazia; False, caso contrário
    def vazia(self):
        if (self.obter_tamanho() == 0):
            return True
        else:
            return False

    # método para inserir novos elementos; recebe como parâmetros o valor do novo elemento e sua posição na lista
    def inserir(self, valor, posicao):
        novo_no = Node(valor)

        # tratamento de erro para não aceitar posição nula ou negativa
        if posicao <= 0:
            return False
        
        # se inserimos o elemento na primeira posição
        if posicao == 1:
            # o novo nó tem como próximo nó o nó do início; nos certificamos de que o nó anterior do novo nó aponta para None
            novo_no.proximo = self.inicio
            novo_no.anterior = None

            # lista está vazia e inserimos o primeiro elemento da lista no fim
            if(self.vazia()):
                self.fim = novo_no
            else: # caso contrário: lista não vazia; nó do início tem como nó anterior o novo nó inserido
                self.inicio.anterior = novo_no
            
            # o novo nó é o nó do início
            self.inicio = novo_no
            return True
        else: # se inserimos elemento no meio ou fim da lista
            # percorremos os nós da lista e auxiliar recebe o nó anterior ao da posição indicada pelo usuário 
            auxiliar = self.inicio
            for i in range(posicao - 2):
                if auxiliar is None:
                    return False
                auxiliar = auxiliar.proximo

            # se o nó da posição indicada estiver vazio, retorna False
            if auxiliar is None:
                return False

            # o novo nó tem como nó anterior o auxiliar; o próximo nó é o próximo do auxiliar
            novo_no.anterior = auxiliar
            novo_no.proximo = auxiliar.proximo

            if auxiliar.proximo is not None:
                # o nó seguinte ao auxiliar agora tem como nó anterior o novo nó criado
                auxiliar.proximo.anterior = novo_no

            # por fim, o nó auxiliar tem como próximo nó o novo nó
            auxiliar.proximo = novo_no

            return True

    # método para remover elementos; recebe como parâmetro a posição na lista do elemento a ser removido
    def remover_por_posicao(self, posicao):
        # não é possível remover elementos quando a lista está vazia
        if self.vazia() == True:
            return False
        # não é possível remover elemento em posição nula ou negativa; só acessamos elementos nas posições 1, 2, 3, etc;
        if posicao <= 0:
            return False
        # se removemos o primeiro elemento da lista
        if posicao == 1:
            # o nó do início passa a ser o segundo nó (ou seja, o nó próximo ao início)
            self.inicio = self.inicio.proximo
            if self.inicio is not None:
                # o nó anterior ao início é None (não aponta para nenhum nó)
                self.inicio.anterior = None
            return True
        else: # se removemos um elemento no meio ou fim da lista
            # percorremos os nós da lista do começo até o nó da (posição indicada - 1)
            no_anterior = self.inicio
            for i in range(posicao - 2):
                if no_anterior is None:
                    return False
                no_anterior = no_anterior.proximo

            # se o nó da (posição indicada - 1) não é vazio e se seu próximo nó não é vazio
            if no_anterior is not None and no_anterior.proximo is not None:
                # fazemos as devidas alterações nos nós próximo e anterior para os quais no_anterior.proximo aponta
                no_anterior.proximo = no_anterior.proximo.proximo
                if no_anterior.proximo is not None:
                    no_anterior.proximo.anterior = no_anterior
                else:
                    self.fim = no_anterior
                return True
            else:
                return False
        
    def remover_por_valor(self, valor):
        no_anterior = None

        # percorremos os nós da lista do começo até o nó da (posição indicada - 1)
        no_atual = self.inicio
        while no_atual is not None:
            # valor_atual recebe o conteúdo do nó em que estamos na iteração atual
            valor_atual = int(no_atual.valor)
            # encontramos o valor que desejamos remover da lista
            if valor_atual == valor:
                # no_anterior is None significa que o nó atual é o início da lista
                if no_anterior is None:
                    self.inicio = no_atual.proximo
                    if no_atual.proximo is not None:
                        no_atual.proximo.anterior = None
                else: # Caso o valor a ser removido esteja em algum nó do meio ou fim da lista
                    no_anterior.proximo = no_atual.proximo
                    if no_atual.proximo is not None:
                        no_atual.proximo.anterior = no_anterior
                return True
            
            # nas iterações, temos o nó da iteração atual e o nó anterior ao atual
            no_anterior = no_atual
            no_atual = no_atual.proximo
        
        return False

    # método para consultar elementos; recebe como parâmetro o valor do elemento a ser consultado
    def consulta_por_valor(self, valor):
        no_atual = self.inicio
        posicao = 1
        while no_atual is not None:
            if no_atual.valor == valor:
                return posicao
            no_atual = no_atual.proximo
            posicao += 1
        return None

    # método para consultar elementos; recebe como parâmetro a posição do elemento a ser consultado
    def consulta_por_posicao(self, posicao):
        if posicao < 1:
            return None

        no_atual = self.inicio
        for i in range(posicao - 1):
            if no_atual is None:
                return None
            no_atual = no_atual.proximo

        if no_atual is None:
            return None

        return no_atual.valor

    # método que retorna a quantidade de elementos da lista
    def obter_tamanho(self):
        tamanho = 0
        no_atual = self.inicio
        while no_atual is not None:
            tamanho += 1
            no_atual = no_atual.proximo
        return tamanho

    # método que retorna todos os valores de uma lista
    def obter_valores(self):
        valores = []
        atual = self.inicio
        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo
        return valores