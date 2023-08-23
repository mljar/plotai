from plotai.llm.openai import ChatGPT

class PlotAI:

    def __init__(self, *args, **kwargs):

        print("args")
        print(args)
        print("kwargs")
        print(kwargs)


        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        

    def make(self, prompt):
        print(prompt)


        print(self.x[:5])
        print(self.y[:5])

        msg = f"""
You are provided two NumPy arrays:

x=np.array({self.x[:5]})
y=np.array({self.y[:5]})


Initial python code to be updated        

```
# TODO import required dependencies
# Provide the plot
```

Output only Python code. Plot should be 

{prompt}
"""
        print(msg)
        ChatGPT().chat(msg)


    def code(self):
        print("aa")

    def save(self):
        pass


    def plot(self):
        pass