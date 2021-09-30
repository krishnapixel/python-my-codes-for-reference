import numpy as np
import matplotlib.pyplot as plt
from docplex.mp.model import Model
import docplex.mp.solution as Solution
n = 10
customers = [i for i in range (n)]
arcs = [(i,j) for i in customers for j in customers if i!=j]
print (arcs)
random = np.random
random.seed(1)
coord_x = random.rand(n)*100
coord_y = random.rand(n)*100
print coord_x
Print coord_y
x = coord_x
y = coord_y

