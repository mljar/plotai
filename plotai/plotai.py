import pandas as pd
import numpy as np
from plotai.prompt.prompt import Prompt
from plotai.llm.openai import ChatGPT
from plotai.code.executor import Executor
from plotai.code.logger import Logger

class PlotAI:

    def __init__(self, *args, **kwargs):

        self.df, self.x, self.y, self.z = None, None, None, None
        if len(args) > 1:
            for i in range(len(args)):
                if isinstance(args[i], pd.DataFrame):
                    raise Exception("You can pass only one DataFrame")

        if len(args) == 1:
            if isinstance(args[0], pd.DataFrame):
                self.df = args[0]
            else:
                self.x = args[0]
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

        for k in kwargs:
            for expected_k in ["x", "y", "z", "df"]:
                if k == expected_k:
                    setattr(self, k, kwargs[k])

    def make(self, prompt):

        df, x, y, z = self.df, self.x, self.y, self.z
        p = Prompt(prompt, self.df, self.x, self.y, self.z)    

        Logger().log({"title": "Prompt", "details": p.value})

        response = ChatGPT().chat(p.value)

        Logger().log({"title": "Response", "details": response})

        executor = Executor()
        error = executor.run(response, globals(), locals())
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
