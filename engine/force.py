"""Manage all kind of forces.

Todo:
    Friction expression depends on speed norm value.
    Weight is not a constant field.
"""


from numpy import zeros, array, ndarray
from numpy.linalg import norm
from engine.corpse import Corpse

class Force():
    """A Force is a constraint on a Corpse.

    Note:
        Abstract

    """

    @staticmethod
    def null_force_field(target: Corpse) -> ndarray:
        """Define a default null action force field function.

        Args:
            target: Not used but important for standardization

        Returns:
            Null acceleration

        """
        return zeros(3)


class ForceField(Force):
    """A Force which only needs informations about target.

    Note:
        Use only when source is not included in the system.

    Attributes:
        field (function): Function of target returning acceleration

    Methods:

    """

    def __init__(self, field=Force.null_force_field):
        self.acceleration = field


FIELDS = {
    'WEIGHT': ForceField(lambda target: target.mass * array([0, 0, -9.81])),
    'AIR_FRICTION': ForceField(lambda target: - 1/2 * target.environment.density * target.drag_coef * target.cross_section_area * norm(target.speed) * target.speed)
}
