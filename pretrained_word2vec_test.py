from gensim.models import Word2Vec
import numpy as np
from numpy.linalg import norm

def cos_sim(A, B):
  return np.dot(A, B)/(norm(A)*norm(B))

model = Word2Vec.load('./ko.bin')

print(model.wv.most_similar('다이어트'))