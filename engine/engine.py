"""An Engine instance is what runs the system physics.

Todo:

"""

from typing import List
from conf import TIME_STEP

class Engine():
    """An Engine runs the system physics."""

    def __init__(self, corpses: List['Corpse'] = None):
        self.corpses = corpses if corpses else []

    def compute_step(self, time_step: float = TIME_STEP, method: str = 'euler'):
        for corpse in self.corpses:
            corpse.move_step(time_step, method)
