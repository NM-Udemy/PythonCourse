# じゃんけん　勝った場合はループの外、負けた場合3回でループの外、あいこはあいこと表示

def generate_enemy_hand():
    while True:
        yield '1'
        yield '2'
        yield '3'

def is_win(my_hand, enemy_hand):
    if my_hand == '1' and enemy_hand == '2':
        return True
    elif my_hand == '2' and enemy_hand == '3':
        return True
    elif my_hand == '3' and enemy_hand == '1':
        return True
    return False

hands_dict = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}

from random import randint

lose_count = 0
enemy_hands = generate_enemy_hand()

while True:
    my_hand = input('何を出しますか? 1:グー, 2:チョキ, 3:パー')
    if my_hand not in ('1', '2', '3'):
        print('間違った入力です')
        continue
    enemy_hand = str(randint(1,3))
    print('あなたの出した手は: {}, 相手の出した手は: {}'.format(hands_dict.get(my_hand), hands_dict.get(enemy_hand)))
    if my_hand == enemy_hand:
        print('あいこ')
    elif is_win(my_hand, enemy_hand):
        print('あなたは勝ちました')
        break
    else:
        lose_count += 1
        if lose_count == 3:
            print('あなたは負けました')
            break
        else:
            print('あなたは負けました。再チャレンジ')