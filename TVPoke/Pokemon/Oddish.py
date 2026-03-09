from TVPoke.BaseClasses.PokeTypes import Grass
from TVPoke.BaseClasses.Move import Move

class Oddish(Grass):
    def __init__(self):
        moves = [
            Move(),
            Move(),
            Move(),
            Move()
        ]
        super().__init__("Oddish", 80, moves, "https://www.clipartmax.com/png/middle/171-1711907_oddish-oddish-pokemon.png")