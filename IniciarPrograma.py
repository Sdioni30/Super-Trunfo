import time
from MostrarCartas import MostrarCartas
from ListaCarrosEsportivos import CarrosEsportivos
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class FuncaoDeIniciarPrograma:
    def __init__(self):
        self.carros_esportivos = CarrosEsportivos()
        self.mostrarcartas = MostrarCartas(self.carros_esportivos.carros)
        self.usuarios = self.mostrarcartas.mostrar_qtdd_de_cartas()
        self.usuario1 = self.usuarios[0]
        self.usuario2 = self.usuarios[1]


    def main(self):
        while True:
            self.carros_esportivos.exibir_nome_do_jogo()
            self.carros_esportivos.exibir_menu()
            try:
                pergunta = int(input('Escolha uma opção: '))
            except ValueError:
                print("Digite apenas números!")
                time.sleep(2)
                limpar_tela()
                continue

            if pergunta == 1:
                print('Você escolheu Jogar: \n')
                time.sleep(2)
                self.carros_esportivos.receber_carro_aleatorio()
                time.sleep(2)
                limpar_tela()
            elif pergunta == 2:
                self.mostrarcartas.listar_carros()
                self.carros_esportivos.voltar_menu()
                limpar_tela()
            elif pergunta == 3:
                print(f"\033[94m Quantidade de carros para escolher no jogo: {len(self.carros_esportivos.carros)}\033[0m\n")
                time.sleep(3)
                limpar_tela()
            elif pergunta == 4:
                self.mostrarcartas.listar_cartas_usuario1()
                self.mostrarcartas.listar_cartas_usuario2()
                time.sleep(5)
                limpar_tela()
            elif pergunta == 5:
                self.mostrarcartas.mostrar_qtdd_de_cartas()
                time.sleep(5)
                limpar_tela()
            elif pergunta == 6:
                print('Obrigado por jogar, volte sempre: ')
                self.carros_esportivos.finalizar_app()
            else:
                self.carros_esportivos.opcao_invalida()
                limpar_tela()