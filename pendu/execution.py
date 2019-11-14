# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:12:22 2019

@author: Georges
"""

# Une version basique du jeu du pendu
# TAF : documenter du code python

from fonctions import compteLesEtoiles
from random import choice

listeDesMots = ['bonjour', 'salut', 'bonsoir']
motADeviner = choice(listeDesMots)
compteurEtoiles = len(motADeviner)
coupsAjouer = compteurEtoiles
motMasque = '*' * compteurEtoiles

# --> TAF : on pourrait rajouter en option la possibilité de
#           lancer une nouvelle partie s'il le souhaite
#           On mettrait pour cela la boucle while dans une 
#           fonction appelée si besoin
# --> TAF : on pourrait aussi rajouter une gestion du score,
#           le nombre de points étant le nombre de coups restant 
#           à jouer.

while compteurEtoiles > 0 and coupsAjouer > 0:
    print(motMasque)
    print("il vous reste {0} coups à jouer".format(coupsAjouer))
    lettreChoisie = input("Entrer une lettre : ")
    # --> TAF : Il faudrait éventuellement levée une exception
    #           pour vérifier la saisie de l'utilisateur
    lettreTrouvee = 0
    for i in range(len(motADeviner)):
        if lettreChoisie == motADeviner[i]:
            motMasque = motMasque[:i] + lettreChoisie + motMasque[(i+1):]
            lettreTrouvee += 1
    if lettreTrouvee == 0:
        print("la lettre que vous avez choisie n'est pas",
              "dans le mot à deviner")
    compteurEtoiles = compteLesEtoiles(motMasque)
    coupsAjouer -= 1
if motMasque == motADeviner:
    print("c'est gagné !!")
else:
    print("c'est perdu !!")
