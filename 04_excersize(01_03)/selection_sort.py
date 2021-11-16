#選択ソート

list_a = [5,7,4,5,1,2,3,2,9,1,4]

# i: 0 => list_aの長さ-1までループしたインデックス
for i in range(len(list_a)):
    # min_idx: i以上のインデックスでlist_aに最小値の入っているインデックス
    min_idx = i
    # j: i+1 => list_aの長さ-1
    for j in range(i+1, len(list_a)):
        if list_a[min_idx] < list_a[j]:
            min_idx = j
    list_a[i], list_a[min_idx] = list_a[min_idx], list_a[i]

print(list_a)