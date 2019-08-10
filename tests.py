import unittest
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from engine.corpse import Corpse

# class TestCorpseClass(unittest.TestCase):

#     def test_corpse_creation(self):
#         corpse = Corpse()
#         self.assertEqual(corpse.mass, 1.0)
#         self.assertEqual(corpse.gravity_center, (0.5, 0.5, 0.5))

# if __name__ == '__main__':
#     unittest.main()
density = lambda x, y, z: max(0, np.cos(x*y*2)) if ((0<x<1) and (0<y<1) and (0<z<1)) else 0
# density = np.vectorize(lambda x, y: density(x, y, 0.5))

# corpse = Corpse(
#     density=lambda x, y, z: max(0, np.cos(x*y*10)) if (0<x<1) and (0<y<1) and (0<z<1) else 0
# )
# print(corpse)
z = 0.5
p = 1000
# Heat map 2D
# array = np.array([[density(x/p,y/p,z) for y in range(p)] for x in range(p)])
plt.figure()
ax = plt.axes(projection="3d")
x = np.array([x/p for x in range(p)])
y = x.copy()
# y = 0.5
z = 0.5
d = np.array([[density(i,j,z) for i in x] for j in y])
# plt.plot(x, d)
# plt.show()

ax.plot_surface(x, y, d, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)

# plt.imshow(array, cmap="hot", interpolation="nearest")
# plt.show()
