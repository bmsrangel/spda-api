from functions import a_linha_4, a_linha_6, calc_resistividade_aparente, calc_rho_h, resistencia
from os import system

# Dados do projeto
comprimento_contrapeso = 16
raio = 0.00259
profundidade_instalacao = 0.4
distancia_contrapesos = 38

distancia_contrapesos_12 = 19
distancia_contrapesos_23 = 19

# Valores medidos com as hastes
resistividade_camada1 = 1661
resistividade_camada2 = 2553

# Valores obtidos por análise gráfica
altura_camada1 = 4
n = 1.3


def calculo_resistencia(descricao):
    if (descricao != None):
        print(descricao)
    rho_h = calc_rho_h(resistividade_camada1, resistividade_camada2)
    print(f'Resistividade em função da altura: {rho_h}')
    resistividade_aparente = calc_resistividade_aparente(
        altura_camada1, resistividade_camada1, comprimento_contrapeso, distancia_contrapesos, n)
    print(f'Resistividade aparente (pa): {resistividade_aparente}')
    a_linha = a_linha_4(raio, profundidade_instalacao, distancia_contrapesos)
    print(f'Valor a\': {a_linha}')
    resistencia_final = resistencia(resistividade_aparente,
                                    comprimento_contrapeso, a_linha)
    print(
        f'Resistência final do arranjo (4 fios, {comprimento_contrapeso}m): {resistencia_final}\n\n')


def calculo_resistencia_6(descricao):
    if (descricao != None):
        print(descricao)
    rho_h = calc_rho_h(resistividade_camada1, resistividade_camada2)
    print(f'Resistividade em função da altura: {rho_h}')
    resistividade_aparente = calc_resistividade_aparente(
        altura_camada1, resistividade_camada1, comprimento_contrapeso, distancia_contrapesos, n)
    print(f'Resistividade aparente (pa): {resistividade_aparente}')
    a_linha = a_linha_6(distancia_contrapesos_12,
                        distancia_contrapesos_23, raio, profundidade_instalacao)
    print(f'Valor a\': {a_linha}')
    resistencia_final = resistencia(resistividade_aparente,
                                    comprimento_contrapeso, a_linha)
    print(
        f'Resistência final do arranjo (6 fios, {comprimento_contrapeso}m): {resistencia_final}\n\n')


system('cls')
# teste 1
calculo_resistencia('Teste 1')

# teste 2 - aumento na distância entre contrapesos
distancia_contrapesos = 39
calculo_resistencia(
    'Teste 2 - aumento na distância entre contrapesos para 39m')

# teste 3 - aumento no comprimento dos contrapesos para 40m
distancia_contrapesos = 38
comprimento_contrapeso = 40
n = 1.4
calculo_resistencia(
    'Teste 3 - aumento no comprimento dos contrapesos para 40m')

# teste 4 - aumento no comprimento dos contrapesos para 80m
comprimento_contrapeso = 80
n = 1.5
calculo_resistencia(
    'Teste 4 - aumento no comprimento dos contrapesos para 80m')

# teste 5 - aumento no comprimento dos contrapesos para 150m
comprimento_contrapeso = 150
n = 1.2
calculo_resistencia(
    'Teste 5 - aumento no comprimento dos contrapesos para 150m')

# teste 6 - 6 contrapesos, dados iniciais
comprimento_contrapeso = 16
n = 1.3
calculo_resistencia_6('Teste 6 - 6 contrapesos, dados iniciais')

# teste 7 - 6 contrapesos, comprimento em 40m
comprimento_contrapeso = 40
n = 1.4
calculo_resistencia_6('Teste 7 - 6 contrapesos, comprimento em 40m')

# teste 8 - 6 contrapesos, comprimento em 80m
comprimento_contrapeso = 80
n = 1.5
calculo_resistencia_6('Teste 8 - 6 contrapesos, comprimento em 80m')

# teste 9 - 6 contrapesos, comprimento em 150m
comprimento_contrapeso = 150
n = 1.2
calculo_resistencia_6('Teste 9 - 6 contrapesos, comprimento em 150m')
