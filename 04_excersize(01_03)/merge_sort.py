# マージソート

def merge_sort(arr):
    if len(arr) > 1:
        res = [] # 返り値の配列
        mid = len(arr) // 2 # 配列のまん中の値
        L = arr[:mid] # [1,2,3,4] => [1,2]
        R = arr[mid:] # [1,2,3,4] => [3,4]
        L = merge_sort(L) # 
        # [4,1,3,2]
        # L: 4,1, R: 3, 2 (merge_sort: 1回目)
        # merge_sort(L(4,1)), merge_sort(R(3,2)) (merge_sort: 1回目)
        # L: 4, R:1     L: 3, R: 2 (merge_sort(2回目))
        # merge_sort(L(4)), merge_sort(R(1))      merge_sort(L(3)), merge_sort(R(2)) (merge_sort(2回目))
        # 4,1    3,2(merge_sort(3回目))
        # 4, 1 => 1,4  3,2 => 2,3(merge_sort(2回目))
        # L(1,4) R(3,2) =>  1,2,3,4 (merge_sort(1回目))
        # 4,1,3,2 => 1,2,3,4

        R = merge_sort(R) # [2] => 2
        i = j = 0 # iはLを探索するインデックス, jはRを探索するインデックス
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            elif L[i] > R[j]:
                res.append(R[j])
                j += 1
            else:
                res.append(L[i])
                i += 1
        while i < len(L):
            res.append(L[i])
            i += 1
        while j < len(R):
            res.append(R[j])
            j += 1
        return res
    else:
        return arr
    
list_a = [5,7,6,4,5,1,2,3,2,2,9,1,4]
print(merge_sort(list_a))