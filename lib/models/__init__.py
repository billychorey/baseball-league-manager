import sqlite3

CONN = sqlite3.connect('../baseball_league.db')
CURSOR = CONN.cursor()
