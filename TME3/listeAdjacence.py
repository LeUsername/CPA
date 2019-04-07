import time
import queue
# awk '{if ($1<$2) print $1" "$2;else if ($2<$1) print $2" "$1}' data | sort -n -k1,1 | uniq > data2
# pour enlever self node et trier

class adjlist:
    cd = None # degré cumulatif
    adj = None # listes des voisins de tous les noeuds 
    degre = None
    existeSommetZero = False
    
    def __init__(self, a,b,c, d):
        self.adj = a
        self.cd = b
        self.degre = c
        self.existeSommetZero = d
        
    def affiche(self, i):
        if(i in self.degre):
            return (self.adj[self.cd[i]-self.degre[i]:self.cd[i]])
        else:
            return list()
        
def mkadjlist(nom):
    fichier = open(nom,"r")
    degre = dict()
    liste_voisins = list()
    liste_degre_cumulatif = list()
    noeudMax = 0
    existeSommetZero = False
    for ligne in fichier:
        s = ligne.split()
        if(int(s[0]) == 0):
            existeSommetZero = True
        entree = int(s[0])
        sortie = int(s[1])
        if(entree == sortie):
            liste_voisins.append(-1)
            if(entree not in degre):
                degre[entree] = 0
                if(entree>noeudMax):
                    noeudMax = entree
            degre[entree] += 2
        else:
            liste_voisins.append(-1)
            liste_voisins.append(-1)
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
    degre_cumulatif = 0
    for i in range(noeudMax+1):
        if(i in degre):
            degre_cumulatif += degre[i]
        liste_degre_cumulatif.append(degre_cumulatif)
    fichier = open(nom,"r")
    for ligne in fichier:
        s = ligne.split()
        entree = int(s[0])
        sortie = int(s[1])
        degC = liste_degre_cumulatif[entree]
        deg = degre[entree]
        for i in range(degC-deg, degC):
            if(liste_voisins[i] == -1):
                liste_voisins[i] = sortie
                break
        degC = liste_degre_cumulatif[sortie]
        deg = degre[sortie]
        for i in range(degC-deg, degC):
            if(liste_voisins[i] == -1):
                liste_voisins[i] = entree
                break          
    return adjlist(liste_voisins,liste_degre_cumulatif,degre,existeSommetZero)

def BFSTousLesSommets(nom):
    plusGrandeCC = 0
    G = mkadjlist(nom)
    print("debut BFS")
    sommetsDejaVisite = list()
    for v in range(len(G.cd)):
        res = list()
        sommetOrigine = v
        if(sommetOrigine in sommetsDejaVisite):
            continue
        #BFS(G, v, res[v])
        fifo = queue.Queue(len(G.cd))
        fifo.put(sommetOrigine)
        mark=list()
        mark.append(sommetOrigine)
        if(sommetOrigine not in sommetsDejaVisite):
            sommetsDejaVisite.append(sommetOrigine)
        while(not fifo.empty()):
            u = fifo.get(0)
            res.append(u)
            for w in G.affiche(u):
                if(w not in mark):
                    fifo.put(w)
                    if(w not in mark):
                        mark.append(w)
                    if(w not in sommetsDejaVisite):
                        sommetsDejaVisite.append(w)
        if(len(res)>plusGrandeCC):
            plusGrandeCC = len(res)
            print(plusGrandeCC)
        del res
    return plusGrandeCC
#print(BFSTousLesSommets("/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt"))

"""t1 = time.time()
res = mkadjlist("/Vrac/TME_CPA_19-02-20/com-orkut.ungraph-clean.txt")
print(time.time()-t1)"""

def Diametre(nom, sommetBase, nbIter):
    sommetMax = sommetBase
    i = 0
    G = mkadjlist(nom)
    poidsMax = 0
    while(i < nbIter):
        fifo = queue.Queue(len(G.cd))
        fifo.put((sommetMax,0))
        poids = dict()
        mark=set()
        mark.add(str(sommetMax))
        poids[0] = set()
        poids[0].add(sommetMax)
        while(not fifo.empty()):
            u = fifo.get(0)
            for v in G.affiche(u[0]):
                if v not in mark:
                    if(u[1]+1 not in poids):
                        poids[u[1]+1] = set()
                    poids[u[1]+1].add(v)
                    fifo.put((v,u[1]+1))
                    mark.add(v)
        poidsMaxCourant = max(poids.keys())
        if(poidsMaxCourant > poidsMax):
            poidsMax = poidsMaxCourant
            sommetMax = poids[poidsMax].pop()
        print (i)
        i +=1
    return sommetMax, poidsMax

#print(Diametre("/Vrac/TME_CPA_19-02-20/com-friendster.ungraph.txt", 1, 5))

def TRList(nom):
    G = mkadjlist(nom)
    nbTriangle = 0
    res = list()
    if(G.existeSommetZero):
        for u in range(0,len(G.cd)):    
            if(u==0):
                voisinsU = [voisin for voisin in G.adj[0: G.cd[u]]]
            else:
                voisinsU = [voisin for voisin in G.adj[G.cd[u- 1]: G.cd[u]]]
            for v in voisinsU:
                if(v > u):
                    voisinsV = [voisin for voisin in G.adj[G.cd[v - 1]: G.cd[v]]]
                    nbTriangle += len([w for w in voisinsV if w in voisinsU])
    else:
        for u in range(1,len(G.cd)):
            voisinsU = [voisin for voisin in G.adj[G.cd[u-1]: G.cd[u]]]
            for v in voisinsU:
                if(v > u):
                    voisinsV = [voisin for voisin in G.adj[G.cd[v - 1]: G.cd[v]]]
                    nbTriangle += len([w for w in voisinsV if w in voisinsU])
    return nbTriangle/3

t1 = time.time()
print(TRList("/Vrac/TME_CPA_19-02-20/com-lj.ungraph-clean.txt"))
print(time.time() - t1)