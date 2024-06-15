from models.team import Team
from models.player import Player
from helpers import (
    exit_program, list_teams, find_team_by_name, find_team_by_id,
    create_team, update_team, delete_team, list_players, find_player_by_name,
    find_player_by_id, create_player, update_player, delete_player, list_team_players
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
        choice = input("Would you like to add a team? (y/n): ")
        if choice.lower() == 'y':
            create_team()
        elif choice.lower() == 'n':
            return
        else:
            print("Invalid choice, please try again.")
    else:
        for index, team in enumerate(teams):
            print(f"{index + 1}. {team.name} - Coach: {team.coach}")
        print("\n- Select a team by number")
        print("- 'A' to add a team")
        print("- 'B' to go back")
        print("- 'E' to exit")

        handle_team_selection(teams)

def handle_team_selection(teams):
    choice = input().lower()
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
        handle_team_selection(teams)

def manage_team(team):
    while True:
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
            delete_team(team)
            break
        elif choice == 'b':
            break
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

def view_players(team):
    players = team.players()
    if not players:
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
        for index, player in enumerate(players):
            print(f"{index + 1}. {player.name} - Position: {player.position}")
        print("\nSelect a player by number, 'B' to go back, 'E' to exit:")

        handle_player_selection(players, team)

def handle_player_selection(players, team):
    choice = input().lower()
    if choice.isdigit() and 1 <= int(choice) <= len(players):
        manage_player(players[int(choice) - 1])
    elif choice == 'b':
        manage_team(team)
    elif choice == 'e':
        exit_program()
    else:
        print("Invalid choice, please try again.")
        handle_player_selection(players, team)

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



