#author:mohammed khandwawala(e16b117)
import string
f = open("hbv.txt","r")
content = f.read()
content = content.translate(None,string.punctuation).lower()
words = content.split()
d ={}

for word in words :
	if word in d:
		d[word] += 1
	else:
		d[word] = 1

for key in sorted(d,key = d.get, reverse=True):
	print key,"\t",d[key]
