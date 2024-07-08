import numpy as np

conjunto = [-9, 2, 2, 3, 4, 5, 5, 6, 7, 20]

def media(v):
    """Calcula a média de um conjunto de dados."""
    return sum(v) / len(v)


"""Mas para podermos considerar a existências de overliers, teremos que calcular os quartis"""

"""Quartis são representações percentuais do conjunto dos dados"""
def calcular_quartis(v):
    q1 = np.percentile(conjunto, 25)    # valores abaixo de 25% dos dados
    q2 = np.percentile(conjunto, 50)    # valores abaixo de 50% dos dados
    q3 = np.percentile(conjunto, 75)    # valores abaixo de 75% dos dados
    return q1, q2, q3


"""Agora precisamos calcular o intervalo interquartis.
Que é o intervalo entre o menor quantil e o maior do conjunto de dados. """
def identificar_outliers(v, q1, q3):
    iqr = q3 - q1

    """O IQR é importante para definirmos um limite superior e inferior para o conjunto de dados """
    limite_superior = q3 + 1.5 * iqr
    limite_inferior = q1 - 1.5 * iqr

    """Agora estamos aptos a identificar a existência de outliers"""
    outliers = [x for x in conjunto if x < limite_inferior or x > limite_superior]

    return outliers, limite_inferior, limite_superior


if __name__ == "__main__":

    # Calcular a média geral
    med = media(conjunto)
    print(f"Média geral: {med:.2f}")

    # Calcular os quartis
    q1, q2, q3 = calcular_quartis(conjunto)

    # Calcular o IQR e identificar outliers
    outliers, limite_inferior, limite_superior = identificar_outliers(conjunto, q1, q3)

    # Calcular a média sem outliers
    padroes = [x for x in conjunto if x not in outliers]
    med_padroes = media(padroes)

    # Exibir resultados
    print(f"1° Quartil (Q1): {q1:.2f}")
    print(f"2° Quartil (Mediana, Q2): {q2:.2f}")
    print(f"3° Quartil (Q3): {q3:.2f}")
    print(f"IQR: {q3 - q1:.2f}")
    print(f"Limite inferior: {limite_inferior:.2f}")
    print(f"Limite superior: {limite_superior:.2f}")
    print(f"Outliers: {outliers}")
    print(f"Média sem outliers: {med_padroes:.2f}")
