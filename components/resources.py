from utils import PlayerError
from components.component import Component

class ResourceComponent(Component):
    def __init__(self, name:str, max_resource:int):
        self.name = name
        self.max_resource = max_resource
        self.min_resource = 0
        self.resource_count = None

    def start_of_turn(self) -> int:
        raise NotImplementedError

    def spend(self, amount) -> int:
        new_count = self.resource_count - amount
        if new_count >= self.min_resource:
            self.resource_count = new_count
            return self.resource_count
        raise PlayerError(f'You must have more {self.name} to perform that action.')

    def add(self, amount) -> int:
        new_count = self.resource_count + amount
        if new_count < self.max_resource:
            new_count = self.max_resource
        
        self.resource_count = new_count
        return self.resource_count

    def __str__(self) -> str:
        return self.name

class ManaResourceComponent(ResourceComponent):
    def __init__(self, name: str, max_resource: int, regen_amount:int):
        super().__init__(name, max_resource)
        self.regen_amount = regen_amount

    def start_of_turn(self) -> int:
        self.resource_count = self.regen_amount
        return self.resource_count

class RageResourceComponent(ResourceComponent):
    def __init__(self, name: str, max_resource: int):
        super().__init__(name, max_resource)
        self.damage_last_turn = 0
        

    def start_of_turn(self) -> int:
        reset_count = 5
        if self.damage_last_turn > 0:
            if self.damage_last_turn > 0.49:
                reset_count = 10
            else:
                reset_count += int(round(self.damage_last_turn * 5, 0))
            
        self.resource_count = reset_count
        return self.resource_count
    
    def report_damage_taken_percentage(self, damage_percent):
        self.damage_last_turn += damage_percent

    def report_damage_done_percentage(self, damage_percent):
        self.damage_last_turn += damage_percent

class EnergyResourceComponent(ResourceComponent):
    def __init__(self, name: str, max_resource: int, regen_amount:int):
        super().__init__(name, max_resource)
        self.regen_amount = regen_amount

    def start_of_turn(self) -> int:
        self.add(self.regen_amount)

## Examples:
if __name__ == '__main__':
    mana = ManaResourceComponent(name="Mana", max_resource=100, regen_amount=10)
    rage = RageResourceComponent(name="Rage", max_resource=50)
    rage.report_damage_taken_percentage(0.2)  # Example: 20% of health as damage
    energy = EnergyResourceComponent(name="Energy", max_resource=100, regen_amount=5)









    
