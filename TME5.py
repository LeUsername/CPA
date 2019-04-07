# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import copy, matplotlib.pyplot as plt

def sommeMat(P,A):
    for i in A.keys():
        P[i]=P[i]+A[i]
    return P
def prod(A,alpha):
    for i in A.keys():
        A[i]=A[i]*alpha
    return A

def IniP(lnoeud):
    I=dict()
    for i in lnoeud :
        I[i]=1.0/len(lnoeud)
    return I
    
def normalize(A):
    somme = 0.0
    for i in A.keys():
        somme+=A[i]
    for i in A.keys():
        A[i] += (1-somme)/len(A)
    del somme
    return A
def ProdMatVect(M,A):
    B=dict()
    for i in A.keys():
        B[i]=0
    for (i,k) in M.keys():
        B[k]+=M[(i,k)] *A[i]
    return B


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
                     a=noeud.get(buff[i])
                     noeud[buff[i]]=a+1
    f.close()
    if buff:
        del buff
    return noeud
def liste_noeud (nom):
    f = open(nom, "r")
    noeud=[]
    for n in f:
        buff=n.split()
        if(buff!=[]):
            if (buff[0]=='#'):
                continue
            noeud.append(buff[0])
    
    f.close()
    if buff:
        del buff
        
    return noeud
def adjacence(nom,d):
    f = open(nom, "r")
    s = dict()
    for n in f:
        buff=n.split()
        if(buff!=[]):
            if (buff[0]=='#'):
                continue
            s[(buff[0],buff[1])]=1.0/d[buff[0]]

    f.close()
    if buff:
        del buff
    return s
def powerIteration(T, alpha, t,l_noeud):
    I=IniP(l_noeud)
    P=I
    for i in range (0,t):
        P=ProdMatVect(T,P)
        I2=prod(I,alpha)
        P2=prod(P,(1-alpha))
        P=sommeMat(P2,I2)
        P=normalize(P)
    del I,I2,P2
    return P

def plusGrands(vecteur):
    vecteurCopie = copy.deepcopy(vecteur)
    res = list()
    for i in range (0,5):
        res.append(max(vecteurCopie.keys(), key=(lambda k: vecteurCopie[k])))
        vecteurCopie.pop((max(vecteurCopie.keys(), key=(lambda k: vecteurCopie[k]))))
    del vecteurCopie
    return res

def plusGrands2(vecteur):
    res = list()
    for i in range (0,5):
        res.append(max(vecteur))
        vecteur.remove(max(vecteur))
    return res


def plusPetits(vecteur):
    vecteurCopie = copy.deepcopy(vecteur)
    res = list()
    for i in range (0,5):
        res.append(min(vecteurCopie.keys(), key=(lambda k: vecteurCopie[k])))
        vecteurCopie.pop((min(vecteurCopie.keys(), key=(lambda k: vecteurCopie[k]))))
    del vecteurCopie
    return res

def tracer(x, y):
    valX = list()
    valY = list()
    for i in x:
        #if(i in y.keys())
            valX.append(x[i])
            valY.append(i)
    plt.ylabel("out-degree")
    plt.xlabel("PageRank")
    plt.scatter(valX, valY)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(0)
    plt.ylim(0)
    
    plt.show()
def degSortant(nom):
    f = open(nom, "r")
    noeud=[]
    for n in f:
        buff=n.split()
        if(buff!=[]):
            if (buff[0]!='#'):
                while((int(buff[0])<len(noeud)) ==False ):
                    noeud.append(0)
                while((int(buff[1])<len(noeud)) ==False ):
                    noeud.append(0)
                noeud[int(buff[0])]= noeud[int(buff[0])]+1
    
    f.close()
    return noeud
    
def degIN(nom):
    f = open(nom, "r")
    noeud=[]
    for n in f:
        buff=n.split()
        if(buff!=[]):
            if (buff[0]!='#'):
                while((int(buff[0])<len(noeud)) ==False ):
                    noeud.append(0)
                while((int(buff[1])<len(noeud)) ==False ):
                    noeud.append(0)
                noeud[int(buff[1])]= noeud[int(buff[1])]+1
    
    f.close()
    return noeud
        
    
def PageRank2(nom,t,alpha):
    #pagerank lecture de fichier sans mise en mémoire
    deg=degSortant(nom)
    print ("ok")
    P=[0]
    P1=[0]
    for i in range(1,len(deg)):
       P.append(1.0/(len(deg)-1))
       P1.append(0)
    P0=list(P1)
    print (t)
    for i in range(0,t):
        norm=0

        f = open(nom, "r")
        for n in f:
            buff=n.split()
            s=int(buff[0])
            t=int(buff[1])
            if(buff!=[]):
                P1[t]+=(P[s]/deg[s])
                norm+=(P[s]/deg[s])
        a=0
        for i in range(1,len(P1)):
            a=a+P1[i]
        for i in range (1, len(P)):
            P1[i]+=(1-norm)/norm
        for i in range (1, len(P)):
            P1[i]=(P1[i]*(1-alpha)) +(alpha/(len(P)-1)) 
    
        P.clear
        P=list(P1)
        P1=list(P0)
        f.close()
        print (i)   
    return P
def ecrire (A):
    f = open("azerty0.5", "a")
    for e in A:
            f.write(e + " ")
            f.write(str(A[e]) + "\n")
    f.close()   


def charge (A):
    f = open(A, "r")
    no=dict()
    for n in f:
        buff=n.split()
        if(buff!=[]):
            no[int(buff[0])]=float(buff[1])
    return no
#a=PageRank2("/Vrac/CPA-PageRank/alr21--dirLinks--enwiki-20071018.txt",15,0.15) 
#pg['3434750', '31717', '11867', '36165', '36164']
#pp['12664661', '2846524', '3200187', '11694615', '11688561']
#degreout=degSortant("/Vrac/CPA-PageRank/alr21--dirLinks--enwiki-20071018.txt")
#degrein=degIN("/Vrac/CPA-PageRank/alr21--dirLinks--enwiki-20071018.txt")    
noeud = liste_noeud("/Vrac/CPA-PageRank/alr21--pageNum2Name--enwiki-20071018.txt")
degre=degre("/Vrac/CPA-PageRank/alr21--dirLinks--enwiki-20071018.txt")
arete =adjacence("/Vrac/CPA-PageRank/alr21--dirLinks--enwiki-20071018.txt",degre)
#noeud = liste_noeud("sommet")
#degre = degre("grapheCours")
#arete =adjacence("grapheCours", degre)
#a = powerIteration(arete, 0.15, 15, noeud)
#ecrire(a)
P=charge("/Vrac/0.0/test")
P1=charge("/Vrac/0.0/test0.1")
def deg(nom1):
    f = open(nom1)
    T=dict()
    Tinv=dict()
    for line in f:
            a = line[:-1].split()
            if(int(a[0]) in T):
                T[int(a[0])].add(int(a[1]))
            else:
                T[int(a[0])] = set()
                T[int(a[0])].add(int(a[1]))
            if(int(a[1]) not in T):
                T[int(a[1])] = set()
                
            if(int(a[1]) in Tinv):
                Tinv[int(a[1])].add(int(a[0]))
            else:
                Tinv[int(a[1])] = set()
                Tinv[int(a[1])].add(int(a[0]))
            if(int(a[0]) not in Tinv):
                Tinv[int(a[0])] = set()
            del a
    f.close() 
    return T,Tinv



#plotDegOut(P,T)  
#plotDegIn(P,Tinv)      
#print (degreout)
#print (degrein)
#b = powerIteration(arete, 0.5, 15, noeud)
#ecrire(b)
#print (b)
#print(len(b))
       

#print (len(b))
#c = powerIteration(arete, 0.2, 15, noeud)
#print (len(c))
#print(noeud)
#print(a)
#print(plusGrands2(a))
#print(plusPetits(a))
#tracer(a, b)
#tracer(a, c)
