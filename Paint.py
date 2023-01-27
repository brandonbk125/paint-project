# the Paint class holds information about the paint a user will use to paint a Wall
class Paint:
    def __init__(self, colour: str, cost_per_litre: float):
        self._colour = colour
        self._cost_per_litre = cost_per_litre

    # get cost per litre of this Paint
    def get_cost(self):
        return self._cost_per_litre

    # get colour of this Paint
    def get_colour(self):
        return self._colour
