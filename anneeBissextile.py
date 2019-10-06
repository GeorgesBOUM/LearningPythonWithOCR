annee = int(input("choisissez une année : "))

if (annee % 4 == 0):
	if (annee % 100 == 0):
		if (annee % 400 == 0):
			print("l'année {} est bissextile".format(annee))
		else:
			print("l'année {} n'est pas bissextile".format(annee))
	else:
		print("l'année {} est bissextile".format(annee))
else:
	print("l'année n'est {} pas bissextile".format(annee))