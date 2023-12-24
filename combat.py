import random

class AttackComponent:
    def __init__(self):
        pass

    def attack(self, damage: (int, int), target):
        mu = (damage[1] + damage[0])//4
        sigma = (damage[1] - damage[0])//4
        damage = int(random.gauss(mu, sigma)//1)
        return damage
        # add a target later