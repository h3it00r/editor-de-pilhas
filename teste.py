import time
import os
from pilha import PilhaEncadeada, PilhaException

class MainException(Exception):

    def __init__(self, mensagem):
        super().__init__(mensagem)

class Node:
    
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: 'Node' | None = proximo

class Main:

    def __init__(self):
        self.__pilha = PilhaEncadeada()
        self.__head_lista = Node (self.__pilha)
        self.__total_pilhas = 1
        self.__pilha_atual = 1
        self.__opcao = None

    def __processar_opcao(self,opcao):
        match opcao:
            
            case '1':
                try:
                    os.system('cls')
                    numero = int (input('Número a ser adicionado à pilha: '))
                except:
                    os.system('cls')
                    print ('Você precisa escolhar um número para ser adicionado à pilha.')
                    time.sleep(3)
                    os.system('cls')
                    return

                self.__pilha.empilhar(numero)
                os.system('cls')
                print(f'Valor empilhado: {numero}.')
                time.sleep(3)
                os.system('cls')
            
            case '2':
                try:
                    os.system('cls')
                    print(f'Valor desempilhado: {self.__pilha.desempilhar()}')
                    time.sleep(3)
                    os.system('cls')
                except PilhaException as pe:
                    os.system('cls')
                    print(pe)
                    time.sleep(3)
                    os.system('cls')
            
            case '3':
                os.system('cls')
                print(f'Tamanho da pilha: {self.__pilha.tamanho()}')
                time.sleep(3)
                os.system('cls')
            
            case '4':
                try:
                    os.system('cls')
                    print(f'Topo da pilha: {self.__pilha.obter_topo()}')
                    time.sleep(3)
                    os.system('cls')
                except PilhaException as pe:
                    os.system('cls')
                    print(pe)
                    time.sleep(3)
                    os.system('cls')
            
            case '5':
                os.system('cls')
                print(f'Pilha vazia: {self.__pilha.esta_vazia()}')
                time.sleep(3)
                os.system('cls')
            
            case '6':
                os.system('cls')
                self.__pilha = PilhaEncadeada()
                self.__lista_pilhas(self.__pilha)
                self.__pilha_atual = self.__total_pilhas
                print('Nova pilha criada.')
                time.sleep(3)
                os.system('cls')
            
            case '7':
                if self.__pilha.tamanho() <= 1:
                    os.system('cls')
                    print('O tamanho da pilha deve ser maior que um para que está operação seja feita.')
                    time.sleep(3)
                    os.system('cls')
                    return
                try:
                    os.system('cls')
                    self.__pilha.inverter()
                    print('A pilha foi invertida.')
                    time.sleep(3)
                    os.system('cls')
                except PilhaException as pe:
                    os.system('cls')
                    print(pe)
                    time.sleep(3)
                    os.system('cls')
            
            case '8':
                try:
                    os.system('cls')
                    self.__pilha.esvazia()
                    print('A pilha foi esvaziada.')
                    time.sleep(3)
                    os.system('cls')
                except PilhaException as pe:
                    os.system('cls')
                    print(pe)
                    time.sleep(3)
                    os.system('cls')
            
            case '9':
                try:
                    os.system('cls')
                    pilha_1 = int (input('Primeira pilha: '))
                
                except:
                    os.system('cls')
                    print(f'Você precisa escolher um número entre 1 e o total de pilhas ({self.__total_pilhas}).')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                if pilha_1 < 1 or pilha_1 > self.__total_pilhas:
                    os.system('cls')
                    print(f'Você precisa escolher um número entre 1 e o total de pilhas ({self.__total_pilhas}).')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                uma_pilha = self.__selecionar_pilha(pilha_1)

                if uma_pilha.esta_vazia():
                    os.system('cls')
                    print('Não é possível realizar contatenação com essa pilha, pois ela está vazia.')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                if self.__pilha.esta_vazia():
                    os.system('cls')
                    print('Não é possível realizar contatenação com essa pilha, pois ela está vazia.')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                try:
                    os.system('cls')
                    pilha_2 = int (input('Pilha a ser concatenada com a primeira: '))
                
                except:
                    os.system('cls')
                    print(f'Você precisa escolher um número entre 1 e o total de pilhas ({self.__total_pilhas}).')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                if pilha_1 == pilha_2:
                    os.system('cls')
                    print('Você deve escolher uma pilha diferente da primeira.')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                if pilha_2 < 1 or pilha_2 > self.__total_pilhas:
                    os.system('cls')
                    print(f'Você precisa escolher um número entre 1 e o total de pilhas ({self.__total_pilhas}).')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                outra_pilha = self.__selecionar_pilha(pilha_2)
                
                if outra_pilha.esta_vazia():
                    os.system('cls')
                    print('Não é possível realizar contatenação com essa pilha, pois ela está vazia.')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                while True:
                    os.system('cls')
                    print ('Deseja criar uma nova pilha para concatenar as pilhas selecionadas [S/N]?\n')
                    opcao_concatenar = input ('Resposta: ').lower()
                    os.system('cls')
                    if opcao_concatenar == 's' or opcao_concatenar == 'n':
                        break
                    
                match opcao_concatenar:
                    
                    case 's':
                        self.__pilha = self.__pilha.concatena_pilhas(uma_pilha, outra_pilha)
                        self.__lista_pilhas(self.__pilha)
                        self.__pilha_atual = self.__total_pilhas
                        pass
                    
                    case 'n':
                        self.__pilha = self.__selecionar_pilha(pilha_1)
                        self.__atualizar_pilha_atual(pilha_1)
                        self.__pilha.concatena(outra_pilha)
                
                os.system('cls')
                print(f'As pilhas {pilha_1} e {pilha_2} foram concatenadas.')
                time.sleep(3)
                os.system('cls')
            
            case '10':
                try:
                    os.system('cls')
                    pilha = int (input('Selecione a pilha: '))
                except:
                    os.system('cls')
                    print(f'Você precisa escolher um número entre 1 e o total de pilhas ({self.__total_pilhas}).')
                    time.sleep(3)
                    os.system('cls')
                    return
                if pilha < 1 or pilha > self.__total_pilhas:
                    os.system('cls')
                    print(f'Você precisa escolher um número entre 1 e o total de pilhas ({self.__total_pilhas}).')
                    time.sleep(3)
                    os.system('cls')
                    return
                self.__pilha = self.__selecionar_pilha(pilha)
                self.__atualizar_pilha_atual(pilha)
                os.system('cls')
                print(f'A pilha {pilha} foi selecionada.')
                time.sleep(3)
                os.system('cls')
            
            case '11':
                try:
                    os.system('cls')
                    numero = int (input('Digite um número inteiro para convertê-lo ao sistema binário: '))
                    time.sleep(3)
                    os.system('cls')
                except:
                    os.system('cls')
                    print('Você deve digitar um número inteiro para realizar a conversão.')
                    time.sleep(3)
                    os.system('cls')
                    return
                
                os.system('cls')
                print(f'{numero} é igual a {self.__dec_to_bin(numero)} no sistema binário.')
                time.sleep(3)
                os.system('cls')
            
            case '12':
                os.system('cls')
                print('Saindo.')
                time.sleep(3)
                os.system('cls')
            
            case _:
                os.system('cls')
                print('Opção inválida.')
                time.sleep(3)
                os.system('cls')
            
        self.__opcao = opcao

    def __exibir_menu(self):
        print(f'''
Editor de pilha v1.2
===================================
Pilha selecionada: {self.__pilha_atual} de {self.__total_pilhas} 
{self.__pilha} <- topo
===================================
(1) Empilhar
(2) Desempilhar
(3) Tamanho
(4) Obter elemento do topo
(5) Teste de pilha vazia
(6) Criar nova pilha
(7) Inverter os elementos da pilha
(8) Esvaziar a pilha
(9) Concatenar duas pilhas 
(10) Escolher outra pilha
(11) Conversão dec/bin
(12) Sair
===================================''')
        opcao = input('Digite sua opção: ')
        print()
        
        self.__processar_opcao(opcao)

    def __lista_pilhas (self, pilha):
        no = self.__head_lista
        while no.proximo:
            no = no.proximo
        no.proximo = Node (pilha)
        self.__total_pilhas += 1

    def __selecionar_pilha (self, index):
        no = self.__head_lista
        apontador = 1
        while no.proximo and apontador < index:
            no = no.proximo
            apontador += 1
        return no.valor
    
    def __atualizar_pilha_atual(self, index):
        self.__pilha_atual = index

    def __dec_to_bin(self, numero):
        if numero == 0:
            return '0'
        
        pilha = PilhaEncadeada()
        dividendo = numero
        divisor = 2

        while dividendo + 1 >= divisor:
            quociente = dividendo // divisor
            resultado = quociente * divisor
            resto = dividendo - resultado
            dividendo = quociente
            
            '''Restos das divisões sucessivas.'''
            pilha.empilhar(resto)
        
        conversao = ''
        for i in range(pilha.tamanho()):
            conversao += f'{pilha.desempilhar()}'

        return conversao

    def iniciar(self):
        self.__exibir_menu()
        return self.__opcao

main = Main()      
while True:
    if main.iniciar() == '12':
        break