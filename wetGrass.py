#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:01:39 2019

@author: coleconstantino
"""

from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

G = BayesianModel([('R', 'G'),( 'S', 'G'),('R','J'),('S','J')])
cpd_B = TabularCPD(variable = 'R', variable_card = 2, values = [[0.2,0.8]], state_names = {'R' : ['1','0']})


cpd_F = TabularCPD(variable = 'S', variable_card = 2, values = [[0.1,0.9]], state_names = {'S' : ['1','0']})


cpd_G = TabularCPD(variable = 'G', variable_card = 2, values = [[0,0.95,1,1],
                                                                [1,0.05,0,0]
                                                                ],
                                                                evidence = ['R','S'], 
                                                                evidence_card = [2, 2],
                                                                state_names = {'G': ['1','0'],
                                                                               'R' : ['1','0'],
                                                                               'S' : ['1','0']})

cpd_J = TabularCPD(variable = 'J', variable_card = 2, values = [[0.15,0.15,1,1],
                                                                [0.85,0.85,0,0]
                                                                ],
                                                                evidence = ['R','S'], 
                                                                evidence_card = [2, 2],
                                                                state_names = {'J': ['1','0'],
                                                                               'R' : ['1','0'],
                                                                               'S' : ['1','0']})

G.add_cpds(cpd_B, cpd_F, cpd_G, cpd_J)


infer = VariableElimination(G)

one_dist = infer.query(['J'], evidence={'R': '0','S': '0'})
two_dist = infer.query(['J'], evidence={'R': '0','S': '1'})
three_dist = infer.query(['J'], evidence={'R': '1','S': '0'})
four_dist = infer.query(['J'], evidence={'R': '1','S': '1'})
final_dist = infer.query(['S'], evidence={'J': '1','G': '1'})

print(final_dist)

