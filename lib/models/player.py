from models.__init__ import CURSOR, CONN
from models.team import Team

class Player:
    def __init__(self, name, position, team, id=None):
        self.id = id
        self._name = name
        self._position = position
        self._team = team

    def __repr__(self):
        return f"<Player {self.id}: {self.name}, {self.position}, Team: {self.team.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, str) and position:
            self._position = position
        else:
            raise ValueError("Position must be a non-empty string")

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, team):
        if isinstance(team, Team):
            self._team = team
        else:
            raise ValueError("Team must be a valid Team object")

    @classmethod
    def create_tables(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES teams(id)
        )
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS players")
        CONN.commit()

    def save(self):
        if self.id:
            CURSOR.execute("UPDATE players SET name = ?, position = ?, team_id = ? WHERE id = ?", (self.name, self.position, self.team.id, self.id))
        else:
            CURSOR.execute("INSERT INTO players (name, position, team_id) VALUES (?, ?, ?)", (self.name, self.position, self.team.id))
            self.id = CURSOR.lastrowid

        CONN.commit()

    def delete(self):
        if self.id:
            CURSOR.execute("DELETE FROM players WHERE id = ?", (self.id,))
            CONN.commit()
            self.id = None

    @classmethod
    def create(cls, name, position, team_id):
        """ Initialize a new Player instance and save the object to the database """
        team = Team.find_by_id(team_id)  # Ensure this returns a valid team or None
        if not team:
            raise ValueError("Invalid team specified")
        player = cls(name=name, position=position, team=team)
        player.save()
        return player

    @classmethod
    def instance_from_db(cls, row):
        team = Team.find_by_id(row[3])
        player = cls(row[1], row[2], team, row[0])
        return player

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM players"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Player object corresponding to the table row matching the specified primary key"""
        sql = "SELECT * FROM players WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        return None  # Return None if no row found

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM players WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        return None

    @classmethod
    def get_players_by_team_id(cls, team_id):
        sql = "SELECT * FROM players WHERE team_id = ?"
        rows = CURSOR.execute(sql, (team_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
