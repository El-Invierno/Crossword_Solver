# Vertical Function:-
def vertical(i, j, puzzle, word):
    length = len(word) - 1
    # Up Vertical:-
    r = i
    c = j
    num = 1
    sig = 0
    for k in range(length):
        if r == 1:
            break
        if puzzle[r - 1][c] == word[num]:
            num += 1
            r -= 1
            sig = 1
        else:
            sig = 0
            break
    if sig == 1:
        return 1

    # Down Vertical:-
    r = i
    c = j
    num = 1
    sig = 0
    for k in range(length):
        if r == 11:
            break
        if puzzle[r + 1][c] == word[num]:
            num += 1
            r += 1
            sig = 1
        else:
            sig = 0
            break
    if sig == 1:
        return 1
    else:
        return 0


# Horizontal Function:-
def horizontal(i, j, puzzle, word):
    length = len(word) - 1
    # Left Horizontal:-
    r = i
    c = j
    num = 1
    sig = 0
    for k in range(length):
        if c == 1:
            break
        if puzzle[r][c - 1] == word[num]:
            num += 1
            c -= 1
            # if c < 0 or c > 11:
            #     sig = 0
            #     break
            sig = 1
        else:
            sig = 0
            break
    if sig == 1:
        return 1

    # Right Horizontal Function:-
    r = i
    c = j
    num = 1
    sig = 0
    for k in range(length):
        if c == 11:
            break
        if puzzle[r][c + 1] == word[num]:
            num += 1
            c += 1
            sig = 1
        else:
            sig = 0
            break
    if sig == 1:
        return 1
    else:
        return 0


# Locator Function:-
def locator(word, arr):
    first_char = word[0]
    for i in range(0, 12):  # row

        for j in range(0, 12):  # column
            if arr[i][j] == first_char:
                val_h = horizontal(i, j, puzzle, word)
                if val_h == 1:
                    print('The word', word, 'is found in the horizontal row, from:-', i, ',', j)
                    return 1
                val_v = vertical(i, j, puzzle, word)
                if val_v == 1:
                    print('The word', word, 'is found in the vertical row, from:-', i, ',', j)
                    return 1
    return 0


# Driver Code:-
sample = ['add', 'count', 'even', 'less', 'long', 'math', 'minus', 'more', 'number', 'odd', 'plus', 'subtract', 'sum',
          'total', 'wide']
puzzle = [['b', 'f', 'v', 't', 's', 'a', 'j', 'm', 'o', 'r', 'e', 'h'],
          ['p', 'y', 'l', 'o', 'n', 'g', 'd', 'q', 'i', 'u', 'm', 'z'],
          ['k', 'm', 'f', 'h', 'c', 'v', 'e', 'b', 'x', 'j', 'a', 'r'],
          ['w', 'i', 'd', 'e', 'q', 'p', 'z', 's', 'y', 'o', 't', 'n'],
          ['t', 'n', 'r', 'g', 'a', 'l', 'e', 'u', 'd', 'f', 'h', 'c'],
          ['o', 'u', 'p', 'j', 'n', 'u', 'm', 'b', 'e', 'r', 'x', 'c'],
          ['d', 's', 'y', 'i', 'k', 's', 'f', 't', 'g', 'w', 'u', 'e'],
          ['d', 'a', 'w', 's', 'e', 'h', 'o', 'r', 'n', 'a', 'd', 'd'],
          ['f', 'c', 'o', 'u', 'n', 't', 'k', 'a', 'l', 's', 'b', 'i'],
          ['h', 'x', 'b', 'm', 'f', 'y', 's', 'c', 'u', 'p', 'r', 'q'],
          ['l', 'e', 's', 's', 'i', 'd', 'q', 't', 'o', 't', 'a', 'l'],
          ['y', 'r', 'h', 'e', 'v', 'e', 'n', 'j', 'b', 'k', 'm', 'f']]

for item in sample:
    res = locator(item, puzzle)
    if res == 0:
        print(item, 'is not found in the puzzle!')

