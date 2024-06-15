from models.__init__ import CURSOR, CONN
# from models.player import Player

class Team:
    all = {}

    def __init__(self, name, coach, id=None):
        self.id = id
        self.name = name
        self.coach = coach

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
    def create_tables(cls):
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
        sql = """
            DROP TABLE IF EXISTS teams;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            # Update the existing record
            sql = "UPDATE teams SET name = ?, coach = ? WHERE id = ?"
            CURSOR.execute(sql, (self.name, self.coach, self.id))
            print("Updated existing team.")
        else:
            # Insert a new record
            sql = "INSERT INTO teams (name, coach) VALUES (?, ?)"
            CURSOR.execute(sql, (self.name, self.coach))
            self.id = CURSOR.lastrowid  # Get the last inserted ID and assign it to the object's id attribute
            type(self).all[self.id] = self  # Updating the dictionary entry if using a cache
            print("Inserted new team.")
        CONN.commit()

    @classmethod
    def create(cls, name, coach):
        """ Initialize a new Team instance and save the object to the database """
        team = cls(name, coach)
        team.save()
        return team

    def update(self):
        """Update the table row corresponding to the current Team instance."""
        sql = """
            UPDATE teams
            SET name = ?, coach = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.coach, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Team instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM teams
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Team object having the attribute values from the table row."""
        if row is None:
            return None

        team_id = row[0]
        team = cls.all.get(team_id)
        if not team:
            # Create new instance if it's not in the cache
            team = cls(name=row[1], coach=row[2], id=team_id)
            cls.all[team_id] = team
        else:
            # Update existing instance with new data
            team.name = row[1]
            team.coach = row[2]
            
        return team

    @classmethod
    def get_all(cls):
        """Return a list containing a Team object per row in the table"""
        sql = """
            SELECT *
            FROM teams
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Team object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM teams
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def players(self):
        """Return list of players associated with the current team"""
        from models.player import Player
        sql = """
            SELECT * FROM players
            WHERE team_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [
            Player.instance_from_db(row) for row in rows
        ]


# import team here somewhere inside this method
# getters and setters - these are validations. I need these.
# example of this in dept and employee(and getters and setters)

# need something like this:
#      @name.setter
#     def name(self, name):
#         if isinstance(name, str) and len(name):
#             self._name = name
#         else:
#             raise ValueError(
#                 "Name must be a non-empty string"
#             )
