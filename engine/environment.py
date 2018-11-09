"""Manage different environments in a system.

Todo:

"""

from conf import AIR, WATER

class Environment():
    """Define an environment, which is a part of the system space.

    Attributes:

    Methods:

    """

    contains_corpse = lambda corpse: False
    density = 1
    name = ""

    def __init__(self, name: str, contains_corpse: 'function', density: float):
        self.name = name
        self.contains_corpse = contains_corpse
        self.density = density

    def __repr__(self):
        return "{name} (d={density})".format(name=self.name, density=self.density)

ENVIRONMENTS = {
    "air": Environment("air", lambda corpse: corpse.position[2] > 0.0, density=AIR['density']),
    "water": Environment("water", lambda corpse: corpse.position[2] <= 0.0, density=WATER['density']),
}
