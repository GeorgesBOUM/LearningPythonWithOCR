# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:13:20 2019

@author: utilisateur
"""


def compteLesEtoiles(mot):
    """
       Fonction qui compte le nombre d'étoiles dans un mot
       donné en paramètres.
       Les étoiles masquent les lettres à deviner pendant une partie
    """
    compteur = 0
    for element in mot:
        if element == '*':
            compteur += 1
    return compteur
