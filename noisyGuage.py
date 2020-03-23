#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:59:40 2019

@author: coleconstantino
"""
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

G = BayesianModel([('B', 'G'),( 'F', 'G')])
cpd_B = TabularCPD(variable = 'B', variable_card = 2, values = [[0.8,0.2]], state_names = {'B' : ['1','0']})


cpd_F = TabularCPD(variable = 'F', variable_card = 2, values = [[0.9,0.1]], state_names = {'F' : ['1','0']})


cpd_G = TabularCPD(variable = 'G', variable_card = 2, values = [[0.1,0.2,0.1,0.9],
                                                                [0.9,0.8,0.9,0.1]
                                                                ],
                                                                evidence = ['B','F'], 
                                                                evidence_card = [2, 2],
                                                                state_names = {'G': ['1','0'],
                                                                               'B' : ['1','0'],
                                                                               'F' : ['1','0']})

G.add_cpds(cpd_B, cpd_F, cpd_G)


infer = VariableElimination(G)
#g_dist = infer.query(['F'], evidence={'G': '0'})
one_dist = infer.query(['F'])
two_dist = infer.query(['F'], evidence={'G': '0'})
three_dist = infer.query(['F'], evidence={'G': '0','B': '0'})

onlyb_dist = infer.query(['F'], evidence={'B': '0'})
print(onlyb_dist)
