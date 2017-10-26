import numpy as np


class NearestNeighbor:
  def __init__(self):
    pass # do nothing, placeholder for later code...


def train(self, X, y):
  """X is N x D where each row is an example. Y is 1-dimension of size N"""
  # the nearest neighbor classifier simply remembers all the training data
  self.Xtr = X
  self.ytr = y


def predict(self, X):
  """X is N x D where each row is an example we with to predict the label for"""
  num_test = X.shape(0)

  # making sure the output type matches the input type
  Ypred = np.zeros(num_test, dtype = self.ytr.dtype)

  for i in xrange(num_test):
    distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
    min_index = np.argmin(distances)
    Ypred[i] = self.ytr[min_index]

  return Ypred

