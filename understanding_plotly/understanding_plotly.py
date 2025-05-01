"""This script is all about understanding plotly"""

import plotly.offline as pyo
import matplotlib.pyplot as plt
import pandas as pd
orders = pd.read_excel("Orders/Order Year/2009.xlsx")
print(orders.head())