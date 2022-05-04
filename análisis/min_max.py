import pandas as pd
pokemon=pd.read_csv("pokemon.csv")

class Min:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def operacion(self):
  min=self.csv[self.columna].min()
  print("El valor min es el siguiente:")
  print(min)



class Max:
  def __init__(self,columna,csv):
    self.columna=columna
    self.csv=csv

def operacion(self):
  max=self.csv[self.columna].max()
  print("El valor max es el siguiente:")
  print(max)