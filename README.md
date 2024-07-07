# ⚾ Baseball League Manager

![Baseball](lib/img/baseball.png)
*Image of Fenway park - Getty images - from [Fenway - Conde Nast Traveler](https://www.cntraveler.com/activities/boston/fenway-park)*

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

### `cli.py`

This is the main entry point for the CLI application. It provides an interactive menu for users to manage teams and players.

#### Key Functions:

- **`cli()`**: The main function that runs the CLI loop and handles user input.
- **`search_team()`**: Allows searching for a team by name.
- **`teams_loop()`**: Displays a list of all teams and provides options to add a team, go back, or exit.
- **`manage_team(team)`**: Manages operations related to a specific team, including viewing players, adding a player, editing the team, and deleting the team.
- **`view_players_and_manage(team)`**: Displays a list of players associated with a specific team and provides options to manage the players.
- **`manage_player(player, team)`**: Manages operations related to a specific player, including editing the player and deleting the player.
- **`search_player_within_team(team)`**: Allows searching for a player within a specific team.

### `player.py`

This file defines the `Player` class, which represents a player in the baseball league. It provides methods to interact with the player's data in the database.

#### Key Methods and Attributes:

- **Attributes**:
    - `id`: Integer, primary key.
    - `name`: String, name of the player.
    - `position`: String, position of the player.
    - `team_id`: Integer, foreign key referencing the team.

- **Methods**:
    - `__init__(self, name, position, team_id, id=None)`: Initializes a new player instance.
    - `__repr__(self)`: Returns a string representation of the player instance.
    - `name`: Property to get and set the name attribute.
    - `position`: Property to get and set the position attribute.
    - `team_id`: Property to get and set the team_id attribute.
    - `create_tables(cls)`: Creates the players table in the database.
    - `drop_table(cls)`: Drops the players table from the database.
    - `save(self)`: Saves the player instance to the database.
    - `update(self)`: Updates the player instance in the database.
    - `delete(self)`: Deletes the player instance from the database.
    - `create(cls, name, position, team_id)`: Class method to create a new player instance and save it to the database.
    - `instance_from_db(cls, row)`: Class method to return a Player object having the attribute values from the table row.
    - `get_all(cls)`: Class method to return a list of all player instances.
    - `find_by_id(cls, id)`: Class method to find a player by its id.
    - `find_by_name(cls, name)`: Class method to find a player by its name.

### `team.py`

This file defines the `Team` class, which represents a team in the baseball league. It provides methods to interact with the team's data in the database.

#### Key Methods and Attributes:

- **Attributes**:
    - `id`: Integer, primary key.
    - `name`: String, name of the team.
    - `coach`: String, name of the team's coach.

- **Methods**:
    - `__init__(self, name, coach, id=None)`: Initializes a new team instance.
    - `__repr__(self)`: Returns a string representation of the team instance.
    - `name`: Property to get and set the name attribute.
    - `coach`: Property to get and set the coach attribute.
    - `create_table(cls)`: Creates the teams table in the database.
    - `drop_table(cls)`: Drops the teams table from the database.
    - `save(self)`: Saves the team instance to the database.
    - `update(self)`: Updates the team instance in the database.
    - `delete(self)`: Deletes the team instance from the database.
    - `create(cls, name, coach)`: Class method to create a new team instance and save it to the database.
    - `instance_from_db(cls, row)`: Class method to return a Team object having the attribute values from the table row.
    - `get_all(cls)`: Class method to return a list of all team instances.
    - `find_by_id(cls, id)`: Class method to find a team by its id.
    - `find_by_name(cls, name)`: Class method to find a team by its name.
    - `players(self)`: Method to return a list of players associated with the current team.

### `helpers.py`

This file provides helper functions to find teams and players by name, display all teams and players, and manage the CRUD operations for teams and players.

#### Key Functions:

- **`find_by_attribute(object_list, attribute, value)`**: Finds objects in a list by a specified attribute and value.
- **`find_team_by_name(teams, name)`**: Finds teams by name.
- **`find_player_by_name(players, name)`**: Finds players by name.
- **`display_all_teams()`**: Displays all teams.
- **`create_team()`**: Creates a new team.
- **`update_team(team)`**: Updates an existing team.
- **`delete_team(team)`**: Deletes an existing team.
- **`display_all_players(team)`**: Displays all players in a team.
- **`create_player(team_id)`**: Creates a new player in a team.
- **`update_player(player)`**: Updates an existing player.
- **`delete_player(player)`**: Deletes an existing player.
- **`exit_program()`**: Exits the program.

## 🤝 Contributing

This is a fun project to use for our local league - feel free to fork, or share suggestions!

## 📄 License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.
