import unittest

from plotai.prompt.prompt import Prompt

class PromptTest(unittest.TestCase):

    def test_init(self):
        p = Prompt("do scatter plot")
        self.assertTrue(p.value is not None)