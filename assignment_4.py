"""Fourth assignment of CMEPDA Course, 2022/2023"""
import matplotlib.pyplot as plt
import numpy
from scipy import interpolate


class VoltageData:
    """Handle a set of voltage measurements at different times"""
    def __init__(self, times, voltages):
        """ Constructor from two iterables of the same length """
        times = numpy.array(times, dtype=numpy.float64)
        voltages = numpy.array(voltages, dtype=numpy.float64)
        self.data = numpy.column_stack([times, voltages])
        self._spline = interpolate.InterpolatedUnivariateSpline(times, voltages, k=3)

    @classmethod
    def from_file(cls, file_path):
        """ Alternative constructor from file """
        t, v = numpy.loadtxt(file_path, unpack=True)
        return cls(t, v)

    @property
    def times(self):
        return self.data[:, 0]

    @property
    def voltages(self):
        return self.data[:, 1]

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        """Return the number of measurements (which is the numer of rows)"""
        return len(self.data)

    def __iter__(self):
        """Return self_data as an iterable"""
        return iter(self.data)

    def __str__(self):
        """Print the full content row by row (formatted)"""
        header = '#row || time || voltage \n'
        output_str = ''
        for i, row in enumerate(self):
            line = f'{i}: {row[0]:.1f}, {row[1]:.2f} \n'
            output_str += line
        return header + output_str

        # Compact:
        # return header + '\n'.join([f'{i}: {row[0]:.1f}, {row[1]:.2f}' for i, row in enumerate(self)])

    def __repr__(self):
        """Print the full content row by row (debugging)"""
        return '\n'.join([f'{row[0]}  {row[1]}' for row in self])

    def __call__(self, t):
        """Return the voltage value interpolated at time t from spline"""
        return self._spline(t)

    def plot(self, ax=None, draw_spline=False, **plot_opts):
        """Draw the data points and optionally the spline interpolating them"""
        if ax is None:
            ax = plt.figure('voltage_vs_time')
        else:
            plt.sca(ax)
        plt.plot(self.times, self.voltages, **plot_opts)
        plt.xlabel('Time[s]')
        plt.ylabel('Voltage[mV]')
        if draw_spline:
            x = numpy.linspace(min(self.times), max(self.voltages), 100)
            plt.plot(x, self(x), '-')
        return ax
