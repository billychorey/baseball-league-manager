# # import sqlite3
# import os

# DATABASE_NAME = 'baseball_league.db'

# # def get_connection():
# #     conn = sqlite3.connect(DATABASE_NAME)
# #     return conn

# # def create_database():
# #     if not os.path.exists(DATABASE_NAME):
# #         conn = get_connection()
# #         conn.close()

# def create_tables():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS teams (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             coach TEXT NOT NULL
#         )
#         """)
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS players (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             attributes TEXT NOT NULL,
#             team_id INTEGER NOT NULL,
#             FOREIGN KEY (team_id) REFERENCES teams (id)
#         )
#         """)
#         conn.commit()
