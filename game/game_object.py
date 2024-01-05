from abc import ABC, abstractmethod

class GameObject(ABC):
    
    def start_of_game(self):
        pass

    
    def start_of_queue_phase(self):
        pass

    def turn_processing(self):
        pass
    
    def death_processing(self):
        pass

    
    def animate_turn(self):
        pass

    
    def post_death_actions(self):
        pass

    
    def end_of_turn(self):
        pass



    
