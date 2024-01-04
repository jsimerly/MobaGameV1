
# May need to differtiate between Abilities and basic attacks as basic attacks improve throughout the game.
class Ability:
    def __init__(self, name:str) -> None:
        self.name = name

    required_components = []

    def inject_components(self, **components):
        for component_type, component in components.items():
            if component_type in self.required_components:
                setattr(self, component_type, component)

    def activate(self):
        pass
    
    def __str__(self):
        return self.name