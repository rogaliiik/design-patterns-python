from abc import ABC, abstractmethod


class Character:
    def __init__(self):
        self.weapon_behavior = None

    def fight(self):
        self.weapon_behavior.fight()

    def setWeapon(self, weaponBehavior):
        self.weapon_behavior = weaponBehavior


class Queen(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = None


class King(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = None


class Troll(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = None


class Knight(Character):
    def __init__(self):
        super().__init__()
        self.weapon_behavior = None


class WeaponBehavior(ABC):
    @abstractmethod
    def fight(self):
        pass


class SwordBehavior(WeaponBehavior):
    def fight(self):
        print("Stabby stab stab")


class KnifeBehavior(WeaponBehavior):
    def fight(self):
        print("Knife attacks!")


class AxeBehavior(WeaponBehavior):
    def fight(self):
        print("Axe attacks!")


class BowAndArrowBehavior(WeaponBehavior):
    def fight(self):
        print("Bow attacks!")


queen = Queen()
queen.setWeapon(BowAndArrowBehavior())
queen.fight()
