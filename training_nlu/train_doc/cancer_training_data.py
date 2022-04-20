#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:09:25 2018

@author: justine
"""

import network as nw
#import scikit_learn as sl

question= [["what is cancer?"],["what are the possible signs and symptoms of cancer?"],["how many types of cancers can affect human?"],["what causes to cancer deaths mainly?"],["what are the other causes of cancer?"],["what are the other factors of cancer?"],["what about cancer in the developing countries?"]
,["does genetic issues cause cancer? "],["how can cancer be detected?"],["how to prevent cancer?"],["how cancer is often treated?"],["what are the important part of cancer care?"],["what about palliative cancer care?"],["what about the chances of survival of cancer?"]
,["how much cancer survival in children?"],["how much cancer survival in united states?"],["how many people had cancer in 2015?"],["around how many people died of cancer?"],["which is the common cancer seen in males?"],["which is the common cancer seen in females?"],["which is the common cancer seen in children?"],["about how many children where affected by cancer?"],["why the cancer rates are increasing?"],["how much is the financial costs of cancer estimated?"]]
selected_sentences_list= [["cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body.","over 100 types of cancers affect humans."]
                         ,["possible signs and symptoms include a lump, abnormal bleeding, prolonged cough, unexplained weight loss and a change in bowel movements.","cancer can be detected by certain signs and symptoms or screening tests."]
                         ,["over 100 types of cancers affect humans.","in the developing world, 15% of cancers are due to infections such as helicobacter pylori, hepatitis b, hepatitis c, human papillomavirus infection, epstein–barr virus and human immunodeficiency virus (hiv)."]
                         ,["tobacco use is the cause of about 22% of cancer deaths.","it caused about 8.8 million deaths (15.7% of deaths)."]
                         ,["other causes of cancer 10% are due to obesity, poor diet, lack of physical activity or excessive drinking of alcohol.","tobacco use is the cause of about 22% of cancer deaths."]
                         ,["other factors include certain infections, exposure to ionizing radiation and environmental pollutants.","cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body."]
                         ,["in the developing world, 15% of cancers are due to infections such as helicobacter pylori, hepatitis b, hepatitis c, human papillomavirus infection, epstein–barr virus and human immunodeficiency virus (hiv).","typically, many genetic changes are required before cancer develops."]
                         ,["approximately 5–10% of cancers are due to inherited genetic defects from a person's parents.","tobacco use is the cause of about 22% of cancer deaths."]
                         ,["cancer can be detected by certain signs and symptoms or screening tests.","early detection through screening is useful for cervical and colorectal cancer."]
                         ,["many cancers can be prevented by not smoking, maintaining a healthy weight, not drinking too much alcohol, eating plenty of vegetables, fruits and whole grains, vaccination against certain infectious diseases, not eating too much processed and red meat and avoiding too much sunlight exposure.","cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body."]
                         ,["cancer is often treated with some combination of radiation therapy, surgery, chemotherapy and targeted therapy.","in children, acute lymphoblastic leukemia and brain tumors are most common cancers, except in africa where non-hodgkin lymphoma occurs more often."]
                         ,["pain and symptom management are an important part of care.","cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body."]
                         ,["palliative care is particularly important in people with advanced disease.","cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body."]
                         ,["chance of survival depends on the type of cancer and extent of disease at the start of treatment.","for cancer in the united states, the average five-year survival rate is 66%."]
                         ,["in children under 15 at diagnosis, the five-year survival rate in the developed world is on average 80%.","many cancers can be prevented by not smoking, maintaining a healthy weight, not drinking too much alcohol, eating plenty of vegetables, fruits and whole grains, vaccination against certain infectious diseases, not eating too much processed and red meat and avoiding too much sunlight exposure."]
                         ,["for cancer in the united states, the average five-year survival rate is 66%.","many cancers can be prevented by not smoking, maintaining a healthy weight, not drinking too much alcohol, eating plenty of vegetables, fruits and whole grains, vaccination against certain infectious diseases, not eating too much processed and red meat and avoiding too much sunlight exposure."]
                         ,["in 2015, about 90.5 million people had cancer.","typically, many genetic changes are required before cancer develops."]
                         ,["it caused about 8.8 million died of cancer (15.7% of deaths).","typically, many genetic changes are required before cancer develops."]
                         ,["the most common types of cancer in males are lung, prostate, colorectal and stomach .","in females, the most common types are breast, colorectal, lung and cervical cancer."]
                         ,["in females, the most common types are breast, colorectal, lung and cervical cancer.","the most common types of cancer in males are lung, prostate, colorectal and stomach ."]
                         ,["in children, acute lymphoblastic leukemia and brain tumors are most common cancers, except in africa where non-hodgkin lymphoma occurs more often.","the most common types of cancer in males are lung, prostate, colorectal and stomach ."]
                         ,["in 2012, about 165,000 children under 15 years of age were diagnosed with cancer.","over 100 types of cancers affect humans."]
                         ,["rates are increasing as more people live to an old age and as lifestyle changes occur in the developing world.","for cancer in the united states, the average five-year survival rate is 66%."]
                         ,["financial costs of cancer were estimated at $1.16 trillion usd per year as of 2010.","many cancers can be prevented by not smoking, maintaining a healthy weight, not drinking too much alcohol, eating plenty of vegetables, fruits and whole grains, vaccination against certain infectious diseases, not eating too much processed and red meat and avoiding too much sunlight exposure."]]

for i in range (0, len(question)):
    
    array=nw.question_answer_nurel_network(question[i],selected_sentences_list[i])
#answer= nw.question_answer_nurel_network(question,selected_sentences_list)
#print(answer)
print("array= " +str(array))

#net=sl.learn(array)
#sl.save_perceptron(net)

