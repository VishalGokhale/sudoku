import json
from pprint import pprint

import numpy as np
import pandas as pd


def read_input():
    df = pd.read_excel(r'..\resources\input - hard.xlsx', header=0, index_col=0)
    df = df.replace(np.nan, -1)
    arr = df.to_numpy(dtype=np.int32)
    arr = np.where(arr == -1, None, arr)
    # print(arr)
    return arr


def dict_print(dict_to_print):
    print("=" * 40)
    pprint(dict_to_print)
    print("=" * 40)


def candidates_reverse(candidates):
    reversed_candidates = {(smr, smc): [] for smr in range(3) for smc in range(3)}
    for d in range(1, 10):
        for submat in list(candidates[d].keys()):
            reversed_candidates[submat].append(d)

    return reversed_candidates
