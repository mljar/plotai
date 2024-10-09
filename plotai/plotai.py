import pandas as pd
import numpy as np
from plotai.prompt.prompt import Prompt
from plotai.llm.openai import ChatGPT
from plotai.code.executor import Executor
from plotai.code.logger import Logger


class PlotAI:

    def __init__(self, *args, **kwargs):
        self.model_version = "gpt-3.5-turbo"
        # DataFrame to plot
        self.df, self.x, self.y, self.z = None, None, None, None
        self.verbose = True
        
        for expected_k in ["x", "y", "z", "df", "model_version", "verbose"]:
            if expected_k in kwargs:
                setattr(self, expected_k, kwargs[expected_k])
        
        if self.df is None:
            for arg in args:
                if isinstance(arg, pd.DataFrame):
                    self.df = arg
                    break

    def make(self, prompt):
        p = Prompt(prompt, self.df, self.x, self.y, self.z)
        
        if(self.verbose):
            Logger().log({"title": "Prompt", "details": p.value})

        response = ChatGPT(model=self.model_version).chat(p.value)
        
        if(self.verbose):
            Logger().log({"title": "Response", "details": response})

        executor = Executor()
        error = executor.run(response, globals(), {"df":self.df, "x": self.x, "y": self.y, "z": self.z})
        if error is not None:
            Logger().log({"title": "Error in code execution", "details": error})

            # p_again = Prompt(prompt, self.df, self.x, self.y, self.z, previous_code=response, previous_error=error)

            # Logger().log({"title": "Prompt with fix", "details": p_again.value})

            # response = ChatGPT().chat(p.value)

            # Logger().log({"title": "Response", "details": response})

            # executor = Executor()
            # error = executor.run(response, globals(), locals())
            # if error is not None:
            #     Logger().log({"title": "Error in code execution", "details": error})
