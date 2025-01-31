import pandas as pd
import numpy as np

def database__(csv_path, npy_path):
  dataset = pd.read_csv(csv_path)
  data = []
  for i, row in dataset.iterrows():
    data.append({
      'title': row['title'],
      'artist': row['artist'],
      'copyright': row['copyright'],
      'features': np.load(f"{npy_path}/{row['title']}.npy")
    })
  return data