# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:36:46 2024

@author: miche
"""

## EXERCICIO 2 
import pytest

def calc_desconto(valor_produto, valor_desconto):
    total_desc = valor_produto * (valor_desconto / 100)
    total = valor_produto - total_desc
    return round(total, 2)

