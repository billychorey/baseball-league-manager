from models.team import Team
from models.player import Player

def exit_program():
    print("Goodbye!")
    exit()

def list_teams():
    teams = Team.get_all()
    for index, team in enumerate(teams):
        print(f"{index + 1}. {team.name} - Coach: {team.coach}")

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
    try:
        confirm = input(f"Are you sure you want to delete {team.name}? (y/n): ")
        if confirm.lower() == 'y':
            team.delete()  # This calls the delete method on the team instance
            print(f"Team {team.name} deleted successfully.")
            return None  # Return None to signify the team has been successfully deleted
        else:
            print("Deletion canceled.")
            return team  # Return the team instance if deletion was not confirmed
    except Exception as e:
        print(f"Failed to delete team: {e}")
        return team  # Return the team instance if an error occurs during deletion


def list_players(team_id):
    players = Player.get_players_by_team_id(team_id)
    for index, player in enumerate(players):
        print(f"{index + 1}. {player.name} - Position: {player.position}")

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
