import pandas as pd
import numpy as np

def get_species():
  return pd.read_csv("../data/X_species.csv", index_col=[0, 1])

def get_taxonomy():
  return pd.read_csv("../data/X_all.csv", index_col=[0, 1])

def get_counts():
  return pd.read_csv("../data/counts.csv", index_col=[0, 1])

def get_labels():
  return pd.read_csv("../data/y.csv", index_col=[0, 1])

def get_labels_all():
  return pd.read_csv("../data/y_all.csv", index_col=[0, 1])
