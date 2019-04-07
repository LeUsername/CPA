#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:47:25 2019

@author: 3410456
"""

import random #, matplotlib.pyplot as plt, networkx as nx
import Q1,Q2
import time
def graphe(p, q):
    res = dict()
    G = []
    i = 0
    f = open("TEST", "w+")
    for i in range (0, 400):
        res[i]=set()

    for i in range (0, 400):
        for j in range(i+1, 400):
            if(i!=j):
                if(i < 100):
                    if(j<100):
                        if(random.uniform(0,1)<=p):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
                    else:
                        if(random.uniform(0,1)<=q):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
                if(i >= 100 and i<200):
                    if(j >= 100 and j<200):
                        if(random.uniform(0,1)<=p):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
                    else:
                        if(random.uniform(0,1)<=q):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
   
                if(i >= 200 and i<300):
                   if(j >= 200 and j<300):
                        if(random.uniform(0,1)<=p):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
                   else:
                        if(random.uniform(0,1)<=q):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
                if(i >= 300 ):
                    if(j>=300):
                        if(random.uniform(0,1)<=p):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
                    else:
                        if(random.uniform(0,1)<=q):
                            res[i].add(j)
                            res[j].add(i)
                            G.append((i, j))
                            f.write(str(i))
                            f.write(" ")
                            f.write(str(j))
                            f.write("\n")
    f.flush()
    f.close()
    return res, G

#g = graphe(0.3,0.0025)
"""nx.draw(g[1], node_size=5)
plt.draw()"""


def Intersection(A,B):
    c=[]
    if (len (B)>=len(A)):
        for i in A:
            if (i in B):
                c.append(i)
        return c
    else:
        for i in B:
            if (i in B):
                c.append(i)
        return c
def listeVoisin(G,A):
    voisin=set()
    print (A)
    for i in A:
        #print (i)
        for e in G[i]:
            voisin.add(e)
    return voisin
    
def Jaccard(G,A,B):
    if(A is None or B is None):
        return -1
    seta=listeVoisin(G,A)
    setb=listeVoisin(G,B)
    inter=Intersection(seta,setb)
    a=0.0
    a=inter/(len(A)+len(B)-inter )
    return a

def aggloJaccard(A):
    c=[]
    maxJ=0
    maxA=0
    maxB=1
    for a in A.keys():
        c.append(a)
    while (len(c)>4):
        for i in range(0,len(c)):
            for j in range(i,len(c)):
                if ((i!=j)):
                    current=Jaccard(A,c[i],c[j])
                    if(current>maxJ):
                        maxJ=current
                        maxA=i
                        maxB=j
        c[maxA]=c[maxA]+c[maxB]
        c[maxB]=None
    return c
    

def frequence(reseau, indice, label):
    labelOccurence = dict()
    for i in reseau[indice]:
        labelCourant = label[i]
        if(labelCourant not in labelOccurence):
            labelOccurence[labelCourant] = 0
        labelOccurence[labelCourant] += 1
    labelMax = max(labelOccurence.keys(), key=(lambda k: labelOccurence[k]))
    return labelMax


        
def labelPropagation(reseau):
    label = []
    labelstop=dict()
	
    for i in reseau.keys():
        label[i]=i
    while( labelstop!=label):
        labelstop=label
        r=[]
        for i in reseau.keys():
            r.append(i)
        random.shuffle(r)
        for i in r:
            label[i] = frequence(reseau, i, label)
    return label
print ("zeojij")
liste_c=['red','blue','yellow','green','pink','purple','black','white','grey','brown']
couleur=dict()
c=0
print ("yo")
t1 = time.time()
z=Q2.liste_a_symetrique("data3")
#♥z1=Q2.liste("data")
label=aggloJaccard(z.listeAdjacence)
print (time.time()-t1)
e=dict()
for er in label:
    e[label[er]]=0
for er in label:
    e[label[er]]+=1
print (len(e.keys()))

for i in label:
    if (label[i] not in couleur):
        couleur[label[i]]=c
        c+=1
lcn=[]
ln=[]
for i in label:
    lcn.append(couleur[label[i]])
    ln.append(i)
G=nx.Graph()
G.add_nodes_from(ln)

G.add_edges_from(z1)
nx.draw(G,nodelist=ln,node_color=lcn,node_size=5)



