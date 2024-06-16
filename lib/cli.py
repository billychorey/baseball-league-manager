from models.team import Team
from models.player import Player
from helpers import (
    exit_program, list_teams,create_team, 
    update_team, delete_team, list_players, 
    create_player, update_player, delete_player
     
    
)

def cli():
    Team.create_tables()
    Player.create_tables()
    print("Tables created successfully")

    while True:
        print("\n1. Type T or t to view all teams")
        print("2. Type E or e to exit")
        choice = input("\nChoose an option: ").lower()

        if choice == 't':
            display_teams()
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

def display_teams():
    teams = Team.get_all()
    if not teams:
        print("No teams in database")
        while True:
            choice = input("Would you like to add a team? (y/n): ").lower()
            if choice == 'y':
                create_team()
                break  # Break after team creation to allow new teams to be displayed
            elif choice == 'n':
                return
            else:
                print("Invalid choice, please try again.")
    else:
        list_teams()  # Assuming list_teams() prints all teams with formatting
        print("\n- Select a team by number")
        print("- 'A' to add a team")
        print("- 'B' to go back")
        print("- 'E' to exit")

        handle_team_selection(teams)


def handle_team_selection(teams):
    while True:
        choice = input().lower()
        if choice.isdigit() and 1 <= int(choice) <= len(teams):
            action = manage_team(teams[int(choice) - 1])
            if action != 'continue':
                return action
        elif choice == 'a':
            create_team()
        elif choice == 'b':
            return 'break'
        elif choice == 'e':
            exit_program()
            return 'exit'
        else:
            print("Invalid choice, please try again.")

def manage_team(team):
    while True:
        if not team:
            print("Team has been deleted or is not available.")
            return 'break'

        print(f"\nSelected Team: {team.name} - Coach: {team.coach}")
        print("************************************")
        print("\n1. View players")
        print("2. Edit team")
        print("3. Delete team")
        print("B. Go back")
        print("E. Exit")
        choice = input("\nChoose an option: ").lower()

        if choice == '1':
            view_players(team)
        elif choice == '2':
            update_team(team)
        elif choice == '3':
            if delete_team(team) is None:
                print("Team deleted successfully.")
                return 'break'
        elif choice == 'b':
            return 'break'
        elif choice == 'e':
            exit_program()
            return 'exit'
        else:
            print("Invalid choice, please try again.")

def view_players(team):
    if not team.players():
        print("No players currently associated with this team.")
        choice = input("Would you like to add a player? (y/n): ").lower()
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
    while True:  # Adding a loop to handle repeated inputs correctly
        choice = input().lower()
        if choice.isdigit() and 1 <= int(choice) <= len(players):
            manage_player(players[int(choice) - 1])
        elif choice == 'b':
            # If 'b' is pressed, break this loop and return to manage team or previous menu
            return 'break'
        elif choice == 'e':
            exit_program()
            return 'exit'  # Make sure to handle 'exit' properly if you have a loop above this
        else:
            print("Invalid choice, please try again.")

def manage_player(player):
    print(f"\nSelected Player: {player.name} - Position: {player.position}")
    print("1. Edit player")
    print("2. Delete player")
    print("B. Go back")
    print("E. Exit")
    choice = input("\nChoose an option: ").lower()

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



