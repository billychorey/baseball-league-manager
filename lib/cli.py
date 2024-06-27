from models.team import Team
from models.player import Player

def display_teams():
    while True:
        teams = Team.get_all()
        Team.display_teams(teams)
        print("\n- Select a team by number")
        print("- 'A' to add a team")
        print("- 'B' to go back")
        print("- 'E' to exit")
        choice = input("Enter your choice: ").lower()
        if choice == 'a':
            add_team()
        elif choice == 'b':
            return
        elif choice == 'e':
            exit()
        else:
            try:
                manage_team(teams[int(choice) - 1])
            except (IndexError, ValueError):
                print("Invalid choice. Please try again.")

def add_team():
    name = input("\nEnter team name: ")
    coach = input("Enter coach name: ")
    team = Team.create(name, coach)
    print(f"Team {team.name} added.")

def manage_team(team):
    while True:
        print(f"Selected Team: {team.name} - Coach: {team.coach}")
        print("************************************")
        print("1. View players")
        print("2. Add player")
        print("3. Edit team")
        print("4. Delete team")
        print("B. Go back")
        print("E. Exit")

        choice = input("\nChoose an option: ").lower()
        if choice == '1':
            view_players(team)
        elif choice == '2':
            add_player(team)
        elif choice == '3':
            edit_team(team)
        elif choice == '4':
            delete_team(team)
            return  # Go back to the previous menu after deleting the team
        elif choice == 'b':
            return
        elif choice == 'e':
            exit()
        else:
            print("Invalid choice. Please try again.")

def handle_player_selection(players, team):
    while True:
        choice = input("\nSelect a player by number or 'B' to go back: ").lower()
        if choice == 'b':
            return "back"
        try:
            if manage_player(players[int(choice) - 1], team) == "back":
                return "back"
        except (IndexError, ValueError):
            print("Invalid choice. Please try again.")

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
            edit_player(player)
        elif choice == '2':
            delete_player(player)
            return "back"  # Go back to the previous menu after deleting the player
        elif choice == 'b':
            return "back"
        elif choice == 'e':
            exit()
        else:
            print("Invalid choice. Please try again.")

def edit_player(player):
    print(f"\nEditing Player: {player.name}")
    new_name = input("Enter new name (leave blank to keep current): ")
    new_position = input("Enter new position (leave blank to keep current): ")

    if new_name:
        player.name = new_name
    if new_position:
        player.position = new_position

    player.save()
    print("\nPlayer details updated.")

def delete_player(player):
    player.delete()
    print("\nPlayer deleted.")

def view_players(team):
    while True:
        players = team.players()
        if not players:
            print("\nNo players in this team.")
            print("1. Add player")
            print("B. Go back")
            choice = input("Choose an option: ").lower()
            if choice == '1':
                add_player(team)
            elif choice == 'b':
                return
            else:
                print("Invalid choice. Please try again.")
        else:
            for i, player in enumerate(players, start=1):
                print(f"{i}. {player.name} - Position: {player.position}")
            if handle_player_selection(players, team) == "back":
                return

def add_player(team):
    name = input("\nEnter player name: ")
    position = input("Enter player position: ")
    player = Player.create(name, position, team.id)
    print(f"Player {player.name} added to team {team.name}.")

def edit_team(team):
    print(f"\nEditing Team: {team.name}")
    new_name = input("Enter new team name (leave blank to keep current): ")
    new_coach = input("Enter new coach name (leave blank to keep current): ")

    if new_name:
        team.name = new_name
    if new_coach:
        team.coach = new_coach

    team.save()
    print("Team details updated.")

def delete_team(team):
    team.delete()
    print("Team deleted.")
    return  # Go back to the previous menu after deleting the team

def cli():
    while True:
        print("1. Type T or t to view all teams")
        print("2. Type E or e to exit")

        choice = input("Choose an option: ").lower()
        if choice == 't':
            display_teams()
        elif choice == 'e':
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli()
