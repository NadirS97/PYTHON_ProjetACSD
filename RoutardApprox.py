# -*- coding: utf-8 -*- 
# Fait par: Saiah Nadir L2-Inge n°2164158

# Pour la file de priorité

from priority_dict import priority_dict
import random

# =================================================================================================================
#                                           EXEMPLE DE GRAPH
# =================================================================================================================

G = {
     'a': {'b':1.54, 'c':2.97},
     'b': {'a':1.54, 'f':5, 'c':10.5},
     'c': {'a':2.97, 'b':10.5, 'f':2.33, 'e':4.25},
     'd': {'f':8.01, 'e':3.73},
     'e': {'c':4.25, 'd':3.73}, 
     'f': {'b':5, 'c':2.33, 'd':8.01} 
    }

J = {
    'a' : {'f':4.5,'b':2,'d':6.6,'e':0.5},
    'b' : {'a':2, 'f':0.5, 'd':7,'c':3.5},
    'c' : {'f':20, 'b':3.5,'d':18.7,'e':9},
    'd' : {'a':6.6, 'b':7,'c':18.7,'e':1.7},
    'e' : {'c':9, 'd':1.7,'a':0.5},
    'f' : {'a':4.5, 'b':0.5,'c':20}
    }

# =================================================================================================================
#                                          Algo_Djikstra 
#                               
#                             Return une liste du plus court chemin 
# =================================================================================================================

#| DEBUT ==================
def Algo_Djikstra (G, s, d) :
    
        # G -> notre graph
        # s -> Sommet de départ
        # d -> Sommet final (destination)  
    
    print ('\n| ----> Algo_Djikstra <---- |')    
    F=priority_dict()
    Pere=priority_dict()
    
                  #   INITIALISATION
    
    for u in (list(G.keys())) :     # Parcourant tous les sommets de G
        F[u]= float('inf')          # Initialiser la valeur (le cout pour y acceder depuis notre sommet initial) de tous nos sommets a l'infini
                                    # Et creer l'element dans notre File F={Sommet:Poids}
        Pere[u] = 'None'            # Initialiser le pere de tous nos sommets a 'None'
                                    # Et creer l'element dans notre File Pere={Sommet:Pere}
    F[s] = 0                        # Initialiser la valeur (le cout pour y acceder depuis notre sommet initial) de notre sommet initial a 0
    
                  #   FIN INTIALISATION
    
    X=[]
    
    while F:
        p_u_min=F[F.smallest()] 
        u=F.pop_smallest()
        for v in (list(G.get(u).keys())):
            
                 #   RELACHER  
            
            if v in F and F[v] > p_u_min + G.get(u).get(v) :
                F[v] = p_u_min + G.get(u).get(v)
                Pere[v]=u
                
                 #   FIN RELACHER

    SommetActuel = d
        # Apres avoir finis de traiter les sommets etapes par etapes toutes les valeurs de nos sommets dans notre File F sont normalement
        # mis a jour on peut donc remonter de pere en pere pour retracer notre chemin en commencant par la destination, jusqu'a notre sommet initial
        # en l'ajoutant a chaque fois en premiere position dans notre liste X
        
        # c'est une sorte de retracage du chemin pour construire notre chemin X du sommet final jusqu'au sommet initial
    
    while SommetActuel != s:
        X.insert(0,SommetActuel)
        SommetActuel=Pere[SommetActuel]
    X.insert(0,s)
    print('-> Le plus court chemin entre',s,'et',d,'est:', X)
    return X

#| FIN ==================

# =================================================================================================================
#                             PRIM FONCTIONNEL (FINAL)
#                                  Return file
#                  Avec un sommet r aleatoire si r est absent, en revanche
#                   s'il est donne en parametre il sera pris en compte
# =================================================================================================================
#| DEBUT ==================

def Algo_Prim (G, r=None) :
    
        # G -> notre graph
        # r -> a notre racine (sommet intial) si il est donné en parametre alors il le prendra en compte sinon il lui attribuera "None"
    
    print ('\n| ----> Algo_Prim <---- |')
    
    if r == None:
        r=random.choice(list(G.keys())) # Recuperer un sommet initial au hasard
    
    Somme = priority_dict()
            # File Somme={Sommets:Poids} contenant uniquement les sommets de notre chemin avec sa valeur (poids) pour nous permettre de calculer le poids final
    F = priority_dict()
            # File F={Sommets:Poids}
    Pere = priority_dict()
            # File Pere={Sommets:Pere} representant l'arbre a retourner
    
    
    for u in (list(G.keys())) :         
        F [u] = float('inf')            # Initialisation toutes les valeur des sommets a inf
    F[r] = 0                            # Initialisation de la valeur du sommet initial a 0 
    Pere[r] = 'None'                    # Definir le pere du sommet initial a None
    
    
       
    while F:
        u = F.pop_smallest()                        # ExtraireMin(F) Permet de retourner dans u le sommet ayant le poids minimum de F, ainsi que de la supprimer de F 
        for v in (list(G.get(u).keys())):           #On parcourt les sommets adjacents de u (qui est le sommet ayant un poids minimum)
            if v in F and G.get(u).get(v) < F[v] :  #On teste si v est dans notre F et si le poids entre l'arrette u, v est inferieur au poids de v dans F
                Pere[v] = u                         #Si c'est cas alors le pere de v devient u
                F[v] = G.get(u).get(v)              #et le poids de celui ci deviens le poids de l'arrette u, v
                Somme[v]= G.get(u).get(v)           #Somme me permet juste de stocker les sommets et leur nouveau poids pour me permettre de calculer le poids du chemin total
                
    def poids():                            #Fonction poids() qui retourne le poids total du chemin parcouru
        poids=0
        for v in (list(Somme.values())):    # Boucle pour nous permettre d'additioner les poids de chaque arretes pour avoir le poids final
            poids = poids + v
        return poids
        
    #print ('-> Pere {Sommet : Pere} =', Pere)
    print ('-> Sommet initial:', r)
    print ('\n-> Poids total minimum:', poids())
    
    return Pere

#| FIN ==================

# =================================================================================================================
#                                PARCOURS PREFIXE
#               Return liste avec des sommets ordonés selon leur positionement
#                    !ATTENTION! Selon un sommet initial aleatoire 
#                          (sinn il faut le donner en parametre)
# ================================================================================================================
#| DEBUT ==================
def Parcours_Prefixe(G, r=None):
       
         # G -> notre graph
         # r -> (Pour prim)a notre racine (sommet intial) si il est donné en parametre alors il le prendra en compte sinon il lui attribuera "None" (pas obligatoire)
    
    print ('\n| =======> Parcours_Prefixe <======= |')
    
    if r == None:
        F=Algo_Prim(G)                  # Dans le cas ou r n'est pas donné en parametre alors on execute Algo_Prim(G) qui va chercher un sommet initial aleatoirement
    else:
        F=Algo_Prim(G,r)                # Dans le cas ou r est donné en parametre alors on execute Algo_Prim(G,r) avec r etant le sommet initial
        
    print ('\n-> F {Sommet:Pere} =', F)
    
    
    def getSommetInitial():             # Retourne le premier sommet ayant pour pere None qui correspond a notre sommet initial
        for h in F.keys():              # On parcourt tous les sommets de F et on retourne le sommet si le pere associé est "None"
            if F.get(h) == 'None':
                return h
          
    def trouver_cle (v):                # trouver_cle(v) une fonction qui retourne un dictionnaire contenant toutes les clés ayant la meme valeur que V
        L=dict()
        for k,val in F.items():         # On transforme notre file F en -> items c'est a dire en couple (clé, valeur) pour pouvoir recupérer 
            if v == val:                # Toutes les clés ayant la meme valeur v, on recupere la clé dans L
                L[k]= v
        return L
    
    def sommet_fils():                                  # Retourne la file Fils = {Sommet:[Fils]}
        Fils=priority_dict()            
        for v in F.keys() :             
            Fils[v] = list(trouver_cle(v).keys())       # Ajouter a la file Fils la valeur v et toutes ces clés ayant pour valeur v
                                                        # Autrement dis la file fils= pour chaque sommet sera associé a la liste de toutes ces sommets fils 
        return Fils
  
    print ('\n-> Fils {Sommet:[fils]} =',sommet_fils())
    
    Lfinal=[]
    def Parcours_Prefixe_Rec(s):                            # Fonction recursive de prefixe  qui prend en parametre un sommet s et qui retourne la liste des sommets triés
                                                            # selon l'ordre prefixe
        Lfinal.append(s)
        if len(sommet_fils().get(s)) != 0 :
            for j in range (len(sommet_fils().get(s))):     #Pour pouvoir traiter chaque sommets fils j -> position
                for o in [(sommet_fils().get(s) [j])]:      #Pour parcourir les sommets fils de s a la position j
                    Parcours_Prefixe_Rec(o)                 #Pour chaque sommet fils o, on réexecute en recursivité  Parcours_Prefixe_Rec(o)
        return Lfinal
    print('\n-> Liste des sommets triés selon l\'ordre prefixe =', Parcours_Prefixe_Rec(getSommetInitial()))
    Lfinal=[]                          # Je reinitialise a vide car je l'ai modifie pour "print" alors avant de return il faut la reinitialiser
    return Parcours_Prefixe_Rec(getSommetInitial())
    

#| FIN ==================
    
# =================================================================================================================
#                                    RoutardApprox(G)
#                   Retourne un cycle de poid minimum pour un graph G
# =================================================================================================================
#| DEBUT ==================

def RoutardApprox(G, r=None) :
    
            # G -> notre graph
            # r -> (Pour prim) a notre racine (sommet intial) si il est donné en parametre alors il le prendra en compte sinon il lui attribuera "None" (pas obligatoire)
        
    print ('===============> ROUTARD_APPROX <================')
    sigma=[]
    
    if r == None:
        rho=Parcours_Prefixe(G)                # Dans le cas ou r n'est pas donné en parametre alors on execute Algo_Prim(G) qui va chercher un sommet initial aleatoirement
    else:
        rho=Parcours_Prefixe(G,r)              # Dans le cas ou r est donné en parametre alors on execute Algo_Prim(G,r) avec r etant le sommet initial 
        
    sigma.insert(0,rho[0])                     # Inserer dans sigma à la premiere position le premier élément de rho
    for j in range(0, len(rho)-1):             
        mu=Algo_Djikstra(G,rho[j],rho[j+1])    # Grace à Djikstra , on calcule le plus court chemin entre les sommets j et j=+1 (sommet j -> rho[j]; sommet j+1 -> rho[j+1])
        mu.pop(0)                              # Retire le premier élément de mu
        sigma.extend(mu)                       # Ajoute mu à la fin de sigma
    mu=Algo_Djikstra(G,rho[len(rho)-1],rho[0]) # On calcule le plus court chemin entre le dernier  et le premier éléments de rho
    mu.pop(0)                                  # Retire le premier élément de mu
    sigma.extend(mu)                           # Ajoute mu à la fin de sigma
    poids=0                                             # On initialise le poids a 0
    for i in range(0,len(sigma)-1):                     # i allant de 0 a len(sigma) -1
        poids= poids + G.get(sigma[i]).get(sigma[i+1])  # a chaque fois on additione l'ancien poids au poids entre l'arrette des sommets sigma[i] et sigma[i+1]
        
    print ('\n================================================')
    print ('-> Le poids total est:', poids) 
    print ('-> Sequence:', sigma)
    
    return sigma

#| FIN ==================
    
#==================================================================================================================
#                                             TESTS
#==================================================================================================================
"""
Algo_Djikstra(G, 'a', 'b')
Algo_Prim(G,'a')
Algo_Prim(G)
Parcours_Prefixe(G,'a')
Parcours_Prefixe(G)
RoutardApprox(G,'a')
RoutardApprox(G)

"""