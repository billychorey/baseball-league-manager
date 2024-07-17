# tests/test_player.py
import pytest
from models.player import Player
from models.team import Team
from models import CURSOR, CONN

def setup_module(module):
    Team.create_table()
    Player.create_tables()

    # Insert a test team to avoid foreign key issues
    sql = "INSERT INTO teams (id, name, coach) VALUES (?, ?, ?)"
    CURSOR.execute(sql, (1, "Test Team", "Test Coach"))
    CONN.commit()

def teardown_module(module):
    Player.drop_table()
    Team.drop_table()

def test_player_creation():
    player = Player(name="John Doe", position="Pitcher", team_id=1)
    assert player.name == "John Doe"
    assert player.position == "Pitcher"
    assert player.team_id == 1

def test_player_update():
    player = Player(name="John Doe", position="Pitcher", team_id=1)
    player.name = "Jane Doe"
    player.position = "Catcher"
    assert player.name == "Jane Doe"
    assert player.position == "Catcher"
