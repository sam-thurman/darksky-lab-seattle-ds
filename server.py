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

def get_rainy(time):
    url = f'https://api.darksky.net/forecast/50d46873ca88e25f973adf8228bf2275/52.5200,13.4050,{time}T12:00:00'
    response = requests.get(url)
    data = json.loads(response.text)
    if 'icon' in data['daily']['data'][0].keys():
        return 'rain' in data['daily']['data'][0]['icon']
    return False

def add_rainy(df):
    rain_frame = df.copy()
    rainy = []
    for date in rain_frame['Date']:
        rainy.append(get_rainy(date))
    rain_frame['rainy'] = rainy
    return rain_frame

def total_goals(team, dataframe):
    home_goals = dataframe.loc[dataframe['HomeTeam'] == team]['FTHG'].sum()
    away_goals = dataframe.loc[dataframe['AwayTeam'] == team]['FTAG'].sum() 
    return home_goals + away_goals

def total_wins(team, dataframe):
    home_wins = len(dataframe.loc[dataframe['HomeTeam'] == team].loc[dataframe['FTR'] == 'H'])
    away_wins = len(dataframe.loc[dataframe['AwayTeam'] == team].loc[dataframe['FTR'] == 'A'])
    return home_wins + away_wins

def rain_percent(team, df):
    home = df.loc[df['HomeTeam'] == team].loc[df['rainy'] == True]
    away = df.loc[df['AwayTeam'] == team].loc[df['rainy'] == True]
    wins = len(home.loc[home['FTR'] == 'H']) + len(away.loc[away['FTR'] == "A"])
    total_games = len(home) + len(away)
    if total_games == 0:
        return 0
    return wins / total_games

def get_stats(dataframe):
    columns=['Team Name', 'League', 'Season', 'Wins', 'Goals', 'Win Percentage on Rainy Days']
    df_list = []
    for team in set(list(dataframe['HomeTeam']) + list(dataframe['AwayTeam'])):
        league1 = dataframe.loc[dataframe['HomeTeam'] == team]
        league2 = dataframe.loc[dataframe['AwayTeam'] == team]
        league = pd.concat([league2, league1])
        season = dataframe['Season'][0]
        df_list.append([team, league['league'].iloc[0], season, total_wins(team, dataframe), total_goals(team, dataframe),
                        rain_percent(team, dataframe)])
    return pd.DataFrame(df_list, columns=columns)

def mongo_handler(stats_df):
    password = json.load(open ('pwds.json'))
    client = pymongo.MongoClient(f"mongodb+srv://samthurman:{password['password']}@flatironcluster1-mfxlu.mongodb.net/test?retryWrites=true&w=majority")
    db = client.DarkskyLab
    dictionary_list = []
    for team in stats_df.values:
        dictionary = dict(zip(list(stats_df.columns), team))
        dictionary_list.append(dictionary)
    db.teamResults.insert_many(dictionary_list)
    return db.teamResults

