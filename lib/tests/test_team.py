# tests/test_team.py
import pytest
from models.team import Team
from models import CURSOR, CONN

def setup_module(module):
    Team.create_table()

def teardown_module(module):
    Team.drop_table()

def test_team_creation():
    team = Team(name="Dodgers", coach="Mike")
    assert team.name == "Dodgers"
    assert team.coach == "Mike"

def test_team_update():
    team = Team(name="Dodgers", coach="Mike")
    team.name = "Giants"
    team.coach = "John"
    assert team.name == "Giants"
    assert team.coach == "John"
