# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:00:22 2024

@author: miche
"""

import pytest

from restaurante import taxa_servico

def test_cal_taxa_1():
    assert taxa_servico(75.00, 10) == pytest.approx(82.50)
    
def test_cal_taxa_2():
    assert taxa_servico(125, 10) == pytest.approx(137.50)
    
def test_cal_taxa_3():
    assert taxa_servico(350.87, 10) == pytest.approx(385.96)