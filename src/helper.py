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


def update_arr(arr, candidates):
    for digit in range(1, 10):
        for _, cells in candidates[digit].items():
            if len(cells) == 1:
                cell = cells[0]
                arr[cell[0], cell[1]] = digit


def reverse_map(candidates):
    reversed_map = {(r, c): [] for r in range(9) for c in range(9)}
    for d in range(1, 10):
        for _, cells in candidates[d].items():
            for cell in cells:
                reversed_map[cell].append(d)
    reversed_map = {k: v for k, v in reversed_map.items() if v}
    # dict_print(reversed_map)
    # dict_print(candidates)
    return reversed_map


def update_arr_using_reversed_map(candidates, arr):
    reversed_map = reverse_map(candidates)
    for cell, digits in reversed_map.items():
        if len(digits) == 1:
            arr[cell[0], cell[1]] = digits[0]
