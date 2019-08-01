import utils

def acts(self):
    return [
        [
            utils.gf("acts/1/scenarios/1").format(self.perso.name),
            [
                [ utils.gf("acts/1/questions/1"), 1 ],
                [ utils.gf("acts/1/questions/2"), 1 ],
                [ utils.gf("acts/1/questions/3"), 1 ]
            ]
        ],
        [
            utils.gf("acts/2/scenario").format(self.perso),
            [
                [ utils.gf("acts/transversal/yes"), 2 ],
                [ utils.gf("acts/transversal/no"), 0 ]
            ]
        ],
        [
        ]
    ]
