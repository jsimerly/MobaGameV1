from abilities.ability import Ability

class BasicAttack(Ability):
    def __init__(self):
        super().__init__(name='Basic Attack')

class Slash(Ability):
    def __init__(self):
        super().__init__(name='Slash')

class SecondWind(Ability):
    def __init__(self):
        super().__init__(name='Second Wind')

class RecklessRage(Ability):
    def __init__(self):
        super().__init__(name='Reckless Rage')