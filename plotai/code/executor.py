

from tempfile import TemporaryFile


class Executor:

    def run(self, code, globals_env=None, locals_env=None):
        try:
            tmp_code = ""
            for line in code.split("\n"):
                if not line.startswith("```"):
                    tmp_code += line + "\n"

            exec(tmp_code, globals_env, locals_env)
        except Exception as e:
            return str(e)
        return None