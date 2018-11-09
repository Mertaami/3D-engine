"""Manage all kind of corpses.

Todo:
    Environment property raise error when multiple environments exist.
"""

from typing import List
from numpy import zeros, ndarray
from conf import TIME_STEP, ACTIVATED_FIELDS
from engine.force import FIELDS
from engine.environment import Environment, ENVIRONMENTS

class Corpse():
    """A Corpse just being in a system.

    Note:

    Attributes:
        mass: Mass [kg]
        position: 3D array [m]
        speed: 3D array [m/s]
        drag_coef: Used in friction []
        cross_section_area: Used in friction [m²]
        fields: List of fields names acting on the corpse
        environments: List of environments names the corpse move in
        acceleration: 3D array computed from fields [m/s²]
        environnement: Actual environment containing the corpse

    Methods:

    """

    # ATTRIBUTES
    mass: float = 0
    position: ndarray = zeros(3)
    speed: ndarray = zeros(3)
    drag_coef: float = 1
    cross_section_area: float = 0.01

    fields: List[str] = ACTIVATED_FIELDS
    environments: List[str] = ENVIRONMENTS

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
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)






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
