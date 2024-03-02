# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:51:26 2024

@author: miche
"""

import pytest

from exercicio_3 import numeros

def test_calc_ex3_1():
    assert numeros(500, 50) == pytest.approx(450.00)
    
def test_calc_ex3_2():
    assert numeros(10500, 500) == pytest.approx(10000.00)
    
def test_calc_ex3_3():
    assert numeros(90, 0.80) == pytest.approx(89.20)