"""Manage all kind of corpses.

TODO:
    Environment property raise error when multiple environments exist.
"""

from typing import List, Tuple
from numpy import zeros, ndarray, array
from scipy.integrate import tplquad, quad
from conf import TIME_STEP, ACTIVATED_FIELDS
from utils import init
from engine.force import FIELDS
from engine.environment import Environment, ENVIRONMENTS

# TODO
inf = 10

class Corpse():
    """A Corpse just being in a system.

    Note:

    Attributes:
        mass: Mass [kg]
        gravity_center: 3D array [m]
        speed: 3D array [m/s]
        drag_coef: Used in friction []
        cross_section_area: Used in friction [m²]
        fields: List of fields names acting on the corpse
        environments: List of environments names the corpse move in
        acceleration: 3D array computed from fields [m/s²]
        environnement: Actual environment containing the corpse

    Methods:
        move_step: Move the corpse of a step, using specified method
        density: Density repartition in space [kg/m-3]
    """

    # ATTRIBUTES
    mass: float = 0
    speed: ndarray = zeros(3)
    drag_coef: float = 1
    cross_section_area: float = 0.01

    fields: List[str] = ACTIVATED_FIELDS
    environments: List[str] = ENVIRONMENTS

    @property
    def gravity_center(self) -> Tuple[float, float, float]:
        gx = 1 / self.mass * tplquad(lambda x, y, z: x * self.density(x, y, z), -inf, inf, -inf, inf, -inf, inf)[0]
        gy = 1 / self.mass * tplquad(lambda x, y, z: y * self.density(x, y, z), -inf, inf, -inf, inf, -inf, inf)[0]
        gz = 1 / self.mass * tplquad(lambda x, y, z: z * self.density(x, y, z), -inf, inf, -inf, inf, -inf, inf)[0]
        return array([gx, gy, gz])

    @property
    def acceleration(self) -> ndarray:
        """Compute acceleration from forces."""
        force = zeros(3)
        for name, field in FIELDS.items():
            if name in self.fields:
                force = force + field.acceleration(self)
        return force / self.mass

    @property
    def environment(self) -> Environment:
        """Determine the Environment containing the corpse."""
        environment = None
        for name, env in self.environments.items():
            if environment and env.contains_corpse(self):
                raise NotImplementedError
            elif env.contains_corpse(self):
                environment = env
        return environment

    # METHODS
    def __init__(self, **kwargs):
        init(self, **kwargs)
        print(self.density(0.5, 0.5, 0.5))
        self.mass = tplquad(self.density, -inf, inf, -inf, inf, -inf, inf)[0]
        print(self.mass)

    def __str__(self):
        return ("Corpse:\n"
                f"\tmass: {self.mass} kg\n"
                f"\tDrag coefficient: {self.drag_coef}\n"
                f"\tCross section area: {self.cross_section_area} m²\n"
                f"\tPosition (gravity center): {self.gravity_center}"
                )

    def move_step(self, time_step: float = TIME_STEP, method: str = 'euler'):
        """Compute and move the corpse during the time_setp, based on its acceleration.

        Args:
            time_step
            method: Define th enumeric method used to compute.

        """
        if method == 'euler':
            self.position = self.position + self.speed * time_step
            self.speed = self.speed + self.acceleration * time_step
        elif method == 'smart-euler':
            self.speed = self.speed + self.acceleration * time_step
            self.position = self.position + self.speed * time_step
        elif method == 'mean-smart-euler':
            speed = self.speed
            self.speed = self.speed + self.acceleration * time_step
            self.position = self.position + 1/2 * (self.speed + speed) * time_step

    def density(self, x: float, y: float, z: float) -> float:
        """Default"""
        return int((0<x<1) and (0<y<1) and (0<z<1))

