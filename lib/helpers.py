from models.team import Team
from models.player import Player

def find_by_attribute(object_list, attribute, value):
    return [obj for obj in object_list if hasattr(obj, attribute) and getattr(obj, attribute).lower() == value.lower()]

def find_team_by_name(teams, name):
    return find_by_attribute(teams, "name", name)

def find_player_by_name(players, name):
    return find_by_attribute(players, "name", name)


def display_all_teams():
    teams = Team.get_all()
    header = "\nCurrent League Teams"
    border = "*" * len(header)
    print(header)
    print(border)
    for i, team in enumerate(teams, start=1):
        print(f"{i}. {team.name} - Coach: {team.coach}")

def create_team():
    name = input("\nEnter team name: ")
    coach = input("\nEnter coach name: ")
    try:
        team = Team.create(name, coach)
        print(f"Team {team.name} added.")
    except Exception as exc:
        print("Error creating team: ", exc)

def update_team(team):
    try:
        new_name = input(f"\nEnter new name for team {team.name} (or press enter to keep current): ") or team.name
        team.name = new_name
        new_coach = input(f"\nEnter new coach for team {team.name} (or press enter to keep current): ") or team.coach
        team.coach = new_coach
        team.update()
        print(f"Team {team.name} updated successfully.")
    except Exception as exc:
        print("Error updating team: ", exc)

def delete_team(team):
    while True:
        confirmation = input(f"\nAre you sure you want to delete the team {team.name}? (y/n): ").lower()
        if confirmation == 'y':
            team.delete()
            print(f"\nTeam {team.name} deleted successfully.\n")
            return
        elif confirmation == 'n':
            return
        else:
            print("\nInvalid choice. Please select 'y' or 'n'.")
            choice = input("Press 'B' to go back or 'E' to exit: ").lower()
            if choice == 'b' or choice == 'n':
                return
            elif choice == 'e':
                exit_program()

def display_all_players(team):
    players = team.players()
    if not players:
        print("\nNo players in this team.")
    else:
        for i, player in enumerate(players, start=1):
            print(f"{i}. {player.name} - Position: {player.position}")

def create_player(team_id):
    name = input("\nEnter player name: ")
    position = input("\nEnter player position: ")
    try:
        player = Player.create(name, position, team_id)
        print(f"Player {name} created successfully.")
    except Exception as exc:
        print("Error creating player: ", exc)

def update_player(player):
    try:
        new_name = input(f"\nEnter new name for player {player.name} (or press enter to keep current): ") or player.name
        new_position = input(f"\nEnter new position for player {player.name} (or press enter to keep current): ") or player.position
        player.name = new_name
        player.position = new_position
        player.update()
        print(f"\nPlayer {player.name} updated successfully.")
    except Exception as exc:
        print("Error updating player: ", exc)

def delete_player(player):
    while True:
        confirmation = input(f"\nAre you sure you want to delete the player {player.name}? (y/n): ").lower()
        if confirmation == 'y':
            player.delete()
            print(f"\nPlayer {player.name} deleted successfully.\n")
            return
        elif confirmation == 'n':
            return
        else:
            print("\nInvalid choice. Please select 'y' or 'n'.")
            choice = input("Press 'B' to go back or 'E' to exit: ").lower()
            if choice == 'b' or choice == 'n':
                return
            elif choice == 'e':
                exit_program()

def exit_program():
    print("Exiting program. Goodbye!")
    exit()
