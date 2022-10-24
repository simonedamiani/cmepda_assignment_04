"""Fourth assignment of CMEPDA Course, 2022/2023"""
import numpy
import numpy as np
from scipy import interpolate
import matplotlib.pyplot

class VoltageData:
    def __init__(self, times, voltages):
        times = numpy.array(times, dtype=numpy.float64)
        voltages = numpy.array(voltages, dtype=numpy.float64)
        self.data = numpy.column_stack([times, voltages])
        self._spline = interpolate.InterpolatedUnivariateSpline(times, voltages, k=3)