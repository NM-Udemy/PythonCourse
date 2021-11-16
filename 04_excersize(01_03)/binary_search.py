# 2分探索

def binary_search(arr, target): # arrが昇順にソートされた配列、targe:配列にある探索したい値
    left = 0  #探索の左端
    right = len(arr) - 1 #探索の右端
    for i in range(len(arr)): # 配列の長さ分実行すれば十分
        search_idx = (left + right) // 2 # 中間値(探索のインデックス)
        if arr[search_idx] == target:
            return search_idx
        elif arr[search_idx] > target: # 探索値より大きかった場合
            right = search_idx - 1
        elif arr[search_idx] < target:
            left = search_idx + 1
        if left > right:
            return -1

a = [1, 2, 3, 4, 5, 6, 8]
print(binary_search(a, 7))