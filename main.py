#!/usr/bin/env python

import Scenario
import Perso
import utils

if __name__ == "__main__":
    utils.clear()
    utils.splash()
    c = input("o-]===> ")
    utils.clear()
    if c == "1":
        print("Mode non disponible")
    elif c == "2":
        Scenario.Scenario(Perso.Perso(), 0)
