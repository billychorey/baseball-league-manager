from models.team import Team
from models.player import Player
from decorators import case_insensitive_input
from helpers import (
    exit_program, list_teams, create_team, 
    update_team, delete_team, list_players, 
    create_player, update_player, delete_player
)

@case_insensitive_input
def get_choice(prompt):
    return input(prompt)

def cli():
    Team.create_tables()
    Player.create_tables()
    print("Tables created successfully")

    while True:
        print("\n1. Type T or t to view all teams")
        print("2. Type F or f to find a team by name")
        print("3. Type E or e to exit")
        choice = get_choice("\nChoose an option: ")

        if choice == 't':
            display_teams()
        elif choice == 'f':
            find_team_by_name()
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")
            
def display_teams():
    while True:
        teams = Team.get_all()
        if not teams:
            print("No teams in database")
            choice = get_choice("Would you like to add a team? (y/n): ")
            if choice == 'y':
                create_team()
            elif choice == 'n':
                return
            else:
                print("Invalid choice, please try again.")
        else:
            list_teams()
            print("\n- Select a team by number")
            print("- 'A' to add a team")
            print("- 'B' to go back")
            print("- 'E' to exit")

            choice = get_choice("Enter your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(teams):
                manage_team(teams[int(choice) - 1])
            elif choice == 'a':
                create_team()
                continue
            elif choice == 'b':
                break
            elif choice == 'e':
                exit_program()
            else:
                print("Invalid choice, please try again.")

def find_team_by_name():
    name = get_choice("Enter the team name (case insensitive): ")
    team = Team.find_by_name(name)
    if team:
        manage_team(team)
    else:
        print("No team found with that name.")

def manage_team(team):
    while True:
        if not team:
            print("Team has been deleted or is not available.")
            return

        print(f"\nSelected Team: {team.name} - Coach: {team.coach}")
        print("************************************")
        print("\n1. View players")
        print("2. Edit team")
        print("3. Delete team")
        print("4. Find player by name")
        print("B. Go back")
        print("E. Exit")
        choice = get_choice("\nChoose an option: ")

        if choice == '1':
            view_players(team)
        elif choice == '2':
            update_team(team)
        elif choice == '3':
            deleted_team = delete_team(team)  # This will handle the confirmation
            if deleted_team is None:
                print("Team deleted successfully.")
                return  # Exit manage_team as the team no longer exists
        elif choice == '4':
            find_player_in_team(team)
        elif choice == 'b':
            return  # Exit manage_team to go back to the previous menu
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

def view_players(team):
    players = team.players()
    if not players:
        print("No players currently associated with this team.")
        while True:  # Adding a loop for valid input handling
            choice = get_choice("Would you like to add a player? (y/n): ")
            if choice == 'y':
                create_player(team.id)
                break  # Break after creating player to avoid looping
            elif choice == 'n':
                break  # Break if no player is to be added
            else:
                print("Invalid choice, please try again.")
    else:
        print("Team Players:")
        list_players(team.id)  # Assuming this function prints each player nicely
        handle_player_selection(players, team)

def handle_player_selection(players, team):
    while True:
        choice = get_choice("Select a player by number or 'B' to go back: ")
        if choice.isdigit() and 1 <= int(choice) <= len(players):
            manage_player(players[int(choice) - 1])
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

def find_player_in_team(team):
    name = get_choice("Enter the player's name (case insensitive): ")
    players = team.players()
    player = next((p for p in players if p.name.lower() == name.lower()), None)
    if player:
        manage_player(player)
    else:
        print("No player found with that name in this team.")

def manage_player(player):
    while True:
        if not player:
            print("Player has been deleted or is not available.")
            return

        print(f"\nSelected Player: {player.name} - Position: {player.position}")
        print("************************************")
        print("\n1. Edit player")
        print("2. Delete player")
        print("3. View team")
        print("B. Go back")
        print("E. Exit")
        choice = get_choice("\nChoose an option: ")

        if choice == '1':
            update_player(player)
        elif choice == '2':
            delete_player(player)
        elif choice == '3':
            view_team(player.team)
        elif choice == 'b':
            return  # Exit manage_player to go back to the previous menu
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

def view_team(team):
    print(f"Team: {team.name}, Coach: {team.coach}")
    print("Players:")
    view_players(team)

if __name__ == "__main__":
    cli()


#prop methods look at requirements!!! 
#should organize files.... helpers.
#need pipfile readme pipfile 
#name cli not main



