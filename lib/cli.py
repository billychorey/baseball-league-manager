from models.team import Team
from models.player import Player
from helpers import (
    find_team_by_name,
    find_player_by_name,
    display_all_teams,
    create_team,
    display_all_players,
    display_team_players,
    update_team,
    delete_team,
    create_player,
    update_player,
    delete_player,
    exit_program
)

def cli():
    while True:
        print("\n1. Type P or p to view all players")
        print("2. Type T or t to view all teams")
        print("3. Type S or s to search for a team by name")
        print("4. Type E or e to exit")

        choice = input("\nChoose an option: ").lower()
        if choice == 't':
            teams_loop()
        elif choice == 's':
            search_team()
        elif choice == 'e':
            exit_program()
        elif choice == 'p':
            display_all_players()
        else:
            print("\nInvalid choice. Please try again.")

def search_team():
    name = input("Enter the team name: ")
    teams = find_team_by_name(Team.get_all(), name)
    if teams:
        for team in teams:
            print(f"Found Team: {team.name}")
            manage_team(team)
    else:
        print("No teams found with that name.")

def teams_loop():
    while True:
        display_all_teams()
        print("\n- Select a team by number")
        print("- 'A' to add a team")
        print("- 'B' to go back")
        print("- 'E' to exit")
        choice = input("Enter your choice: ").lower()
        if choice == 'a':
            create_team()
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            teams = Team.get_all()
            try:
                manage_team(teams[int(choice) - 1])
            except (IndexError, ValueError):
                print("Invalid choice. Please try again.")

def manage_team(team):
    while True:
        print(f"\nSelected Team: {team.name} - Coach: {team.coach}")
        print("************************************")
        print("1. View players")
        print("2. Add player")
        print("3. Edit team")
        print("4. Delete team")
        print("5. Search for player by name")
        print("B. Go back")
        print("E. Exit")

        choice = input("\nChoose an option: ").lower()
        if choice == '1':
            view_players_and_manage(team)
        elif choice == '2':
            create_player(team.id)
        elif choice == '3':
            update_team(team)
        elif choice == '4':
            delete_team(team)
            return
        elif choice == '5':
            search_player_within_team(team)
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("\nInvalid choice. Please try again.")

def search_player_within_team(team):
    name = input("\nEnter the player name: ")
    players = find_player_by_name(team.players(), name)
    if players:
        for player in players:
            print(f"\nFound Player: {player.name}")
            manage_player(player, team)
    else:
        print("\nNo players found with that name in this team.")

def view_players_and_manage(team):
    while True:
        print("\nCurrent Roster:\n")
        display_team_players(team)
        print("************************************")
        print("Select a player by number")
        print("A. Add player")
        print("B. Go back")
        print("E. Exit")
        choice = input("Choose an option: ").lower()
        if choice == 'a':
            create_player(team.id)
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            try:
                players = team.players()
                manage_player(players[int(choice) - 1], team)
            except (IndexError, ValueError):
                print("\nInvalid choice. Please try again.")

def manage_player(player, team):
    while True:
        print(f"\nSelected Player: {player.name} - Position: {player.position}")
        print("************************************")
        print("1. Edit player")
        print("2. Delete player")
        print("B. Go back")
        print("E. Exit")

        choice = input("Choose an option: ").lower()
        if choice == '1':
            update_player(player)
        elif choice == '2':
            delete_player(player)
            return
        elif choice == 'b':
            return
        elif choice == 'e':
            exit_program()
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    cli()
