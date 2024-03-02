# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:57:38 2024

@author: miche
"""

import pytest


def taxa_servico(valor_consumo, valor_taxa):
    valor_taxa_total = valor_consumo * (valor_taxa / 100)
    
    return round(valor_consumo + valor_taxa_total, 2)


    