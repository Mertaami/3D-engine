"""Main script file"""

from numpy import array, arange
import matplotlib.pyplot as plt
from engine.engine import Engine
from engine.corpse import Corpse
from conf import TIME_STEP

engine = Engine()
corpse1 = Corpse(mass=1, position=array([0, 0, 10]), speed=array([1, 0, 0]))
engine.corpses.append(corpse1)

time = arange(TIME_STEP, TIME_STEP*10000, TIME_STEP)
x1, z1 = [], []

for t in time:
    engine.compute_step(TIME_STEP, 'euler')
    x1.append(corpse1.position[0])
    z1.append(corpse1.position[2])

plt.plot(x1, z1)
plt.legend(["friction"])

plt.show()
