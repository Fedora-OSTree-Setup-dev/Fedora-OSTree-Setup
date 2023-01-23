# HACKING

To setup the project, clone the `devel` branch of the repository and create
your own branch with the name of feature/issue you want to introduce/work on:

```
git clone -b devel https://github.com/iaacornus/Fedora-OSTree-Setup
```

Then

```
git branch <name-of-branch>
```

The project is using Python >= 3.10, preferrably 3.11, thus to start working on
check if you have Python >= 3.10 with:

```
python --version
```

Although there can be workarounds, it is encouraged to use Python 3.10, but if not
possible, it is not enforced, upto Python >= 3.7 is acceptable. Then create a
virtual environment with

```
python -m venv venv
```

Source it and start installing dependencies with

```
pip install -r DEV_REQUIREMENTS && pip install -r REQUIREMENTS
```

_Note that in other system `pip3` or `pip<python-version>` is used instead,
e.g. `pip3.11`._

`DEV_REQUIREMENTS` include the modules needed for test, specifically `mypy` and
the `types` of other third party modules, while `REQUIREMENTS` contains the
modules used by project.

Finally start working in the project, refer to [CONTRIBUTING.md](CONTRIBUTING.md)
for guidelines about code formatting and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
for acceptable interactions with in the community.

# Notes

1. All functions are documented with docstrings, [PEP 0257](https://peps.python.org/pep-0257/),
which takes a format of:

```python
def function(x: int) -> int:
    """This is an example of long documentation.

    Args:
        x -- any number

    Returns:
        Square of the given number, x.
    """

    return x*x
```

Then for a short docstring:

```python
def function(x: int) -> int:
    """"Square a number."""

    return x*x
```

2. Use comments, preferrably if you can use the Better Comments syntax, please do:

```
#! FOR URGENT/WARNING
#? IMPORTANT
#* NOTICE
# TODO: THINGS THAT SHOULD BE DONE
```


