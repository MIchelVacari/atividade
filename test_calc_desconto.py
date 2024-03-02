# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:35:53 2024

@author: miche
"""
import pytest

from calc_desconto import calc_desconto

def testa_desc_1():
    assert calc_desconto(100,9) == pytest.approx(91.00)
    
def testa_desc_2():
    assert calc_desconto(1500, 9) == pytest.approx(1365.00)
    
def testa_desc_3():
    assert calc_desconto(60000, 9) == pytest.approx(54600.00)
    