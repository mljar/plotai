import unittest
from plotai.code.executor import Executor


class ExecutorTest(unittest.TestCase):

    def test_run(self):
        code = """from matplotlib import pyplot as plt
plt.plot(1)
"""
        executor = Executor()
        executor.run(code)

    def test_run_with_error(self):
        code = """print(a)"""
        executor = Executor()
        error = executor.run(code)
        self.assertTrue(error is not None)

    def test_run_with_variable(self):
        executor = Executor()
        a = 2
        code = """print(a)"""
        error = executor.run(code, globals(), locals())
        self.assertTrue(error is None)