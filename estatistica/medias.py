import numpy as np

conjunto = [-9, 2, 2, 3, 4, 5, 5, 6, 7, 20]

def media(v):
    """Este é um cálculo geral de média.
    Sem considerar valores discrepantes"""
    return sum(v) / len(v)


med = media(conjunto)
print(f"Média geral: {med}")

"""Mas para podermos considerar a existências de overliers, teremos que calcular os quartis"""

"""Quartis são representações percentuais do conjunto dos dados"""

q1 = np.percentile(conjunto, 25)    # valores abaixo de 25% dos dados
q2 = np.percentile(conjunto, 50)    # valores abaixo de 50% dos dados
q3 = np.percentile(conjunto, 75)    # valores abaixo de 75% dos dados

"""Agora precisamos calcular o intervalo interquartis.
Que é o intervalo entre o menor quantil e o maior do conjunto de dados. """
iqr = q3 - q1

"""O IQR é importante para definirmos um limite superior e inferior para o conjunto de dados """
limite_superior = q3 + 1.5 * iqr
limite_inferior = q1 - 1.5 * iqr

"""Agora estamos aptos a identificar a existência de outliers"""
outliers = [x for x in conjunto if x < limite_inferior or x > limite_superior]

print(f"1° Quartil: {q1}")
print(f"2° Quartil: {q2}")
print(f"3° Quartil: {q3}")
print(f"IQR: {iqr}")
print(f"Limite superior: {limite_superior}")
print(f"Limite inferior: {limite_inferior}")
print(f"Outliers: {outliers}")

padroes = [x for x in conjunto if x not in outliers]
med_padroes = media(padroes)
print(f"Média sem outliers: {med_padroes}")
