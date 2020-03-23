#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:21:07 2019

@author: coleconstantino
"""

from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

G = BayesianModel([('A', 'L'),( 'D', 'L'),('L', 'B'),('M', 'B')])

cpd_A = TabularCPD(variable = 'A', variable_card = 2, values = [[0.2,0.8]], state_names = {'A' : ['1','0']})
cpd_D = TabularCPD(variable = 'D', variable_card = 2, values = [[0.3,0.7]], state_names = {'D' : ['1','0']})
cpd_M = TabularCPD(variable = 'M', variable_card = 2, values = [[0.1,0.9]], state_names = {'M' : ['1','0']})

#combat Level
cpd_L = TabularCPD(variable = 'L', variable_card = 2, values = [[0,0,0,1],
                                                                [1,1,1,0]
                                                                ],
                                                                evidence = ['A','D'], 
                                                                evidence_card = [2, 2],
                                                                state_names = {'L': ['1','0'],
                                                                               'A' : ['1','0'],
                                                                               'D' : ['1','0']})
#Boss capabilites
cpd_B = TabularCPD(variable = 'B', variable_card = 2, values = [[0.01,0.45,0.28,0.95],
                                                                [0.99,0.55,0.72,0.05]
                                                                ],
                                                                evidence = ['L','M'], 
                                                                evidence_card = [2, 2],
                                                                state_names = {'B': ['1','0'],
                                                                               'L' : ['1','0'],
                                                                               'M' : ['1','0']})

G.add_cpds(cpd_A, cpd_D, cpd_M, cpd_L, cpd_B)


infer = VariableElimination(G)
l_dist = infer.query(['L'])
b_dist = infer.query(['B'])
ex1_dist = infer.query(['B'], evidence={'L': '0','M': '0'})
ex2_dist = infer.query(['B'], evidence={'L': '0','M': '1'})
ex3_dist = infer.query(['B'], evidence={'L': '1','M': '0'})
ex4_dist = infer.query(['B'], evidence={'L': '1','M': '1'})

print(l_dist)
print()
print(b_dist)
print()
print(ex1_dist)
print()
print(ex2_dist)
print()
print(ex3_dist)
print()
print(ex4_dist)