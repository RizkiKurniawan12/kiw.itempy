# 1. Malefic Gun
class maleficGun(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Malefic Gun"
        self.effect = "attack speed & penetration"
        self.effectValue = 40
        self.description = "Increase attack speed and armor penetration"

    def useItem(self, player):
        print(f"{player} used {self.name}, attack speed increased and penetration +{self.effectValue}")


# 2. Sea Halberd
class seaHalberd(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Sea Halberd"
        self.effect = "reduce heal"
        self.effectValue = 50
        self.description = "Reduce enemy healing effect"

    def useItem(self, player):
        print(f"{player} used {self.name}, enemy healing reduced by {self.effectValue}%")


# 3. Hunter Strike
class hunterStrike(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Hunter Strike"
        self.effect = "movement speed"
        self.effectValue = 30
        self.description = "Increase movement speed temporarily"

    def useItem(self, player):
        print(f"{player} used {self.name}, movement speed increased by {self.effectValue}")


# 4. Blade of Despair
class bladeOfDespair(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Blade of Despair"
        self.effect = "physical attack"
        self.effectValue = 160
        self.description = "Massive physical attack boost"

    def useItem(self, player):
        print(f"{player} used {self.name}, physical attack increased by {self.effectValue}")


# 5. Endless Battle
class endlessBattle(itemDefault):
    def __init__(self):
        super().__init__()
        self.name = "Endless Battle"
        self.effect = "true damage & lifesteal"
        self.effectValue = 70
        self.description = "Gain true damage and lifesteal"

    def useItem(self, player):
        print(f"{player} used {self.name}, gained true damage and lifesteal {self.effectValue}")