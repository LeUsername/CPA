#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:02:43 2019

@author: 3408751
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:44:23 2019

@author: 3410456
"""
"""TRouver le noeud de degré minimum
Faire uvec un tas min paire (idNoeud, degré)"""
import TasMinTableau as tasMin
import Q1, Q2
#import matplotlib.pyplot as plt
import operator
#import collections


def deg(nom):
    fichier = open(nom,"r")
    degre = dict()
    noeudMax = 0
    for ligne in fichier:
        s = ligne.split()
        entree = int(s[0])
        sortie = int(s[1])
        if(entree == sortie):
            if(entree not in degre):
                degre[entree] = 0
                if(entree>noeudMax):
                    noeudMax = entree
            degre[entree] += 2
        else:
            if(entree not in degre):
                degre[entree] = 0
                if(entree>noeudMax):
                    noeudMax = entree
            degre[entree] += 1
            if(sortie not in degre):
                degre[sortie] = 0
                if(sortie>noeudMax):
                    noeudMax = sortie
            degre[sortie] += 1
    fichier.close()
    return degre



def denset2(coreD1,A):
    delationLogique=dict()
    coreD=coreD1[0]
    coreD = sorted(coreD.items(), key=operator.itemgetter(0))
    ordre=[]
    f=coreD1[1]
    #print (coreD)
    for i in coreD:
     #   if (i[1][1]==731):
     #       print (i)
        ordre.append(i[1][1])
    #print (A.listeAdjacence["731"])
    for j in A.listeAdjacence.keys():
        delationLogique[j]=0  
    k=[]
    d=-1
    nbA=0.0
    indice=-1
    deg=0.0
    degf=0.0
    for c in ordre:
        delationLogique[c]=1
        for i in A.listeAdjacence[str(c)]:

            if (delationLogique[i]==1):
                nbA+=1
        k.append(str(c))
        deg=deg+f[c]
        if((nbA/len(k))>d):
            d=(nbA/len(k))
            degf=deg
            indice=c
    degf=degf/float(indice)
    degf=degf/2.0
    return  d,indice,degf/2,(2*degf/(indice*(indice-1)))

def denset(coreD1,A):
    delationLogique=[]
    coreD=coreD1[0]
    f=coreD1[1]
    coreD = sorted(coreD.items(), key=operator.itemgetter(0))
    ordre=[]
    for i in coreD:
        ordre.append(i[1][1])
        #print (ordre)
   
    for j in A.listeAdjacence.keys():
        delationLogique.append( 0)  
    delationLogique.append( 0) 
    k=[]
    d=-1
    nbA=0.0
    indice=-1
    deg=0.0
    degf=0.0
    for c in ordre:
        delationLogique[int(c)]=1
        for i in A.listeAdjacence[str(c)]:
            print (i)
            print (len(delationLogique))
            if (delationLogique[int(i)]==1):
                nbA+=1
        k.append(str(c))
        deg=deg+f[c]
        if((nbA/len(k))>=d):
            d=(nbA/len(k))
            indice=c
            degf=deg
    degf=degf/indice
    return d,indice,degf



def coreDecomposition(nom):
    #cpt = 0
    #d = Q1.degre(nom)
    c = 0
    #i = len(d)
    adjacence = Q2.liste_a_symetrique(nom)
    i=len(adjacence.listeAdjacence.keys())
    tas = []
    eta = dict()
    t=dict()
    d=dict()
    print (len(adjacence.listeAdjacence.keys()))
    for j in adjacence.listeAdjacence.keys():
        #check prq juste ajout marche aps
        #repare degre
        tas = tasMin.Ajout_tab(tas, [j,len(adjacence.listeAdjacence[j])],t)
        
        d[j]=len(adjacence.listeAdjacence[j])
    print ("mdr")
    tas=tasMin.BuildMin_Heap_tab(tas,t)
    while(tas != []):
        v = tas[0]
        c = max(c, v[1])
        """if (c>30):
            print ("i",i)
            print ("v",v[1])
            print ("c",c)"""
        eta[i] = (c, v[0])
        i -= 1
        if (len(tas)==1):
            tas=[]
            break
        tas= tasMin.MaJ(tas, adjacence)
        tas=tasMin.SupMin_tab(tas,t)
        
        #tas.remove(v)
        #tas=tasMin.BuildMin_Heap(tas)
        
        #delationLogique[v[0]] = 0
    #print (eta)
    print (denset2([eta,d],adjacence))
    return eta,d
#coreDecomposition("data2")

#graphe("net.txt")


def DensityScore(A,t):
    #A non symétrique
    r=dict()
    d=dict()
    for i in  A.listeAdjacence.keys():
      r[i]=0
      d[i]=len(A.listeAdjacence[i])
    for e in range (0,t):
        for i in A.listeAdjacence.keys():
            for j in A.listeAdjacence[i]:
                if (r[i]<=r[j]):
                    r[i]+=1
                else:
                    r[j]+=1
    for i in r.keys():
        r[i]=r[i]/t
    return r,d

def densetscore(A,t):
    #pour choisir un noeud parmi tous ceux qui ont le meme density score il faudrait prendre celui qui à le plus haut degre mais nous n'avons pas eu le temps de l'implémenté
    r1=DensityScore(A,t)
    r=r1[0]
    print(r)
    delationLogique=[]
    coreD=r
    f=r1[1]
    coreD = sorted(coreD.items(), key=operator.itemgetter(1))
    maxi=1005
    print ("maxi",maxi)
    ordre=[]
    for i in coreD:
        ordre.append(i[0])
        #print (ordre)
    print (max(ordre))
    for j in range(0,maxi):
        delationLogique.append( 0)  
    delationLogique.append( 0) 
    k=[]
    d=-1
    nbA=0.0
    indice=-1
    deg=0.0
    degf=0.0
    for c in ordre:
        delationLogique[int(c)]=1
        for i in A.listeAdjacence[str(c)]:
            print (c)
            if (delationLogique[int(i)]==1):
                nbA+=1
        k.append(str(c))
        deg=deg+f[str(c)]
        if((nbA/len(k))>=d):
            d=(nbA/len(k))
            indice=c
            degf=deg
    degf=degf/float(indice)
    return d,indice,degf/2,(2*degf/(float(indice)*(float(indice)-1)))

           
def tri(A):
    d=dict()
    print (A)
    for e in range(0,len(A)):
        d[e]=A[e]
    return d
def DensityScore2(nom,t):
    #densityscore lecture de fichier
    r1=dict()
    r=[]
    f = open(nom, "r")
    for n in f:
        buff=n.split()
        if(buff!=[]):
            r1[buff[0]]=0
            r1[buff[1]]=0
    for e in r1.keys():
        r.append(0)
    for e in range (0,t):
         f = open(nom, "r")
         for n in f:
             buff=n.split()
             if(buff!=[]):
                if (r[int(buff[0])]<=r[int(buff[1])]):
                    r[int(buff[0])]+=1
                else:
                    r[int(buff[1])]+=1

    return r
           

#a=coreDecomposition('tmpEmail.txt')
#b=Q2.liste_a("data")
#a=coreDecomposition('data')
b=Q2.liste_a_symetrique("data")
#graphe("net.txt")
#print (denset2(a,b))
#(27.380090497737555, '337')
#(27.415841584158414, '151')
print (densetscore(b,10))