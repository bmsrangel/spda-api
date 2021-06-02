from math import pi
from mpmath import ln
from csv import reader


def calc_rho_h(resistividade_camada1, resistividade_camada2):
    razao = resistividade_camada2 / resistividade_camada1
    mi = 0
    with open('permissividade.csv', newline='') as permissividades:
        spamreader = reader(permissividades)
        table = []
        for row in spamreader:
            try:
                new_row = row[0].split(';')
                new_row[0] = float(new_row[0])
                new_row[1] = float(new_row[1])
                table.append(new_row)
            except:
                None
        for row in table:
            if (row[0] == round(razao, 1)):
                mi = row[1]
                break
    return round(mi * resistividade_camada1, 2)


def calc_alfa(comprimento_cabo, distancia_contrapesos, altura_camada1):
    a = 2 * comprimento_cabo * distancia_contrapesos
    r = 0.565 * pow(a, 0.5)
    alfa = r / altura_camada1
    return alfa


def calc_resistividade_aparente(resistividade_camada1, n):
    rho_a = n * resistividade_camada1
    return rho_a


def a_linha_4(raio, profundidade_instalacao, distancia_contrapesos):
    a_linha = pow((pow(2 * raio * profundidade_instalacao, 0.5) * pow((38*pow((4 *
                  pow(profundidade_instalacao, 2) + pow(distancia_contrapesos, 2)), 0.5)), 0.5)), 0.5)
    return a_linha


def a_linha_6(distancia_contrapesos_12, distancia_contrapesos_23, raio, profundidade_instalacao):
    distancia_contrapesos_13 = distancia_contrapesos_12 + distancia_contrapesos_23
    a_linha = pow(pow(2 * raio * profundidade_instalacao, 0.5) * pow((distancia_contrapesos_12 * pow((4 * pow(profundidade_instalacao, 2) + pow(distancia_contrapesos_12, 2)), 0.5)), 1/3) * pow((distancia_contrapesos_23 *
                  pow((4 * pow(profundidade_instalacao, 2) + pow(distancia_contrapesos_23, 2)), 0.5)), 1/3) * pow((distancia_contrapesos_13 * pow((4 * pow(profundidade_instalacao, 2) + pow(distancia_contrapesos_13, 2)), 0.5)), 1/3), 1/3)
    return a_linha


def resistencia(resistividade_aparente, comprimenro_cabo, a_linha):
    resistencia = resistividade_aparente / \
        (pi * comprimenro_cabo) * (ln(2 * comprimenro_cabo / a_linha) - 1)
    return resistencia
