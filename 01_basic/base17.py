# all, any

if all((30 < 10, 10 < 20, 'a' == 'a')): # allは全てTrue
    print('allの中の処理')

if not any((30<20, 10<5, 'a' == 'b')): # anyは1つでもTrue
    print('anyの中の処理')