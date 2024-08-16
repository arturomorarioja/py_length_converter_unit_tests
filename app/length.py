"""
Length class
It converts length units between the metric (cm) and imperial (inches) systems
"""
__author__ = "Arturo Mora-Rioja"
__date__ = "August 2024"

class Length():
    METRIC = 'M'
    IMPERIAL = 'I'
    CONVERSION_FACTOR = 2.54

    def __init__(self, measure, system):
        if system not in (self.METRIC, self.IMPERIAL):
            raise Exception('Invalid length system')
        self.measure = abs(measure)
        self.system = system

    def convert(self):
        if self.system == self.METRIC:
            return round(self.measure / self.CONVERSION_FACTOR, 2)
        else:
            return round(self.measure * self.CONVERSION_FACTOR, 2)