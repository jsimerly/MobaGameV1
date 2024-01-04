from team.team import Team
from map.game_map import GameMap

class GameManager:
    def __init__(self):
        self.player_1 = None
        self.player_2 = None

        self.team_1 = Team(team_id=1)
        self.team_2 = Team(team_id=2)
        self.game_map: GameMap = None

    def add_player(self, player) -> int:
        if not self.player_1:
            self.player_1 = player
            return 1
        if not self.player_2:
            self.player_2 = player
            return 2
       
        raise ValueError("There are already two players assigned to this game.")
        
    def remove_player(self, player):
        if player == self.player_1:
            self.player_1 = None
        if player == self.player_2:
            self.player_2 = None

    def set_game_map(self, game_map:GameMap):
        self.game_map = game_map
        



    