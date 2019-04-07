#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:08:19 2019

@author: 3410456
"""

import Q1, Q2
import time
import queue
import matplotlib as plt

def quantityMesure(nom):
    temps_debut = time.time()
    p=Q1.degre(nom)
    somme=0
    f = open(nom, "r")
    for n in f:
        buff=n.split()
        if(buff!=[]):
             s=len(buff)
             for i in range (0,s-1):
                 if(buff[i] != buff[i+1]):
                     somme+=p[buff[i]]*p[buff[i+1]]
    return somme, time.time() - temps_debut
    
def plotMesure(nom):
    temps_debut = time.time()
    return Q1.p(nom), time.time() - temps_debut
    
def listeMesure(nom):
    temps_debut = time.time()
    return Q2.liste(nom), time.time() - temps_debut    
    
def adjacenceMesure(nom):
    temps_debut = time.time()
    return Q2.adjacence(nom), time.time() - temps_debut    
    
def liste_aMesure(nom):
    temps_debut = time.time()
    return Q2.liste_a(nom), time.time() - temps_debut  

def liste_a_symetriqueMesure(nom):
    temps_debut = time.time()
    return Q2.liste_a_symetrique(nom), time.time() - temps_debut      
    
def BFS(nom):
    temps_debut = time.time()
    bfs = Q2.BFSTousLesSommets(nom)
    maximum = 0
    for v in bfs.values():
        if(len(v)>maximum):
            maximum = len(v)
    return maximum, time.time() - temps_debut

def diametreMesure(nom, sommetBase, nbIter):
    temps_debut = time.time()
    return Q2.Diametre(nom, sommetBase, nbIter), time.time() - temps_debut
    
"""print (quantityMesure('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt'))
print (quantityMesure('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt'))
print (quantityMesure('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt'))
print (quantityMesure('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt'))
print (quantityMesure('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt'))"""

"""plotMesure('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt')
plotMesure('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt')
plotMesure('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt')
plotMesure('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt')
plotMesure('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt')"""

#print(listeMesure('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt')[1])
#print(listeMesure('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt')[1])
#print(listeMesure('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt')[1])
#print(listeMesure('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt')[1])
#print(listeMesure('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt')[1])

#print(adjacenceMesure('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt')[1])
#print(adjacenceMesure('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt')[1])
#print(adjacenceMesure('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt')[1])
#print(adjacenceMesure('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt')[1])
#print(adjacenceMesure('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt')[1])

"""print(liste_aMesure('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt')[1])
print(liste_aMesure('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt')[1])
print(liste_aMesure('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt')[1])
print(liste_aMesure('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt')[1])
print(liste_aMesure('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt')[1])"""

#print(liste_a_symetriqueMesure('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt')[1])
#print(liste_a_symetriqueMesure('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt')[1])
#print(liste_a_symetriqueMesure('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt')[1])
#print(liste_a_symetriqueMesure('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt')[1])
#print(liste_a_symetriqueMesure('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt')[1])

"""print(BFS('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt'))
print(BFS('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt'))
print(BFS('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt'))
print(BFS('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt'))
print(BFS('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt'))"""

print (diametreMesure('/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt','1',5))
print (diametreMesure('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt','1',3))
print (diametreMesure('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt','1',3))
print (diametreMesure('/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt','1',1))
print (diametreMesure('/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt','1',1))