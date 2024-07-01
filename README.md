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

### `lib/cli.py`

This is the main entry point for the CLI application. It provides an interactive menu for users to manage teams and players. 

#### Key Functions:

- **`cli()`**: The main function that runs the CLI loop and handles user input.
- **`teams_loop()`**:  Displays a list of all teams and provides options to add a team, go back, or exit.
- **`manage_team(team)`**:  Manages operations related to a specific team, including viewing players, adding a player, editing the team, and deleting the team.
- **`view_players_and_manage(team)`**: Displays a list of players associated with a specific team and provides options to manage the players.
- **`manage_player(playe, team)`**: Manages operations related to a specific player, including editing the player and deleting the player.


## Models

## Player
The Player class represents a player in the baseball league. It provides methods to interact with the players' data in the database.

## Attributes
id: Integer, primary key.
name: String, name of the player.
position: String, position of the player.
team_id: Integer, foreign key referencing the team.

## Methods
__init__(self, name, position, team_id, id=None): Initializes a new player instance.
__repr__(self): Returns a string representation of the player instance.

name: Property to get and set the name attribute.
position: Property to get and set the position attribute.
team_id: Property to get and set the team_id attribute.
create_tables(): Creates the players table in the database.
drop_table(): Drops the players table from the database.
save(): Saves the player instance to the database.
update(): Updates the player instance in the database.
delete(): Deletes the player instance from the database.
create(cls, name, position, team_id): Class method to create a new player instance and save it to the database.
instance_from_db(cls, row): Class method to return a Player object having the attribute values from the table row.
get_all(cls): Class method to return a list of all player instances.
find_by_id(cls, id): Class method to find a player by its id.
find_by_name(cls, name): Class method to find a player by its name.


## Team
The Team class represents a team in the baseball league. It provides methods to interact with the teams' data in the database.

## Attributes
id: Integer, primary key.
name: String, name of the team.
coach: String, name of the team's coach.

## Methods
__init__(self, name, coach, id=None): Initializes a new team instance.
__repr__(self): Returns a string representation of the team instance.

name: Property to get and set the name attribute.
coach: Property to get and set the coach attribute.
create_table(): Creates the teams table in the database.
drop_table(): Drops the teams table from the database.
save(): Saves the team instance to the database.
update(): Updates the team instance in the database.
delete(): Deletes the team instance from the database.
create(cls, name, coach): Class method to create a new team instance and save it to the database.
instance_from_db(cls, row): Class method to return a Team object having the attribute values from the table row.
get_all(cls): Class method to return a list of all team instances.
find_by_id(cls, id): Class method to find a team by its id.
find_by_name(cls, name): Class method to find a team by its name.
players(self): Method to return a list of players associated with the current team.

## 🤝 Contributing

This is a fun project to use for our local league - feel free to fork, or share suggestions!

## 📄 License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.
