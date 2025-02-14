

from tempfile import TemporaryFile


class Executor:

    def run(self, code, globals_env=None, locals_env=None):
        try:
            tmp_code = ""
            for line in code.split("\n"):
                if not line.startswith("```"):
                    tmp_code += line + "\n"

            # please be aware of security issue with exec functions
            # LLM can execute arbitrary code
            # if you are aware of security issues, please uncomment below line

            # exec(tmp_code, globals_env, locals_env)
            
        except Exception as e:
            return str(e)
        return None