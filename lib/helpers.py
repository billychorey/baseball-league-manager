from models.team import Team
from models.player import Player

def exit_program():
    print("Goodbye!")
    exit()

def list_teams():
    teams = Team.get_all()
    for team in teams:
        print(team)

def find_team_by_name():
    name = input("Enter the team's name: ")
    team = Team.find_by_name(name)
    print(team) if team else print(f'Team {name} not found')

def find_team_by_id():
    id_ = input("Enter the team's id: ")
    team = Team.find_by_id(id_)
    print(team) if team else print(f'Team {id_} not found')

def create_team():
    name = input("Enter the team's name: ")
    coach = input("Enter the coach's name: ")
    try:
        team = Team.create(name, coach)
        print(f'Success: Team {team.id} - "{team.name}" coached by {team.coach} has been added.')
    except Exception as exc:
        print("Error creating team: ", exc)

def update_team(team):
    new_name = input(f"Enter new team name (or press Enter to keep '{team.name}'): ")
    new_coach = input(f"Enter new coach name (or press Enter to keep '{team.coach}'): ")
    team.name = new_name if new_name else team.name
    team.coach = new_coach if new_coach else team.coach
    team.save()
    print("Team updated!")

def delete_team(team):
    team.delete()
    print(f'Team {team.id} deleted')

def list_players():
    players = Player.get_all()
    for player in players:
        print(player)

def find_player_by_name():
    name = input("Enter the player's name: ")
    player = Player.find_by_name(name)
    print(player) if player else print(f'Player {name} not found')

def find_player_by_id():
    id_ = input("Enter the player's id: ")
    player = Player.find_by_id(id_)
    print(player) if player else print(f'Player {id_} not found')

def create_player(team_id):
    name = input("Enter the player's name: ")
    position = input("Enter the player's position: ")
    try:
        player = Player.create(name, position, team_id)
        print(f'Success: Player "{player.name}" (Position: {player.position}) added to {player.team.name}.')
    except Exception as exc:
        print("Error creating player: ", exc)

def update_player(player):
    new_name = input(f"Enter new player name (or press Enter to keep '{player.name}'): ")
    new_position = input(f"Enter new player position (or press Enter to keep '{player.position}'): ")
    player.name = new_name if new_name else player.name
    player.position = new_position if new_position else player.position
    player.save()
    print("Player updated!")

def delete_player(player):
    player.delete()
    print(f'Player {player.id} deleted')

def list_team_players(team):
    players = team.players()
    for player in players:
        print(player)
