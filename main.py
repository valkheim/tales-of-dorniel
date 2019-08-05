#!/usr/bin/env python

import Scenario
import Perso
import utils as u

if __name__ == "__main__":
    u.clear()
    u.splash()
    c = input("o-]===> ")
    u.clear()
    if c == "1":
        print("Mode non disponible")
    elif c == "3":
        pass
    else:
        u.game_init()
        Scenario.Scenario(Perso.Perso(), 0)
