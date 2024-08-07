from models.__init__ import CURSOR, CONN
from models.team import Team

class Player:
    all = {}
    
    def __init__(self, name, position, team_id, id=None):
        self.id = id
        self.name = name
        self.position = position
        self.team_id = team_id

    def __repr__(self):
        return (
            f"<Player {self.id}: {self.name}, {self.position}, Team ID: {self.team_id}>"
        )
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, str) and len(position):
            self._position = position
        else:
            raise ValueError("Position must be a non-empty string")

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        if isinstance(team_id, int) and Team.find_by_id(team_id):
            self._team_id = team_id
        else:
            raise ValueError("team_id must reference a team in the database")

    @classmethod
    def create_tables(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT,
            team_id INTEGER,
            FOREIGN KEY (team_id) REFERENCES teams(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO players (name, position, team_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.position, self.team_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE players
            SET name = ?, position = ?, team_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.position, self.team_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM players
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
        
    @classmethod
    def create(cls, name, position, team_id):
        player = cls(name, position, team_id)
        player.save()
        return player

    @classmethod
    def instance_from_db(cls, row):
        team_id = row[3]
        if not Team.find_by_id(team_id):
            return None
        player = cls.all.get(row[0])
        if player:
            player.name = row[1]
            player.position = row[2]
            player.team_id = team_id
        else:
            player = cls(row[1], row[2], team_id)
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM players"
        rows = CURSOR.execute(sql).fetchall()
        return [player for player in (cls.instance_from_db(row) for row in rows) if player is not None]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM players WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM players WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
