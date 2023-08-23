import unittest
import numpy as np

from plotai import PlotAI

class PlotAITest(unittest.TestCase):

    def test_init(self):
        rows = 100
        x = np.random.rand(rows)
        y = np.random.rand(rows)
        
        plot = PlotAI(x,y, config={"a":2})
        plot.make("Plot a scatter plot")

