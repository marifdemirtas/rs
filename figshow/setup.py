from setuptools import setup, find_packages

setup(
    name="figshow",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "seaborn",
    ],
    entry_points={
        "console_scripts": [
            "figshow=figshow.main:show_figure",
        ],
    },
)
