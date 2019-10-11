"""
Voici ma proposition de solution pour le TP1
du cours "Apprenez à programmer en Python"
proposé sur openclassrooms.
Il s'agit d'une mini simulation de la roulette
Ce programme ne simule qu'une partie à la fois
"""

from random import randrange
from math import ceil

gain = mise = 0;
numeroChoisi = -1

while mise <=0 :
	mise = input("Combien voulez vous misez ?: ")
	try:
	 	mise = int(mise)
	except ValueError:
	 	print("votre mise doit être un nombre positif")
	 	mise = 0

while (numeroChoisi < 0 or numeroChoisi >49):
	numeroChoisi = input("choisissez un numéro entre 0 et 49")
	try:
		numeroChoisi = int(numeroChoisi)
	except ValueError:
		print("vous devez choisir un numéro compris entre 0 et 49")
		numeroChoisi = 50

if ((mise > 0) and (numeroChoisi >= 0 and numeroChoisi <=49)):
	lancer = randrange(50)
	if numeroChoisi == lancer:
		print("vous avez tiré le bon numéro")
		print("vous gagnez le triple de votre mise : ")
		gain = 3*mise
		print(gain)
	else:
		if ((lancer%2 == 0 and numeroChoisi%2 == 0) or (lancer%2 != 0 and numeroChoisi%2 != 0)):
			print("vous n'avez pas tiré le bon numéro mais vous avez la bonne couleur")
			gain = ceil(mise/2)
			print("vous avez gagnez la moitié de votre mise")
			print(gain)
		else:
			print("vous avez perdu")
			gain = 0
