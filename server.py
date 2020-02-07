import pymongo
import pandas as pd
import numpy as np
import json
import requests
import sqlite3
cur = sqlite3.connect('database.sqlite').cursor()

def get_season_games(season):
    wanted_match_df = pd.DataFrame(cur.execute(f"""SELECT HomeTeam, AwayTeam, Div AS league, Season, FTHG, FTAG, FTR, Date
                                                    FROM matches
                                                    WHERE season == {season} OR league = 'E0' OR league = 'D1'
                                                    """).fetchall())
    wanted_match_df.columns = [x[0] for x in cur.description]
    return wanted_match_df