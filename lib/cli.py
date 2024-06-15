from decorators import case_insensitive_input
from models.team import Team
from models.player import Player

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def display_teams():
    teams = Team.get_all()
    if not teams:
        print("No teams in database")
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
        add_team()
    elif choice == 'b':
        return
    elif choice == 'e':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice, please try again.")

def add_team():
    name = input("Enter team name: ")
    coach = input("Enter coach name: ")
    if name and coach:
        Team.create(name, coach)
        print("Team added!")
    else:
        print("Both team name and coach name are required.")

def manage_team(team):
    while True:
        print(f"\nSelected Team: {team.name} - Coach: {team.coach}")
        print("1. View players")
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
            break  # Return to team list after deletion
        elif choice == 'b':
            break
        elif choice == 'e':
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice, please try again.")

def update_team(team):
    new_name = input(f"Enter new team name (or press Enter to keep '{team.name}'): ")
    new_coach = input(f"Enter new coach name (or press Enter to keep '{team.coach}'): ")
    if new_name:
        team.name = new_name
    if new_coach:
        team.coach = new_coach
    team.save()
    print("Team updated!")
    print(f"Team name: {team.name}")
    print(f"Team coach: {team.coach}")

def delete_team(team):
    confirm = input("Are you sure you want to delete this team? (y/n): ")
    if confirm.lower() == 'y':
        team.delete()
        print(f"Team {team.name} deleted!")

def view_players(team):
    players = team.players()
    if not players:
        print("No players currently associated with this team.")
        print("Would you like to add a player? (y/n): ")
        if input().lower() == 'y':
            add_player(team.id)
    else:
        for index, player in enumerate(players):
            print(f"{index + 1}. {player.name} - Position: {player.position}")
        print("\n- Select a player by number")
        print("- 'B' to go back")
        print("- 'E' to exit")

        handle_player_selection(players, team)

def add_player(team_id):
    # Fetch the team first to check if it's valid
    team = Team.find_by_id(team_id)
    if not team:
        print("Invalid team specified. Please check the team ID.")
        return  # Exit the function if no valid team is found

    name = input("Enter player name: ")
    position = input("Enter player position: ")
    if name and position:
        try:
            Player.create(name, position, team_id)
            print(f"Player '{name}' added to the team!")
        except ValueError as e:
            print(e)
    else:
        print("Both player name and position are required.")

def handle_player_selection(players, team):
    choice = input().lower()
    if choice.isdigit() and 1 <= int(choice) <= len(players):
        manage_player(players[int(choice) - 1])
    elif choice == 'b':
        manage_team(team)  # Returns to team management
    elif choice == 'e':
        print("Goodbye!")
        exit()
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
        return  # Go back to player listing
    elif choice == 'e':
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice, please try again.")

def update_player(player):
    new_name = input(f"Enter new player name (or press Enter to keep '{player.name}'): ")
    new_position = input(f"Enter new player position (or press Enter to keep '{player.position}'): ")
    player.name = new_name if new_name else player.name
    player.position = new_position if new_position else player.position
    player.save()
    print("Player updated!")

def delete_player(player):
    confirm = input("Are you sure you want to delete this player? (y/n): ")
    if confirm.lower() == 'y':
        player.delete()
        print(f"Player {player.name} deleted!")

if __name__ == "__main__":
    cli()




#prop methods look at requirements!!! 
#should organize files.... helpers.
#need pipfile readme pipfile 
#name cli not main



