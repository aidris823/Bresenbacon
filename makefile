all: line_draw.py
	python line_draw.py
	convert img.ppm img.png
	display img.png