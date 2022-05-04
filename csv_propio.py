from random import randint
file=open("Medidas.csv","w")
file.write("Altura","peso")

for i in range(100):
  alt=randint(140,200)
  peso=randint(40,100)
  file.write("\n{},{}".format(alt,peso))
file.close()

