

import numpy as np

def calculate(list):

  if (len(list) != 9):
    raise ValueError("List must contain nine numbers.")

  matrix = np.array_split(list, 3)
  print(np.mean(matrix, axis = 0).tolist())

  mean = [np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist(), np.mean(matrix)]
  variance = [np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist(), np.var(matrix)]
  sd = [np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist(), np.std(matrix)]
  max = [np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist(), np.max(matrix)]
  min = [np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist(), np.min(matrix)]
  sum = [np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist(), np.sum(matrix)]

  calculations = {"mean": mean,
                  "variance": variance,
                  "standard deviation": sd,
                  "max": max,
                  "min": min,
                  "sum": sum,
                  }

  return calculations



if __name__ == "__main__":
    print(calculate([0,1,2,3,4,5,6,7,8]))
