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
        print("2. Type E or e to exit")
        choice = get_choice("\nChoose an option: ")

        if choice == 't':
            display_teams()
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
                return  # Exit the display_teams function if no team is added
            else:
                print("Invalid choice, please try again.")
        else:
            list_teams()  # Assuming list_teams() prints all teams with formatting
            print("\n- Select a team by number")
            print("- 'A' to add a team")
            print("- 'B' to go back")
            print("- 'E' to exit")

            choice = get_choice("Enter your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(teams):
                manage_team(teams[int(choice) - 1])
            elif choice == 'a':
                create_team()
                continue  # Ensure the updated list is displayed after adding a team
            elif choice == 'b':
                break  # Break the while loop to return to the main menu
            elif choice == 'e':
                exit_program()
            else:
                print("Invalid choice, please try again.")

def handle_team_selection(teams):
    while True:
        choice = get_choice("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(teams):
            manage_team(teams[int(choice) - 1])
        elif choice == 'a':
            create_team()
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

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
        print("B. Go back")
        print("E. Exit")
        choice = get_choice("\nChoose an option: ")

        if choice == '1':
            view_players(team)
        elif choice == '2':
            update_team(team)
        elif choice == '3':
            if delete_team(team) is None:
                return
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")
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
        choice = get_choice("Would you like to add a player? (y/n): ")
        if choice == 'y':
            create_player(team.id)
        elif choice == 'n':
            return
        else:
            print("Invalid choice, please try again.")
    else:
        print("Team Players:")
        list_players(team.id)
        print("\nSelect a player by number, 'B' to go back, 'E' to exit:")
        handle_player_selection(team.players(), team)

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

def manage_player(player):
    print(f"\nSelected Player: {player.name} - Position: {player.position}")
    print("1. Edit player")
    print("2. Delete player")
    print("B. Go back")
    print("E. Exit")
    choice = get_choice("\nChoose an option: ")

    if choice == '1':
        update_player(player)
    elif choice == '2':
        delete_player(player)
    elif choice == 'b':
        return
    elif choice == 'e':
        exit_program()
    else:
        print("Invalid choice, please try again.")

if __name__ == "__main__":
    cli()



#prop methods look at requirements!!! 
#should organize files.... helpers.
#need pipfile readme pipfile 
#name cli not main



