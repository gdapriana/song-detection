from fastdtw import fastdtw
import time
from scipy.spatial.distance import euclidean

def matching__(database, new_data):
  results = []
  start_exec = time.time()
  for audio in database:
    distance, path  = fastdtw(x=audio['features'], y=new_data, dist=euclidean)
    results.append({
      'title': audio['title'],
      'artist': audio['artist'],
      'copyright': audio['copyright'],
      'distance': distance,
      'path': path,
    })
  exec_time = (time.time() - start_exec)
  min_distance = min(results, key=lambda x: x['distance'])
  return min_distance, results, exec_time