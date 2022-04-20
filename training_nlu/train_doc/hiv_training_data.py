#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:09:25 2018

@author: justine
"""

import network as nw
#import scikit_learn as sl

question= [["what is HIV?"],["what is HIV aids?"],["what is the average survival time without treatment if affected by HIV?"],["how hiv transmitted from one person to another?"],["how hiv transmission on non-sexually?"],["how hiv transmit from mother to child?"],["how hiv present in body fluids in the form of?"],["where do hiv viruses infections?"],["how hiv infections leads to?"],["how HIV aids develop inside the body?"]]
selected_sentences_list= [["the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids).","without treatment, average survival time after infection with hiv is estimated to be 9 to 11 years, depending on the hiv subtype."]
                         ,["HIV aids is a condition in humans in which progressive failure of the immune system allows life-threatening opportunistic infections and cancers to thrive.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]
                         ,["without treatment, average survival time after infection with hiv is estimated to be 9 to 11 years, depending on the hiv subtype.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]
                         ,["in most cases, hiv is a sexually transmitted infection and occurs by contact with or transfer of blood, pre-ejaculate, semen, and vaginal fluids.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]
                         ,["non-sexual transmission of hiv can occur from an infected mother to her infant through breast milk.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]
                         ,["an hiv-positive mother can transmit hiv to her baby both during pregnancy and childbirth due to exposure to her blood or vaginal fluid.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]
                         ,["within these bodily fluids, hiv is present as both free virus particles and virus within infected immune cells.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]
                         ,["hiv infection vital cells in the human immune system such as helper t cells (specifically cd4+ t cells), macrophages, and dendritic cells.","hiv infection leads to low levels of cd4+ t cells through a number of mechanisms, including pyroptosis of abortively infected t cells, apoptosis of uninfected bystander cells, direct viral killing of infected cells, and killing of infected cd4+ t cells by cd8+ cytotoxic lymphocytes that recognize infected cells."]
                         ,["hiv infection leads to low levels of cd4+ t cells through a number of mechanisms, including pyroptosis of abortively infected t cells, apoptosis of uninfected bystander cells, direct viral killing of infected cells, and killing of infected cd4+ t cells by cd8+ cytotoxic lymphocytes that recognize infected cells.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]
                         ,["when cd4+ t cell numbers decline below a critical level, cell-mediated immunity is lost, and the body becomes progressively more susceptible to opportunistic infections, leading to the development of aids.","the human immunodeficiency virus (hiv) is a lentivirus (a subgroup of retrovirus) that causes hiv infection and over time acquired immunodeficiency syndrome (aids)."]]
                         

for i in range (0, len(question)):
    
    array=nw.question_answer_nurel_network(question[i],selected_sentences_list[i])
#answer= nw.question_answer_nurel_network(question,selected_sentences_list)
#print(answer)
print("array= " +str(array))

#net=sl.learn(array)
#sl.save_perceptron(net)

