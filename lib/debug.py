#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.team import Team
from models.player import Player


def reset_database():
    Player.drop_table()
    Team.drop_table()
    Team.create_table()
    Player.create_tables()

   


breakpoint()
#not using ipdb because of deprecation concerns