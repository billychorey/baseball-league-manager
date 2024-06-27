from models.__init__ import CURSOR, CONN

class Team:
    all = {}

    def __init__(self, name, coach, id=None):
        self.id = id
        self.name = name
        self.coach = coach

    def __repr__(self):
        return f"<Team {self.id}: {self.name}, {self.coach}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Team name must be a non-empty string")

    @property
    def coach(self):
        return self._coach

    @coach.setter
    def coach(self, coach):
        if isinstance(coach, str) and len(coach):
            self._coach = coach
        else:
            raise ValueError("Coach name cannot be empty")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Team instances """
        sql = """
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT,
            coach TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Team instances """
        sql = "DROP TABLE IF EXISTS teams;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            sql = "INSERT INTO teams (name, coach) VALUES (?, ?)"
            CURSOR.execute(sql, (self.name, self.coach))
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
        CONN.commit()

    def update(self):
        sql = "UPDATE teams SET name = ?, coach = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.coach, self.id))
        CONN.commit()

    def delete(self):
        if self.id:
            sql = "DELETE FROM teams WHERE id = ?"
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            type(self).all.pop(self.id, None)
            self.id = None

    @classmethod
    def create(cls, name, coach):
        team = cls(name, coach)
        team.save()
        return team

    @classmethod
    def instance_from_db(cls, row):
        """Return a Team object having the attribute values from the table row."""
        team = cls.all.get(row[0])
        if team:
            team.name = row[1]
            team.coach = row[2]
        else:
            team = cls(row[1], row[2])
            team.id = row[0]
            cls.all[team.id] = team
        return team

    @classmethod
    def get_all(cls):
        """Return a list containing a Team object per row in the table"""
        sql = "SELECT * FROM teams"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Team object corresponding to the table row matching the specified primary key"""
        sql = "SELECT * FROM teams WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Team object corresponding to first table row matching specified name"""
        sql = "SELECT * FROM teams WHERE LOWER(name) = LOWER(?)"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @staticmethod
    def display_teams(teams):
        header = "Current League Teams"
        border = "*" * len(header)
        print(header)
        print(border)
        for team in teams:
            print(f"{team.id}. {team.name} - Coach: {team.coach}")

    def players(self):
        """Return list of players associated with the current team"""
        from models.player import Player
        sql = "SELECT * FROM players WHERE team_id = ?"
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Player.instance_from_db(row) for row in rows]
