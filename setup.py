"""setup.py for dmc2gym"""

from setuptools import find_packages, setup

TESTS_REQUIRE = [
    "black",
    "coverage",
    "codecov",
    "codespell",
    "flake8",
    "flake8-blind-except",
    "flake8-builtins",
    "flake8-commas",
    "flake8-debugger",
    "flake8-docstrings",
    "flake8-isort",
    "flaky",
    "isort",
    "pytest",
    "pytest-xdist",
    "pytype",
]

setup(
    name="dmc2gym",
    version="1.1.0",
    author="Yawen Duan and Denis Yarats",
    description=("a gym like wrapper for dm_control"),
    license="",
    keywords="gym dm_control openai deepmind",
    packages=find_packages(),
    install_requires=[
        "gym",
        "dm_control",
    ],
    extras_require={"test": TESTS_REQUIRE},
)
