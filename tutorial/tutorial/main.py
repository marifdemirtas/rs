import base64
import sys
import secrets, os
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

def show_file(filename=None):
    # Use the first command line argument if filename isn't passed directly
    if filename is None and len(sys.argv) > 1:
        filename = sys.argv[1]
    
    if not filename:
        print("Please provide a filename.")
        return

    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    print("@start_figure@" + encoded_string + "@end_figure@")


def display(object):
    if isinstance(object, sns.FacetGrid):
        figure = object._figure
    elif isinstance(grid._figure, mpl.pyplot.Figure):
        figure = object
    else:
        msg = '''
        display() failed.
        display requires return object of a plotting function. For example:

            figure = sns.barplot(x=..., y=..., data=...)
            display(figure)

        OR

            grid = sns.FacetGrid(...)
            grid.map(...)
            display(grid)
    
        '''
        print(msg)
        raise ValueError(f"Cannot display figure: {object}")

    filename = secrets.token_hex(4) + ".png"
    figure.get_figure().savefig(filename)
    show_file(filename)


def load_dataset(name):
    # Get the directory where this file (main.py) is located
    base_path = os.path.dirname(__file__)

    if name == "restaurants":
        # Build the full path dynamically
        file_path = os.path.join(base_path, 'data', 'restaurants.csv')
        return pd.read_csv(file_path)
        
    elif name == "weather":
        file_path = os.path.join(base_path, 'data', 'weather.csv')
        return pd.read_csv(file_path)
        
    elif name == "weather_long":
        file_path = os.path.join(base_path, 'data', 'weather_long.csv')
        return pd.read_csv(file_path)
        
    else:
        # Standard error message
        msg = '''
        load_dataset should be called in one of two ways:
        restaurants = load_dataset("restaurants")
        weather = load_dataset("weather")
        weather_long = load_dataset("weather_long")
        '''
        print(msg)
        raise ValueError(f"Unknown dataset: {name}")