import numpy as np

def mahalanobis_distance(x, mean, cov):
  d = np.dot(x - mean, np.linalg.inv(cov))
  d = np.dot(d, (x - mean).T)
  return d
  
