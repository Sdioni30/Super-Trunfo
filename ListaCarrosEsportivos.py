import time
import random

class CarrosEsportivos:
    def __init__(self):
        self.carros = [
            ("GT-R R35", 2019, 320, 1274194),
            ("Hellcat", 2018, 300,1176000),
            ("SF90 Stradale", 2022, 340,5099316),
            ("Porsche 911 gt3 RS 4.0", 2023, 296,2260300),
            ("Lamborghini Sesto Elemento 5.2 V10", 2010, 350,16875826),
            ("Ferrari 488 Pista 3.9 V8 Turbo", 2019, 340,5037382),
            ("Audi RS 6 Avant 4.0 V8 TFSi", 2022, 250,1168576),
            ("Lamborghini Aventador SVJ 770-4 6.5 V12", 2022, 350,7536006),
            ("Honda Civic Hatch Type R 2.0", 2023, 275,429900),
            ("FORD KA SE Plus 1.5", 2020, 181,60758),
            ("Hyundai HB20 R espect 1.6 AT", 2019, 190,67267),
            ("Uno Mille Economy 1.0", 2012, 156,21338),
            ("Ford Maverick GT 4.9 V8", 1975, 182,241838),
            ("Chevrolet Opala cupê 2.5", 1979,155,25511),
            ("Ford Del Rey 1.6", 1984, 153,9542 ),
            ("Aston Martin Valkyrie 6.5 V12", 2024, 400,21500000),
            ("Mercedes-Benz AMG One 1.6 V6", 2022, 352,19764944),
            ("Koenigsegg One:1 5.0 V8", 2014, 440,11446213),
            ("Nissan Silvia S15", 1999, 260,270750),
            ("Dodge Challenger R/T 5.7 V8", 2015, 250,380000),
            ("Volkswagen Jetta GLi 2.0 TSi", 2024, 249,218010),
            ("Audi TT RS 2.5 TFSi Quattro", 2022, 280,615254),
            ("Mercedes-Benz CLA 45 S AMG 2.0 4Matic", 2024, 270,491396),
            ("Land Rover Evoque HSE Dynamic 2.0 Si4", 2024, 217,140733),
            ("Volkswagen Nivus Highline 1.0 TSi", 2024, 192,117704),
            ("Hyundai Veloster 1.6", 2013, 201,61075),
            ("Audi A3 Sportback Performance Preto 2.0 TFSi", 2024, 236,240420),
            ("Renault Kwid Zen 1.0", 2024, 156,53343),
            ("Fiat Mobi 1.0", 2024, 152,63990),
            ("Audi A3 1.8 Turbo", 2005, 217,32912),
            ("Hyundai Azera 3.0 V6", 2015, 235,85306),
            ("Hyundai Sonata", 2024, 240,200000),
            ("UP Move TSI", 2018, 181,57601)
        ]
        self.usuario1 = []
        self.usuario2 = []

    def voltar_menu(self):
        input("Digite algo para voltar ao menu: ")

    def opcao_invalida(self):
        print("Opção inválida, digite uma opção entre 1 e 6\n")
        input("Digite uma tecla para voltar ao menu principal")

    def exibir_nome_do_jogo(self):
        print("************** Super Trunfo ****************")

    def exibir_menu(self):
        print("Menu: \n")
        print("1- Jogar")
        print("2- Ver lista dos carros")
        print("3- Quantidade de carros listados")
        print("4 - Listar cartas de cada usuário: ")
        print("5- Ver cartas para cada usuário tem:")
        print("6- Sair do app")

    def finalizar_app(self):
        print("Finalizando app")
        exit()

    def receber_carro_aleatorio(self):
        try:
            recebe_carro_1, recebe_carro_2 = random.sample(self.carros, 2)
            print(f'Carro sorteado para o usuário 1: {recebe_carro_1[0]} ')
            time.sleep(2)
            print(f'Carro sorteado para o usuário 2: {recebe_carro_2[0]} \n')
            time.sleep(2)
            if recebe_carro_1[2] > recebe_carro_2[2]:
                vencedor = "Usuário 1"
                self.usuario1.append(recebe_carro_2)
            elif recebe_carro_1[2] < recebe_carro_2[2]:
                vencedor = "Usuário 2"
                self.usuario2.append(recebe_carro_1)
            else:
                print("Empate! Nenhum carro é transferido.")
                return
            print(f'{vencedor} venceu! \n{recebe_carro_1[0]} ({recebe_carro_1[2]} KM/H) vs {recebe_carro_2[0]} ({recebe_carro_2[2]} KM/H)')
            if recebe_carro_1[2] > recebe_carro_2[2]:
                print(f'Carros do Usuário 1: {self.usuario1}')
            else:
                print(f'Carros do Usuário 2: {self.usuario2}\n')
            self.voltar_menu()
        except ValueError as e:
            return f'Error {e}'