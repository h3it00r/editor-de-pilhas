import time
import os

class PilhaException(Exception):

    def __init__(self, mensagem):
        super().__init__(mensagem)

class Node:
    
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: 'Node' | None = proximo


class PilhaEncadeada:

    def __init__(self):
        self.__tamanho: int = 0
        self.__topo: Node | None = None

    def esta_vazia(self):
        return self.__topo is None

    def tamanho(self):
        return self.__tamanho

    def empilhar(self, elemento):
        self.__topo = Node(elemento, proximo=self.__topo)
        # if self.esta_vazia():
        #     self.__topo = Node(elemento)
        # else:
        #     novo_no = Node(elemento)
        #     novo_no.proximo = self.__topo
        #     self.__topo = novo_no
        #self.__lista_pilhas(self.__topo)
        self.__tamanho += 1

    @classmethod
    def concatena_pilhas(cls, pilha1, pilha2):
        pilha1.inverter()
        pilha2.inverter()
        
        nova_pilha = PilhaEncadeada()

        for i in range(pilha1.tamanho()):
            nova_pilha.empilhar(pilha1.get_valor(i + 1))

        for i in range(pilha2.tamanho()):
            nova_pilha.empilhar(pilha2.get_valor(i + 1))

        pilha1.inverter()
        pilha2.inverter()

        return nova_pilha
    
    def concatena(self, pilha):
        pilha.inverter()

        for i in range (pilha.tamanho()):
            self.empilhar(pilha.desempilhar())

    def get_valor(self,index):
        if self.esta_vazia():
            raise PilhaException('A pilha está vazia.')
        
        no = self.__topo
        apontador = 1
        while no.proximo and apontador < index:
            no = no.proximo
            apontador += 1
        return no.valor
        
    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaException('A pilha está vazia.')
        
        valor = self.__topo.valor
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return valor
    
    def inverter (self):
        if self.esta_vazia():
            raise PilhaException('A pilha está vazia.')
        
        pilha = self.__topo
        self.esvazia()
        while pilha:
            self.empilhar(pilha.valor)
            pilha = pilha.proximo

    def esvazia (self):
        if self.esta_vazia():
            raise PilhaException ('A pilha está vazia.')
        while self.__tamanho > 0:
            self.desempilhar()
    
    def obter_topo(self):
        if self.esta_vazia():
            raise PilhaException ('A pilha está vazia.')
        return self.__topo.valor

    def imprimir(self):
        print(self.__str__())
       
    def __str__(self):
        no: Node = self.__topo
        str = 'Pilha = ['
        no_str = ''
        pilha = ''
        while no:
            no_str += f'{no.valor}'
            if no.proximo:
                no_str += ' ,'
            no = no.proximo
        for i in range (len(no_str)):
            pilha += no_str [len(no_str) - i - 1]
        return str + pilha + ']'