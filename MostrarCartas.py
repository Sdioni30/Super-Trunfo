import random
import locale
import os


locale.setlocale(locale.LC_ALL, 'pt_BR')

class MostrarCartas:
    def __init__(self, carros):
        self.carros = carros.copy()
        random.shuffle(self.carros)
        self.usuario1 = self.carros[:len(self.carros)//2]
        self.usuario2 = self.carros[len(self.carros)//2:]

    def mostrar_qtdd_de_cartas(self):
        print(f'Usuário 1: {len(self.usuario1)} cartas')
        print(f'Usuário 2: {len(self.usuario2)} cartas')
        return self.usuario1, self.usuario2

    def listar_cartas_usuario1(self):
        print('\n')
        print("\033[94mO usuário 1 tem os seguintes carros: \n\033[0m")
        for carro in self.usuario1:
            print(f'{carro}\n')

    def listar_cartas_usuario2(self):
        print('\n')
        print("\033[94mO usuário 2 tem os seguintes carros: \n\033[0m")
        for carro in self.usuario2:
            print(f'{carro}\n')

    def listar_carros(self):
        print(f"{'NOME'.ljust(100)} | {'ANO'.ljust(15)} | {'VELOCIDADE'.ljust(15)} | VALOR")
        for carro in self.carros:
            print(f"{carro[0].ljust(100)} | {str(carro[1]).ljust(15)} | {str(carro[2]).ljust(15)} | {float(carro[3]):,}")






