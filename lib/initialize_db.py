from models.team import Team
from models.player import Player

def initialize_database():
    print("Creating tables...")
    Team.create_table()
    Player.create_tables()
    print("Tables created successfully.")

if __name__ == "__main__":
    print("Initializing database...")
    initialize_database()
    print("Database initialized.")
