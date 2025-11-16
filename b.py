import itertools

letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
for perm in itertools.permutations(range(10), len(letters)):
    S, E, N, D, M, O, R, Y = perm
    if S == 0 or M == 0:
        continue
    SEND = S * 1000 + E * 100 + N * 10 + D
    MORE = M * 1000 + O * 100 + R * 10 + E
    MONEY = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
    if SEND + MORE == MONEY:
        print("Solution Found!")
        print(f"S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}")
        print(f"{SEND} + {MORE} = {MONEY}")
        break
else:
    print("No solution found.")
