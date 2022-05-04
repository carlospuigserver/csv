from media import media
from desv_tip import desv
from mediana import mediana
from min_max import min
from min_max import max
from moda import moda
from varianza import varianza
from rango import rango
from cant_observacio import filas
from cant_observacio import columnas
from cuartiles import q1,q3
import pandas as pd 

pokemon=pd.read_csv("pokemon.csv")

# Numero filas
filaspok=filas(pokemon)
filaspok.operacion()

#Num column
columnaspok=columnas(pokemon)
columnaspok.operacion()

#Valores max
max_Hp = max(pokemon,"HP")
max.operacion()

#Valores min
min_Hp = min(pokemon,"HP")
min.operacion()


#Media
media_Hp = media(pokemon,"HP")
media.operacion()

#Moda 
moda_Hp = moda(pokemon,"HP")
moda.operacion()

#Mediana
mediana_Hp = mediana(pokemon,"HP")
mediana.operacion()

#Desviación típica
desv_típ_Hp = desv(pokemon,"HP")
desv.operacion()


#Varianza
varianza_Hp = varianza(pokemon,"HP")
varianza.operacion()

#Rango
Rango_Hp = rango(pokemon,"HP")
rango.operacion()


#Q1
q1_Hp = q1(pokemon,"HP")
q1.operacion()

#Q3
q3_Hp = q3(pokemon,"HP")
q3.operacion()

# Rango intercuartílico
a= pokemon["HP"].quantile(0.25)
b= pokemon["HP"].quantile(0.75)
rango_int= b-a
print("El rango intercuartílico es {}".format(rango_int))

from random import randint
file=open("Medidas.csv","w")
file.write("Altura","peso")

for i in range(100):
  alt=randint(140,200)
  peso=randint(40,100)
  file.write("\n{},{}".format(alt,peso))
file.close()

medidad=pd.read_csv("Medidas.csv")