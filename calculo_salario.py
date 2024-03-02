# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:15:09 2024

@author: miche
"""

import pytest as py

##  EXERCICIO 1 

def calc_salario (aula_hora, n_aula, perc):
    x = perc / 100
    valor = n_aula * aula_hora
    desconto = valor * x
    return round(valor - desconto, 2)



