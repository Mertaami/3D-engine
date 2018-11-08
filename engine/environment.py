"""Manage different environments in a system.

Todo:

"""

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
    "air": Environment("air", lambda corpse: corpse.position[2] > 0.0, density=1.225),
    "water": Environment("water", lambda corpse: corpse.position[2] <= 0.0 and corpse.position[2] > -10.0, density=997),
}
