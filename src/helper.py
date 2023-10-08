import numpy as np
import pandas as pd


def read_input():
    df = pd.read_excel(r'..\resources\input - very hard.xlsx', header=0, index_col=0)
    df = df.replace(np.nan, -1)
    arr = df.to_numpy(dtype=np.int32)
    arr = np.where(arr == -1, None, arr)
    # print(arr)
    return arr
