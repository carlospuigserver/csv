import pandas as pd
pokemon=pd.read_csv("pokemon.csv")
class media:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def operacion(self):
  media=self.csv[self.columna].mean()
  print("La media es la siguiente:")
  print(media)


