
<p align="center">
  <img src="https://github.com/mljar/plotai/blob/main/media/PlotAI_logo.png?raw=true" height="270" alt="PlotAI logo"/>
</p>


<p align="center">
  <em>🎨🤖 Create Python plots in matplotlib with LLM 🎨🤖</em>
</p>
<p align="center">
  <img alt="" src="https://badge.fury.io/py/plotai.svg"/>
  <img alt="" src="https://img.shields.io/pypi/pyversions/plotai.svg"/>
  <img alt="" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg"/>
</p>

<p align="center">
<a href="https://github.com/mljar/plotai#get-started">🚀 Get Started</a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="https://github.com/mljar/plotai/issues">🤝 Issues</a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="https://twitter.com/MLJAROfficial">🐦 Twitter</a>
<span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
<a href="https://www.linkedin.com/in/aleksandra-p%C5%82o%C5%84ska-42047432/">👩‍💼 LinkedIn</a>
</p>

# PlotAI 🎨🤖 

The easiest way to create plots in Python and Matplotlib. The `plotai` is using LLM to generate code and plots.

The idea:
1. User provides input DataFrame and prompt.
2. The `PlotAI` constructs a prompt for LLM, which contains the first 5 rows of DataFrame and the user's prompt and asks for Python code as output.
3. Returned Python code is executed, and the plot is displayed.

https://github.com/mljar/plotai/assets/6959032/cb80bc35-e534-466d-aa1d-ce240d35f624

The simplest possible API for plotting:
```python
# import packages
import pandas as pd
from plotai import PlotAI
# create some data
df = pd.DataFrame({"x":[1,2,3], "y": [4,5,6]})
# do a plot
plot = PlotAI(df)
plot.make("scatter plot")
```

The `PlotAI` class has only one method, `make()`.

It works in Python scripts and in notebooks (Jupyter, Colab, VS Code).


<p align="center">
  <img src="https://github.com/mljar/plotai/blob/main/media/plotai.jpg?raw=true" height="350" alt="PlotAI logo"/>
</p>

## 🚀 Get started

Install `plotai` package:

```bash
pip install plotai
```

Create `.env` file with the OpenAI API key:

```
OPENAI_API_KEY=your-key-here
```

You can also pass the OpenAI API key in Python:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-key-here"
```

Import `plotai` and make plots:

```python
# import PlotAI
from plotai import PlotAI

# create PlotAI object, pass pandas DataFrame as an argument
plot = PlotAI(df)

# make a plot, just tell what you want
plot.make("make a scatter plot")
```

By default the library will use '*gpt-3.5-turbo*'. You can use different OpenAI models:

```python
# import PlotAI
from plotai import PlotAI

# create PlotAI object, pass pandas DataFrame as an argument
plot = PlotAI(df, model_version="gpt-4")

# make a plot, just tell what you want
plot.make("make a scatter plot")
```

## More examples

#### Analyze the GPD dataset

https://github.com/mljar/plotai/assets/6959032/e62b1a26-7c91-40e4-9d2d-1a600d8dd7ba

#### Analyze the Iris dataset 

![](https://github.com/mljar/plotai/blob/main/media/PlotAI-Iris-demo.png?raw=true)


## 👩‍💼🐦 Connect with Us on LinkedIn & Twitter

Stay up-to-date with the latest updates about PlotAI 🎨🤖 by following us on Twitter ([MLJAR Twitter](https://twitter.com/MLJAROfficial)) and LinkedIn ([Aleksandra LinkedIn](https://www.linkedin.com/in/aleksandra-p%C5%82o%C5%84ska-42047432/) & [Piotr LinkedIn](https://www.linkedin.com/in/piotr-plonski-mljar/)). We look forward to connecting with you and hearing your thoughts, ideas, and experiences with PlotAI. Let's explore the future of AI together!

## ⚠️ Limitations

PlotAI is in very experimental form, below are some limitations:
- PlotAI is using OpenAI ChatGPT-3.5-turbo for completions, it will be nice to extend to other LLMs.
- PlotAI is sending 5 first rows from your DataFrame to OpenAI ChatGPT. If you have sensitive data, please remove/encode it before passing to `PlotAI`.
- PlotAI is executing Python code returned by LLM, it can be dangerous and unsafe. It would be nice to have the option to accept the response code before execution.


## 🛡 Disclaimer

This project, PlotAI, is provided "as is" without any warranty, express or implied. By using this software, you agree to assume all risks associated with its use, including but not limited to data loss, system failure, or any other issues that may arise. The developers and contributors of this project do not accept any responsibility or liability for any losses, damages, or other consequences that may occur as a result of using this software. 

Please note that the use of the OpenAI language models can be expensive due to its token usage. By utilizing this project, you acknowledge that you are responsible for monitoring and managing your own token usage and the associated costs. It is highly recommended to check your OpenAI API usage regularly and set up any necessary limits or alerts to prevent unexpected charges.

## Convert Python Notebooks to web applications 📓 -> 🌐

We are working on framework [Mercury](https://github.com/mljar/mercury) for sharing Python notebooks as interactive web applications. The framework is open source. We also working on a service for [one-click deployment of Python notebooks](https://runmercury.com/). You can check [Python notebooks integrations on our website](https://runmercury.com/use/). 

All the best!

