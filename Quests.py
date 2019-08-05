class Quest():
    def __init__(self, name, goal, description):
        self.name = name
        self.goal = goal
        self.description = description

        self.accomplished = False

    def __repr__(self):
        if self.accomplished:
            tick = '[x]'
        else:
            tick = '[ ]'
        return "{} {}\n{}".format(tick, self.name, self.description)

class MainQuest(Quest):
    def __init__(self):
        name = "La paix entre les peuples"
        goal = "Rapporter la paix entre les peuples de Dorniel."
        description = """
            En retrouvant le trésor de notre bon roi, on me couvrira de
            richesses. Et on tuera probablement le larcineur, m'enfin...
            """
        super().__init__(name, goal, description)

    def __repr__(self):
        return super().__repr__()

class Quests():
    def __init__(self):
        self.quests = []

    def add(self, quest):
        self.quests.append(quest())

    def get(self):
        return self.quests
