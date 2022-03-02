# import sys
# print (sys.path)
# sys.path.append('lib')
# print (sys.path)

from fruits.orange import shout
import numpy as np

a = np.arange(15).reshape(3, 5)

print(shout())
print(a)
