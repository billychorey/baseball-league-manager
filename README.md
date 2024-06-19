# ⚾ Baseball League Manager

![Baseball](lib/img/baseball.png)
*Image of Fenway park - Getty images - from [Fenway - Conde Nast Traveler](https://www.cntraveler.com/activities/boston/fenway-park)
*

Welcome to the **Baseball League Manager**! This handy app is perfect for parents, coaches, or league managers to keep track of their baseball teams and players.

## 🎯 Features

- **View Teams**: See a list of all your teams. If none exist, you can add them!
- **Edit Teams**: Change team names or coach names easily.
- **Delete Teams**: Remove teams that are no longer needed.
- **View Players**: Check out the players on each team. If there are no players, you can add them!
- **Edit Players**: Update player details as needed.
- **Delete Players**: Remove players from the team.

## 🚀 Getting Started

1. **Clone the repo**: 
    ```sh
    git clone https://github.com/yourusername/Baseball-League-Manager.git
    cd Baseball-League-Manager
    ```

2. **Set up the environment**:
    ```sh
    pipenv install
    pipenv shell
    ```

3. **Run the app**:
    ```sh
    python cli.py
    ```

## 📖 How to Use

1. **Viewing Teams**: Start by viewing the list of teams. If no teams are present, you'll have the option to add a new team.

2. **Managing Teams**: 
    - **Add Team**: Provide the team name and coach name.
    - **Edit Team**: Select a team to change its details.
    - **Delete Team**: Remove a team if it's no longer needed.

3. **Viewing Players**: Within a team, you can view the players. If no players are present, you can add them.

4. **Managing Players**:
    - **Add Player**: Provide the player's details.
    - **Edit Player**: Select a player to update their information.
    - **Delete Player**: Remove a player from the team.

## 📄 Project Structure

Here's a breakdown of the important files in the project and their roles:

### `lib/cli.py`

This is the main entry point for the CLI application. It provides an interactive menu for users to manage teams and players. 

#### Key Functions:

- **`cli()`**: The main function that runs the CLI loop and handles user input.
- **`display_teams()`**: Displays a list of all teams.
- **`find_team_by_name()`**: Allows users to find a team by its name.
- **`manage_team(team)`**: Manages operations related to a specific team, including viewing players, editing the team, deleting the team, and finding players by name.
- **`view_players(team)`**: Displays a list of players associated with a specific team.
- **`handle_player_selection(players, team)`**: Handles the selection of a player from the list of players.
- **`find_player_in_team(team)`**: Allows users to find a player by name within a specific team.
- **`manage_player(player)`**: Manages operations related to a specific player, including editing the player, deleting the player, and viewing the player's team.
- **`view_team(team)`**: Displays the details of a specific team, including its players.

### `lib/models/team.py`

Defines the `Team` class, representing a baseball team. This class includes methods for interacting with the database to create, read, update, and delete team records.

#### Key Methods:

- **`__init__(self, name, coach, id=None)`**: Initializes a new team instance.
- **`create_tables(cls)`**: Creates the teams table in the database.
- **`drop_table(cls)`**: Drops the teams table from the database.
- **`save(self)`**: Saves the team instance to the database.
- **`create(cls, name, coach)`**: Creates a new team and saves it to the database.
- **`update(self)`**: Updates the team's details in the database.
- **`delete(self)`**: Deletes the team from the database.
- **`get_all(cls)`**: Retrieves all teams from the database.
- **`find_by_id(cls, id)`**: Finds a team by its ID.
- **`find_by_name(cls, name)`**: Finds a team by its name.
- **`players(self)`**: Retrieves all players associated with the team.

### `lib/models/player.py`

Defines the `Player` class, representing a baseball player. This class includes methods for interacting with the database to create, read, update, and delete player records.

#### Key Methods:

- **`__init__(self, name, position, team, id=None)`**: Initializes a new player instance.
- **`create_tables(cls)`**: Creates the players table in the database.
- **`drop_table(cls)`**: Drops the players table from the database.
- **`save(self)`**: Saves the player instance to the database.
- **`create(cls, name, position, team_id)`**: Creates a new player and saves it to the database.
- **`delete(self)`**: Deletes the player from the database.
- **`get_all(cls)`**: Retrieves all players from the database.
- **`find_by_id(cls, id)`**: Finds a player by its ID.
- **`find_by(cls, attribute, value)`**: Finds a player by a specified attribute.
- **`get_players_by_team_id(cls, team_id)`**: Retrieves all players associated with a specific team.

## 🤝 Contributing

This is a fun project to use for our local league - feel free to fork, or share suggestions!

## 📄 License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.
