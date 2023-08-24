

class Logger:

    def __init__(self):
        self.is_nb = self.is_notebook()

    def is_notebook(self):
        try:
            from IPython import get_ipython
            if "IPKernelApp" not in get_ipython().config:
                return False
        except Exception as e:
            return False
        return True

    def log(self, msg):
        if self.is_nb:
            from IPython.display import display, HTML
            display(HTML(f"""
<details>
  <summary>{msg.get("title")}</summary>
  <pre>
  {msg.get("details")}
  </pre>
</details>
"""
+
"""

<style>
details {
  border: 1px solid #aaa;
  border-radius: 4px;
  padding: 0.5em 0.5em 0;
  margin-top: 3px;
}

summary {
  font-weight: bold;
  margin: -0.5em -0.5em 0;
  padding: 0.5em;
}

details[open] {
  padding: 0.5em;
}

details[open] summary {
  border-bottom: 1px solid #aaa;
  margin-bottom: 0.5em;
}
</style>

"""))
        else:
            print(msg.get("title"))
            print(msg.get("details"))

