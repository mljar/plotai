<p align="center">
  <img src="https://github.com/mljar/plotai/blob/main/media/plotai.jpg?raw=true" height="450" alt="PlotAI logo"/>
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

PlotAI is a powerful Python package that streamlines the process of creating captivating plots using Matplotlib. With PlotAI, visualizing your data becomes effortless, allowing you to focus on insights rather than intricate coding.
With PlotAI, you can leave behind the complexities of manual plot configuration. By combining the power of Matplotlib with the intuitive nature of natural language prompts, PlotAI empowers you to bring your data to life through stunning visualizations effortlessly. Dive into the world of seamless data visualization with PlotAI today!

The idea:
1. User provide input DataFrame and prompt.
2. The `PlotAI` constructs a prompt for LLM which contains first 5 rows of DataFrame and user's prompt and asks for Python code as output.
3. Returned Python code is executed and plot is displayed.

https://github.com/mljar/plotai/assets/6959032/138a1812-4941-4ae3-b6d6-c45238852190

## Get started

Install `plotai` package:

```bash
pip install plotai
```

Create `.env` file with OpenAI API key:

```
OPENAI_API_KEY=your-key-here
```

You can also pass OpenAI API key in Python

```python
import os
os.environ["OPENAI_API_KEY"] = "your-key-here"
```

Import `plotai` and make plots:

```python
# import PlotAI
from plotai import PlotAI

# create PlotAI object, pass pandas DataFrame as argument
plot = PlotAI(df)

# make a plot, just tell what you want
plot.make("make a scatter plot")
```

## More examples

#### Analyze GPD dataset

Contents of video:

https://github.com/mljar/plotai/assets/6959032/378dd5ac-4169-4b02-b726-8706c351b8e2

#### Analyze Iris dataset

![](https://github.com/mljar/plotai/blob/main/media/PlotAI-Iris-demo.png?raw=true)


## 👩‍💼🐦 Connect with Us on LinkedIn & Twitter

Stay up-to-date with the latest updates about PlotAI 🎨🤖 by following us on Twitter ([MLJAR Twitter](https://twitter.com/MLJAROfficial)) and LinkedIn ([Aleksandra LinkedIn](https://www.linkedin.com/in/aleksandra-p%C5%82o%C5%84ska-42047432/) & [Piotr LinkedIn](https://www.linkedin.com/in/piotr-plonski-mljar/)). We look forward to connecting with you and hearing your thoughts, ideas, and experiences with PlotAI. Let's explore the future of AI together!

## ⚠️ Limitations



## 🛡 Disclaimer

This project, PlotAI, is provided "as-is" without any warranty, express or implied. By using this software, you agree to assume all risks associated with its use, including but not limited to data loss, system failure, or any other issues that may arise. The developers and contributors of this project do not accept any responsibility or liability for any losses, damages, or other consequences that may occur as a result of using this software. 

Please note that the use of the OpenAI language models can be expensive due to its token usage. By utilizing this project, you acknowledge that you are responsible for monitoring and managing your own token usage and the associated costs. It is highly recommended to check your OpenAI API usage regularly and set up any necessary limits or alerts to prevent unexpected charges.



