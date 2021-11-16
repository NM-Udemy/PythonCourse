# deep_first_search.py

def deep_first_search(H, W, S):
    """
    H: 高さ
    W: 幅
    文字列のリスト
    """
    # write code here
    def dfs(x, y): # gまで到達できたらTrue
        if any((x < 0, x >= W, y < 0, y >= H)):
            return False
        if S[y][x] == '#':
            return False
        if S[y][x] == 'g':
            return True
        tmp_y = S[y] # ....
        tmp_y = tmp_y[:x] + '#' + tmp_y[(x+1):] # ..#.
        S[y] = tmp_y
        return dfs(x-1, y) | dfs(x + 1,y) | dfs(x, y-1) | dfs(x, y+1)

    for i in range(H):
        for j in range(W):
            if S[i][j] == 's':
                if dfs(i, j):
                    print('Yes')
                else:
                    print('No')

# spots[0]
# ...S
# ....
# ....
# .g..    


Hs = [4, 4, 10, 10, 1]
Ws = [5, 4, 10, 10, 10]
spots = [
    ['s####', '....#', '#####', '#...g'],
    ['...s', '....', '....', '.g..'],
    ['s.........', '#########.', '#.......#.', '#..####.#.', '##....#.#.', '#####.#.#.', 'g.#.#.#.#.', '#.#.#.#.#.', '###.#.#.#.', '#.....#...'],
    ['s.........', '#########.', '#.......#.', '#..####.#.', '##....#.#.', '#####.#.#.', 'g.#.#.#.#.', '#.#.#.#.#.', '#.#.#.#.#.', '#.....#...'],
    ['s..####..g']
]
deep_first_search(Hs[0], Ws[0], spots[0]) # Noと表示
deep_first_search(Hs[1], Ws[1], spots[1]) # Yesと表示
deep_first_search(Hs[2], Ws[2], spots[2]) # Noと表示
deep_first_search(Hs[3], Ws[3], spots[3]) # Yesと表示
deep_first_search(Hs[4], Ws[4], spots[4]) # Noと表示

