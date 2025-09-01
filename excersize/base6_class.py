class GameScore:
    high_score = 0
    champion_name = None
    
    def __init__(self, player_name):
        self.player_name = player_name
        self.current_score = 0
    
    def reset(self):
        self.current_score = 0
    
    def __call__(self, points):
        self.current_score = points
        # 最高スコアの更新
        if self.current_score > GameScore.high_score:
            GameScore.high_score = self.current_score
            GameScore.champion_name = self.player_name
            print(f'新記録！{self.player_name}: {self.current_score}')
        return self.current_score
    
    @classmethod
    def get_champion(cls):
        if cls.champion_name:
            return f"{cls.champion_name}({cls.high_score}点)"
        else:
            return 'まだ記録がありません'

player1 = GameScore('Alice')
player2 = GameScore('Bob')

print(player1(150)) # 新記録！Alice: 150 150
print(player2(200)) # 新記録！Bob: 200 200
print(player1(100)) # 100
print(player1.current_score) # 100

print(GameScore.get_champion())
player2.reset()
print(player2.current_score)
print(GameScore.get_champion())

player3 = GameScore('Charlie')
player3(300) # 新記録！Charlie: 300
print(GameScore.get_champion()) # Charlie(300点)