from models.team import Team
from models.player import Player
        
def list_teams(teams):
    header = "Current League Teams"
    border = "*" * len(header)
    print(header)
    print(border)
    for i, team in enumerate(teams, start=1):
        print(f"{i}. {team.name} - Coach: {team.coach}")

def add_team():
    name = input("\nEnter team name: ")
    coach = input("Enter coach name: ")
    team = Team.create(name, coach)
    print(f"Team {team.name} added.")
    
def update_team(team):
    new_name = input(f"Enter new name for team {team.name} (or press enter to keep current): ") or team.name
    new_coach = input(f"Enter new coach for team {team.name} (or press enter to keep current): ") or team.coach
    team.name = new_name
    team.coach = new_coach
    team.save()
    print(f"Team {team.name} updated successfully.")

def delete_team(team):
    while True:
        confirmation = input(f"Are you sure you want to delete the team {team.name}? (y/n): ").lower()
        if confirmation == 'y':
            team.delete()
            print(f"\nTeam {team.name} deleted successfully.\n")
            return None
        elif confirmation == 'n':
            return team
        else:
            print("Invalid choice. Please select 'y' or 'n'.")
            choice = input("Press 'B' to go back or 'E' to exit: ").lower()
            if choice == 'b' or choice == 'n':
                return team
            elif choice == 'e':
                exit_program()
                
def view_players(team):
    players = team.players()
    if not players:
        print("\nNo players in this team.")
    else:
        for i, player in enumerate(players, start=1):
            print(f"{i}. {player.name} - Position: {player.position}")

def create_player(team_id):
    name = input("Enter player name: ")
    position = input("Enter player position: ")
    Player.create(name, position, team_id)
    print(f"Player {name} created successfully.")

def update_player(player):
    new_name = input(f"Enter new name for player {player.name} (or press enter to keep current): ") or player.name
    new_position = input(f"Enter new position for player {player.position} (or press enter to keep current): ") or player.position
    player.name = new_name
    player.position = new_position
    player.save()
    print(f"Player {player.name} updated successfully.")

def delete_player(player):
    while True:
        confirmation = input(f"Are you sure you want to delete the player {player.name}? (y/n): ").lower()
        if confirmation == 'y':
            player.delete()
            print(f"Player {player.name} deleted successfully.")
            return None
        elif confirmation == 'n':
            return player
        else:
            print("Invalid choice. Please select 'y' or 'n'.")
            choice = input("Press 'B' to go back or 'E' to exit: ").lower()
            if choice == 'b' or choice == 'n':
                return player
            elif choice == 'e':
                exit_program()

def exit_program():
    print("Exiting program. Goodbye!")
    exit()
 