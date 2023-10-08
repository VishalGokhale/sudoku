import numpy as np
import pandas as pd


def read_input():
    df = pd.read_excel(r'..\resources\input.xlsx', header=0, index_col=0)
    df = df.replace(np.nan, None)
    arr = df.to_numpy()
    # print(arr)
    return arr
