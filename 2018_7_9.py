from math import sin 
from math import cos

sinpoint = 0
cospoint = 0
while sinpoint < 20 and cospoint < 20:
	sinpoint += .1
	cospoint += .1
	x = sin(sinpoint)
	y = cos(cospoint)
	print(" "*round((x*10)+14)+'_')
	print(" "*round((y*10)+14)+'_')
	print(sinpoint)
	print(cospoint)
