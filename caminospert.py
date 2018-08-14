"""
Pwogwamita kakkoii para cawcuwaw wos caminos dew PEWT (* ^ ω ^)
Twes archivitos de entwada y dos de sawida (≧◡≦)
Cawcuwa duwación y howguwa 。.:☆*:･'(*⌒―⌒*)))
"""

""" Archivitos (´ ω `♡) """
IN_1aENTREGA="1.txt" # Caminos de wa pwimera entwega
IN_2aENTREGA="2.txt" # Caminos de wa segunda entwega
IN_3aENTREGA="3.txt" # Caminos de wa tewcewa entwega
OUT_DURACION="duracion.txt" # Duwación de wos caminos
OUT_HOLGURA="holgura.txt" # Howgura de wos caminos
""" Pwogwamita (°◡°♡) """
duracion = open(OUT_DURACION,"w") # Abwimos ew awchivo
""" Anwade wa duwacion de was twes entweguitas ( ` ω ´ ) """
def durac(l1, l2, l3):
	duracion.write(
	  l1.split("=")[0]
	+ "-"
	+ l2.split("=")[0]
	+ "-"
	+ l3.split("=")[0]
	+ "="
	+ str(
		  int(l1.split("=")[1])
		+ int(l2.split("=")[1])
		+ int(l3.split("=")[1])
		  )
	+ "\n"
	)
""" Pwoducto cawtesiano de was twes entwegas (⌒_⌒;) """
with open(IN_1aENTREGA,"r") as one:
	with open(IN_2aENTREGA,"r") as two:
		with open(IN_3aENTREGA,"r") as three:
			one.seek(0)
			for l1 in one:
				two.seek(0)
				for l2 in two:
					three.seek(0)
					for l3 in three:
						durac(l1, l2, l3)
duracion.close() # Cewwamos ew awchivo
holgura = open(OUT_HOLGURA,"w") # Abwimos ew awchivo
""" Buscamos ew máximo y cawcuwamos la howguwa """
with open(OUT_DURACION,"r") as duracion:
	max = 0
	duracion.seek(0)
	for l in duracion:
		d = int(l.split("=")[1])
		if d > max:
			max = d
	duracion.seek(0)
	for l in duracion:
		holgura.write(
		  l.split("=")[0]
		+ " "
		+ str(max)
		+ "-"
		+ str(int(l.split("=")[1]))
		+ "="
		+ str(max-int(l.split("=")[1]))
		+ "\n"
		)
holgura.close() # Cewwamos ew awchivo
""" Bai bai (╥﹏╥) """
