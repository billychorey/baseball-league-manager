from models.team import Team
from models.player import Player


def exit_program():
    print("Goodbye!")
    exit()



def list_teams():
    teams = Team.get_all()
    for department in teams:
        print(department)


def find_team_by_name():
    name = input("Enter the team's name: ")
    team = Team.find_by_name(name)
    print(team) if team else print(
        f'Team {name} not found')
    
def find_team_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the team's id: ")
    team = Team.find_by_id(id_)
    print(team) if team else print(f'Team {id_} not found')

def create_team():
    name = input("Enter the team's name: ")
    location = input("Enter the team's location: ")
    try:
        team = Team.create(name, location)
        print(f'Success: {team}')
    except Exception as exc:
        print("Error creating team: ", exc)

def update_team():
    id_ = input("Enter the team's id: ")
    if team := Team.find_by_id(id_):
        try:
            name = input("Enter the team's new name: ")
            team.name = name
            location = input("Enter the team's new location: ")
            team.location = location

            team.update()
            print(f'Success: {team}')
        except Exception as exc:
            print("Error updating team: ", exc)
    else:
        print(f'Team {id_} not found')

def delete_team():
    id_ = input("Enter the team's id: ")
    if team := Team.find_by_id(id_):
        team.delete()
        print(f'Team {id_} deleted')
    else:
        print(f'Team {id_} not found')



def list_players():
    pass
    players = Player.get_all()
    for player in players:
        print(player)

def find_player_by_name():
    name = input("Enter the player's name: ")
    player = Player.find_by_name(name)
    print(player) if player else print(
        f'Player {name} not found')


def find_player_by_id():
    id_ = input("Enter the player's id: ")
    player = Player.find_by_id(id_)
    print(player) if player else print(f'{Player} {id_} not found')


def create_player():
    name = input("Enter the player's name: ")
    location = input("Enter the player's location: ")
    try:
        player = Player.create(name, location)
        print(f'Success: {player}')
    except Exception as exc:
        print("Error creating player: ", exc)

def update_player():
    id_ = input("Enter the player's id: ")
    if player := Player.find_by_id(id_):
        try:
            name = input("Enter the player's new name: ")
            player.name = name
            location = input("Enter the player's new location: ")
            player.location = location

            player.update()
            print(f'Success: {player}')
        except Exception as exc:
            print("Error updating player: ", exc)
    else:
        print(f'Player {id_} not found')


def delete_player():
    id_ = input("Enter the player's id: ")
    if player := Player.find_by_id(id_):
        player.delete()
        print(f'Player {id_} deleted')
    else:
        print(f'Player {id_} not found')


def list_team_players():
    id_ = input("Enter the player's id: ")
    team = Team.find_by_id(id_)
    
    if team:
        players = team.players()
        for player in players:
            print(player)
    else:
        print(f'Team {id_} not found')
