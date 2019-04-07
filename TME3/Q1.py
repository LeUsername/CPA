#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:00:00 2019

@author: 3410456
"""
import matplotlib.pyplot as plt
def size(nom):
    noeud=set()
    f = open(nom, "r")
    i=0
    for n in f:
        buff=n.split()
        if(buff!=[]):
            for e in buff:
               noeud.add(e)
            i=i+len(buff)-1
    return len(noeud)
    
#size("/Vrac/TME_CPA_19-02-20/com-amazon.ungraph.txt")    

def clean(nom):
    f = open(nom, "r")
    noeud = dict()
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
    f.close()
    f = open("nouveauNoeud", "a")
    for (k,v) in noeud.items():
        if(len(v)==0):
            continue
        for valeur in v:
            f.write(k + " ")
            f.write(valeur + "\n")
    f.close()            
    
# clean("/Vrac/TME_CPA_19-02-20/com-amazon.ungraph.txt")

def degre(nom):
    f = open(nom, "r")
    noeud = dict()
    for n in f:
        buff=n.split()
        if(buff!=[]):
             s=len(buff)
             for i in range (0,s-1):
                 if(buff[i] != buff[i+1]):
                     if ((buff[i] in noeud)==False):
                         noeud[buff[i]]=0
                     if ((buff[i+1] in noeud)==False):
                         noeud[buff[i+1]]=0
                     a=noeud.get(buff[i])
                     noeud[buff[i]]=a+1
                     noeud[buff[i+1]]=noeud.get(buff[i+1])+1
    return noeud

#print(degre("/Vrac/TME_CPA_19-02-20/email-Eu-core-clean.txt"))

def quantity(nom):
    p=degre(nom)
    print (p)
    somme=0
    f = open(nom, "r")
    for n in f:
        buff=n.split()
        if(buff!=[]):
             s=len(buff)
             for i in range (0,s-1):
                 if(buff[i] != buff[i+1]):
                     somme+=p[buff[i]]*p[buff[i+1]]
    return somme

def p(nom):
    p=degre(nom)
    noeud = dict()
    for (k,v) in p.items():

        if ((v in noeud)==False):
            noeud[v]=0
        noeud[v]=noeud[v]+1
    
    x = list()
    y = list()
    for (k,v) in noeud.items():
        x.append(k)
        y.append(v)
    plt.ylabel("nb noeuds")
    plt.xscale("log")
    plt.xlabel("degre")
    plt.yscale("log")
    plt.scatter(x, y)
    plt.show()
    return noeud
#print (p('/Vrac/TME_CPA_19-02-20/com-amazon.ungraph-clean.txt'))            