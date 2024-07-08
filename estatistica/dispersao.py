import math

from algebra_linear import sum_of_squares
from medias import media

"""Dispersão se refere à medida de como nossos dados estão espalhados."""

conjunto = [-9, 2, 2, 3, 4, 5, 5, 6, 7, 20]
def amplitude(v):
    """A amplitude é zero quando o max e min são iguais, o que significa que os dados estão menos dispersos possível.
    Por outro lado, se a amplitude é ampla, significa que os dados estão mais espalhados"""
    return max(v) - min(v)


"""Uma medida de dispersão mais complexa é a variancia, computada desta forma:
    Variância=∑(vi - ˉvˉ)²/ n-1
"""
"""A variância é uma medida mais precisa de dispersão porque leva em conta o desvio de cada valor individual em relação 
à média do conjunto de dados.
    Então o valor da variância é proporcional à diferença entre os valores dos conjuntos"""


def de_mean(v):
    """Desloca v ao subtrair a sua média (então o resultado tem média 0)"""
    v_bar = media(v)
    return [v_i - v_bar for v_i in v]


def variance(v):
    """Presume que v tem ao menos dois elementos"""
    n = len(v)
    deviations = de_mean(v)
    return sum_of_squares(deviations) / (n - 1)


"""Desvio Padrão: O desvio padrão é a raiz quadrada da variância. Ele mede a quantidade média pela qual cada valor no 
    conjunto de dados se desvia da média do conjunto de dados."""


def standard_deviation(v):
    return math.sqrt(variance(v))


"""O desvio padrão é mais intuitivo do que a variância porque está na mesma unidade dos dados originais. 
    Por exemplo, se os dados estão em metros, o desvio padrão também estará em metros, enquanto a variância estará em 
    metros ao quadrado."""

if __name__ == "__main__":

    amp = amplitude(conjunto)
    print(f"Amplitude: {amp}")
    variancia = variance(conjunto)
    print(f"Variância: {variancia}")
    desvio_padrao = standard_deviation(conjunto)
    print(f"Desvio Padrão: {desvio_padrao}")
