class Paint:
    def __init__(self, colour: str, cost_per_litre: float):
        self._colour = colour
        self._cost_per_litre = cost_per_litre

    def get_cost(self):
        return self._cost_per_litre

    def get_colour(self):
        return self._colour
