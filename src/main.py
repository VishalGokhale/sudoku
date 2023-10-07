import numpy as np
import pandas as pd

df = pd.read_excel(r'..\resources\input.xlsx', header=0, index_col=0)
df = df.replace(np.nan, None)
arr = df.to_numpy()
print(arr)
submats = [(r, c) for r in range(3) for c in range(3)]
candidates = {}


# for r in range(3):
#     for c in range(3):
#         candidates[(r,c)] = []

def blanks(smr, smc, arr, digit):
    return [
        (r, c)
        for r in range(smr * 3, smr * 3 + 3)
        for c in range(smc * 3, smc * 3 + 3)
        if not (arr[r, c] or (digit in arr[smr * 3: smr * 3 + 3, smc * 3: smc * 3 + 3]))
    ]


for digit in range(1, 10):
    candidates[digit] = {
        (smr, smc): blanks(smr, smc, arr, digit)
        for smr in range(3) for smc in range(3)
        if blanks(smr, smc, arr, digit)
    }

# for digit in range(1,10):
#     for (smr,smc) in candidates[digit]:



# iterations = 0
# while iterations < 2:
#     iterations += 1
#     for i in range(9):
#         for j in range(9):
#             if arr[i, j]:
#                 continue
#             sub_mat_row_start = (i // 3) * 3
#             sub_mat_col_start = (j // 3) * 3
#             sub_mat = arr[sub_mat_row_start:sub_mat_row_start + 3, sub_mat_col_start:sub_mat_col_start + 3]
#             sub_mat = sub_mat.flatten().tolist()
#             known_vals = arr[i, :].tolist() + arr[:, j].tolist() + sub_mat
#             # print(known_vals)
#             known_vals = set(known_vals)
#             missing = [x for x in range(9) if x not in known_vals]
#             print(f"{i, j} -- {missing=}")
#             if len(missing) == 1:
#                 print(f"updating {i, j}")
#                 arr[i, j] == missing[0]
#
# print(arr)
print(candidates)