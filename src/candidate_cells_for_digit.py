def candidate_cells_for_digit(arr):
    # submats = [(r, c) for r in range(3) for c in range(3)]
    candidates = {}
    for digit in range(1, 10):
        candidates[digit] = {
            (smr, smc): blanks(smr, smc, arr, digit)
            for smr in range(3) for smc in range(3)
            if blanks(smr, smc, arr, digit)
        }
    return candidates


def blanks(smr, smc, arr, digit):
    return [
        (r, c)
        for r in range(smr * 3, smr * 3 + 3)
        for c in range(smc * 3, smc * 3 + 3)
        if not (arr[r, c] or (digit in arr[smr * 3: smr * 3 + 3, smc * 3: smc * 3 + 3]))
    ]