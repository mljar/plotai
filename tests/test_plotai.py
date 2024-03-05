import unittest
import pandas as pd
import numpy as np

from plotai import PlotAI

class PlotAITest(unittest.TestCase):

    def test_init(self):
        rows = 100
        df = pd.DataFrame({"x":np.random.rand(rows), "y": np.random.rand(rows)})
        plot = PlotAI(df)
        #plot.make("Plot a scatter plot")

    def test_pass_data(self):
        rows = 100
        df2 = pd.DataFrame({"x":np.random.rand(rows), "y": np.random.rand(rows)})
        plot = PlotAI(df=df2)
        #plot.make("Plot a scatter plot")
    
    def test_gpt4(self):
        rows = 100
        df2 = pd.DataFrame({"x":np.random.rand(rows), "y": np.random.rand(rows)})
        plot = PlotAI(df=df2, model_version="gpt4")
        #plot.make("Plot a scatter plot")
