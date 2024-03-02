# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:54:02 2024

@author: miche
"""

import pytest

from calculo_salario import calc_salario

def testa_salario_1():
    assert calc_salario(6.25, 160, 1.3) == pytest.approx(987.00)
    
def testa_salario_2(): 
    assert calc_salario(20.5, 240, 1.7) == pytest.approx(4836.36)
    
def testa_salario_3(): 
    assert calc_salario(13.9, 200, 6.48) == pytest.approx(2599.86) 
   


