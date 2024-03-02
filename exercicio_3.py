# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:47:10 2024

@author: miche
"""

import pytest


def numeros(n1, n2):
    valor_produto = n1
    valor_desconto = n2
    
    return round(valor_produto - valor_desconto, 2)