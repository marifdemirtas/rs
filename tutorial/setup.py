from setuptools import setup, find_packages

setup(
    name="tutorial",
    version="0.2.1",
    packages=find_packages(),
    include_package_data=True,  # <--- CRITICAL: Tells pip to look at MANIFEST.in
    install_requires=[
        "seaborn",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "tutorial=tutorial.main:display",
        ],
    },
)
