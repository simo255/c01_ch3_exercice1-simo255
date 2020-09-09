#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
def square_root(number: int) -> float:
    # TODO completer la fonction

    sqrt=input('veuillez entrer un nombre dont vous voulez calculer la racine carrée : ')
    s= math.sqrt(int(sqrt))
    print('le resulteat est', s)

def square(number: int) -> int:
    # TODO completer la fonction
    pow=input('veuillez entrer un nombre dont vous voulez calculer le carré : ')
    r= math.pow(int(pow), 2)
    print('le resultat est', r)


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
