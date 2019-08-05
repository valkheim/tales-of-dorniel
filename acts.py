import utils as u

def acts(self):
    return [
        [
            [ [ u.gf("acts/0/scenarios/1").format(self.perso.name), True ] ],
            [
                [ u.gf("acts/0/questions/1"), 1 ],
                [ u.gf("acts/0/questions/2"), 1 ],
                [ u.gf("acts/0/questions/3"), 1 ]
            ]
        ],
        [
            [ [ u.gf("acts/1/scenarios/1").format(self.perso.life,
                self.perso.stamina, self.perso.magic, self.perso.attack,
                self.perso.defense, self.perso.strength, self.perso.armour,
                self.perso.intelligence, self.perso.archery, self.perso.invocation,
                self.perso.destruction, self.perso.potion, self.perso.heal), True ] ],
            [
                [ u.gf("acts/transversal/yes"), 2 ],
                [ u.gf("acts/transversal/no"), 0 ]
            ]
        ],
        [
            [ [ u.gf("acts/2/scenarios/1"), True ] ],
            [ [ None, 3 ] ]
        ],
        [
            [
                [ u.gf("acts/3/scenarios/1"), True ],
                [ u.gf("draw/crosses/hautegarde"), False ]
            ],
            [
                [ u.gf("acts/3/questions/1"), 3 ],
                [ u.gf("acts/3/questions/2"), 3 ],
                [ u.gf("acts/3/questions/3"), 3 ]
            ]
        ]
    ]
