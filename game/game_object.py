from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def start_of_game(self):
        pass

    @abstractmethod
    def start_of_queue_phase(self):
        pass

    @abstractmethod
    def movement_processing(self):
        pass

    @abstractmethod
    def pre_combat_processing(self):
        pass

    @abstractmethod
    def combat_processing(self):
        pass

    @abstractmethod
    def death_processing(self):
        pass

    @abstractmethod
    def animate_turn(self):
        pass

    @abstractmethod
    def post_death_actions(self):
        pass

    @abstractmethod
    def end_of_turn(self):
        pass



    
