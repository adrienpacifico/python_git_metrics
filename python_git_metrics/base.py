"""
python_git_metrics base module.

This is the principal module of the python_git_metrics project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""


class BaseClass:
    def base_method(self) -> str:
        """
        Base method.
        """
        return "hello from BaseClass"

    def __call__(self) -> str:
        return self.base_method()


def base_function() -> str:
    """
    Base function.
    """
    return "hello from base function"

def untested_function():
    return None

