###################################################################
# groupe <MIASHS TD02>
# David Daulasim
# Gaetan Bres
# Line-Sephora Assouan
# Sede Saizonou
# Souhaila Chaouch
# Ramata Dia 
# https://github.com/uvsq21921099/terrain_CHAOUCH/blob/main/terrain_CHAOUCH.py
#####################################################################

########################
# import des librairies:

import tkinter as tk
import random as rd
import pickle





#############
# constantes:  
hauteur = 500
largeur = 500
nb_cases = int(input("Entrez un nombre de cases pair copris entre 2 et 100"))
cote = largeur // nb_cases
T = 5


n = 4
nbcol =  largeur // cote
nbligne = hauteur // cote

nombre_carre = nb_cases*nb_cases
 
couleur = ["blue", "brown"]
tableau = [[0 for x in range(nb_cases)] for y in range(nb_cases)]
#GrilleTotal = [[0 for x in range(nb_cases)] for y in range(nb_cases)]
#######################
# Variables globales
liste = []
cpt = 0
cptt = 0
position = None

########################
#Les fonctions utilisées:

def grille():
    """permet de dessiner une grille """
    x = 0
    y = 0
    
    while y <= hauteur:
        y += cote
        canvas.create_line((x,y),(largeur, y), fill = 'black')
    y = 0
    x = 0
    
    while x <= largeur:
        x += cote
        canvas.create_line((x,y),(x, hauteur), fill = 'black')

def terrain_hasard():
    """permet de generer un terrain au hasard"""
    global  cpt, carre, tableau
    li = []
    #liste_couleur = matrice(liste1)
    cpt += 1
    if cpt <= n:
        for x in range(nb_cases):
            for y in range(nb_cases):
                color = rd.choices(couleur, weights=[50, 50] , k=nombre_carre)
                carre = canvas.create_rectangle((x * cote, y * cote),(x * cote + cote, y * cote + cote),fill= color[x])
                li.append(color[x])
                lii = [li[i:i+nb_cases] for i in range(0, len(li), nb_cases)]
                tableau = lii
    return tableau
#def compte_voisinage():
    #"""compte le nombre de cases bleu autour d'une case"""
    #liste = terrain_hasard()
    #cppt = 0
    #for col in range(len(liste)):
        #for m in range(nb_cases):
            # [[1,2,3,4],[5,6,7,8], [9,10,11,12]]
            #colonne = liste[col]
            #case = liste[col][m]
            #voisinage1 = liste[col][m-1]
            #voisinage2 = liste[col-1][m-1]
            #voisinage3 = liste[col+1][m-1]
            #voisinage4 = liste[col-1][m]
            #voisinage5 = liste[col+1][m]
            #voisinage6 = liste[col-1][m+1]
            #voisinage7 = liste[col][m+1]
            #voisinage8 = liste[col+1][m+1]
            #"liste_voisinage = [voisinage1, voisinage2, voisinage3, voisinage4, voisinage5, voisinage6, voisinage7, voisinage8]
            
            #for k in liste_voisinage:
                #if k == 'blue':
                    #cppt +=1
    #return cppt

#def change_couleur():
    #"""change la couleur de la case"""
    #global case, T
    #nbcase_bleu = compte_voisinage()
    #if nbcase_bleu >= T:
        #case = 'blue'
    #else:
        #case = 'brown'



def creer_peronnage(event):
    global cptt, cote, position
    x = event.x
    y = event.y
    dx, dy = cote, cote
    rayon = 2
    cptt += 1
    if cptt == 1:
        for i in range(0, largeur, cote):
            for j in range(0, hauteur, cote):
                x1 = (x // cote)*cote+(cote/2)
                y1 = (y//cote)*cote+(cote/2)
                
                x2 = x1 + rayon
                y2 = y1 + rayon
                position = [int(x//cote),int(y//cote)]
                carre1 =  canvas.create_rectangle((x1-rayon,y1-rayon),(x2,y2), fill = 'black')
    return position 
    
def deplacer_droite():
    """permet de deplacer le personnage vers la droite"""
    global carre1
    position  = creer_peronnage()
    if position[0]+1<nb_cases and tableau[position[0]+1][position[1]] == 'brown' :
        canvas.move(carre1, cote, 0)
        position[0]+=1


def deplacer_gauche():
    """permet de deplacer le personnage vers le gauche"""
    if position[0]-1>=0 and tableau[position[0]-1][position[1]] == 'brown' :
        canvas.move(carre1, -cote, 0)
        position[0]-=1
def deplacer_haut():
    """permet de deplacer le personnage vers le haut"""
    if position[1]-1>=0 and tableau[position[0]][position[1]-1] == 'brown' :
        canvas.move(carre1, 0, -cote)
        position[1]-=1
def deplacer_bas():
    """permet de deplacer le personnage vers le bas"""
    if position[1]+1<nb_cases and tableau[position[0]][position[1]+1] == 'brown' :
        canvas.move(carre1, 0, cote)
        position[1]+=1


def sauvegarde() : #Sauvegarde les données
    fic = open("sauvegarde_terrain","w" )
    for h in saveList :
        pickle.dump(h.letatdelagrille)
        pickle.dump(h.lepersonnage)
    fic.close()

def recharge(): #récupérer le terrain sauvegarder
    pickle.dump(saveList)
    fic = open("sauvegarde_terrain","r")
    saveList = pickle.load()
    fic.close()
    

    
######################
# programme principal:

racine = tk.Tk()
racine.title('terrain_CHAOUCH')
#######################
# création des widgets:

canvas = tk.Canvas(racine, width = largeur, height = hauteur, bg="white")
boutton = tk.Button(racine, text = 'generer', command =  terrain_hasard)
grille()
#change_couleur()

canvas.bind("<1>", creer_peronnage)

canvas.bind("<Right>", deplacer_droite)
canvas.bind("<Left>", deplacer_gauche)
canvas.bind("<Up>", deplacer_haut)
canvas.bind("<Down>", deplacer_bas)

########################
# placement des widgets:

boutton.grid(column =0 ,row = 1)
canvas.grid(column =0 ,row = 0)

#####################
# boucle principale:
racine.mainloop()
