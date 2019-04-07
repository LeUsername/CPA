#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:31:55 2019

@author: 3410456
"""

import Q1, queue

class listeAdjacence:
    def __init__(self, taille, aretes, listeAdjacence):
        self.listeAdjacence = listeAdjacence
        self.taille = taille
        self.aretes = aretes

def liste(nom):
    f = open(nom, "r")
    s = list()
    for n in f:
        buff=n.split()
        if(buff!=[]):
             s.append(buff)
    f.close()
    return s

def adjacence(nom):
    f = open(nom, "r")
    n = Q1.degre(nom)
    s = dict()
    for (k,v) in n.items():
        for (i,j) in n.items():
            s[(k,i)]=0
    for n in f:
        buff=n.split()
        
        if(buff!=[]):
             s[(buff[0],buff[1])]=1
             s[(buff[1],buff[0])]=1
    f.close()
    return s
    
#print (adjacence("TEST"))

def liste_a(nom):
    f = open(nom, "r")
    noeud = dict()
    cptArete = 0
    for n in f:
        buff=n.split()
        if(buff!=[]):
             s=len(buff)
             for i in range (0,s-1):
                 if(buff[i] != buff[i+1]):
                     if ((buff[i] in noeud)==False):
                         noeud[buff[i]]=set()
                     if ((buff[i+1] in noeud)==False):
                         noeud[buff[i+1]]=set()
                     if  ( (buff[i] in noeud.get(buff[i+1]) ) ==False ):
                         noeud.get(buff[i]).add(buff[i+1])
                         cptArete += 1
    f.close()
    return listeAdjacence(len(noeud.keys()), cptArete, noeud)

def liste_a_symetrique(nom):
    f = open(nom, "r")
    noeud = dict()
    cptArete = 0
    for n in f:
        buff=n.split()
        if(buff!=[]):
             s=len(buff)
             for i in range (0,s-1):
                 if(buff[i] != buff[i+1]):
                     if ((buff[i] in noeud)==False):
                         noeud[buff[i]]=set()
                     if ((buff[i+1] in noeud)==False):
                         noeud[buff[i+1]]=set()
                     if  ( (buff[i] in noeud.get(buff[i+1]) ) ==False ):
                         noeud.get(buff[i]).add(buff[i+1])
                         noeud.get(buff[i+1]).add(buff[i])
                         cptArete += 1
    f.close()
    return listeAdjacence(len(noeud.keys()), cptArete, noeud)

def BFS(G, s, res = set()):
    fifo = queue.Queue(G.taille)
    fifo.put(str(s))
    mark=set()
    mark.add(str(s))
    while(not fifo.empty()):
        u = fifo.get(0)
        res.add(u)
        for v in G.listeAdjacence[u]:
            if((v in mark )==False):
                fifo.put(v)
                mark.add(v)
    return res

#BFS(liste_a("TEST"), 1)

def BFSTousLesSommets(nom):
    res = dict()
    G = liste_a_symetrique(nom)
    sommetsDejaVisite = set()
    for v in G.listeAdjacence:
        if(v in sommetsDejaVisite):
            continue
        if(v not in res):
            res[v] = set()
        #BFS(G, v, res[v])
        fifo = queue.Queue(G.taille)
        fifo.put(str(v))
        mark=set()
        mark.add(str(v))
        sommetsDejaVisite.add(str(v))
        while(not fifo.empty()):
            u = fifo.get(0)
            res[v].add(u)
            for w in G.listeAdjacence[u]:
                if((w in mark )==False):
                    fifo.put(w)
                    mark.add(w)
                    sommetsDejaVisite.add(str(w))
    return res
#print(BFSTousLesSommets("TEST"))

def Diametre(nom, sommetBase, nbIter):
    sommetMax = sommetBase
    i = 0
    poidsMax = 0
    while(i < nbIter):
        G = liste_a_symetrique(nom)
        fifo = queue.Queue(G.taille)
        fifo.put((sommetMax,0))
        poids = dict()
        mark=set()
        mark.add(str(sommetMax))
        poids[0] = set()
        poids[0].add(sommetMax)
        while(not fifo.empty()):
            u = fifo.get(0)
            for v in G.listeAdjacence[u[0]]:
                if v not in mark:
                    if(u[1]+1 not in poids):
                        poids[u[1]+1] = set()
                        poids[u[1]+1].add(v)
                    elif(poids[u[1]+1] != set()):
                        poids[u[1]+1].add(v)
                    fifo.put((v,u[1]+1))
                    mark.add(v)
        poidsMaxCourant = max(poids.keys())
        if(poidsMaxCourant > poidsMax):
            poidsMax = poidsMaxCourant
            sommetMax = poids[poidsMax].pop()
        i +=1
    return sommetMax, poidsMax

#print(Diametre('/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt','1',1))