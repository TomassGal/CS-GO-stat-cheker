import json
import os

def convert_user_data(data_json):
    '''
    Input: Users data json file
    Output: A comprehensible dictionary of the users stats 
    '''
    data = data_json["playerstats"]["stats"]
    for dict in data:
        if dict["name"] == "total_kills":
            kills = dict["value"]
        if dict["name"] == "total_deaths":
            deaths = dict["value"]
        if dict["name"] == "total_matches_played":
            total_matches_played = dict["value"]
        if dict["name"] == "total_matches_won":
            total_matches_won = dict["value"]
        if dict["name"] == "total_shots_fired":
            total_shots_fired = dict["value"]
        if dict["name"] == "total_shots_hit":
            total_shots_hit = dict["value"]
        if dict["name"] == "total_kills_headshot":
            total_kills_headshot = dict["value"]
        if dict["name"] == "total_rounds_played":
            total_rounds_played = dict["value"]
        if dict["name"] == "total_mvps":
            total_mvps = dict["value"]
        if dict["name"] == "last_match_favweapon_id":
            last_match_favweapon_id = dict["value"]
        if dict["name"] == "last_match_kills":
            last_match_kills = dict["value"]
        if dict["name"] == "last_match_deaths":
            last_match_deaths = dict["value"]
        if dict["name"] == "last_match_rounds":
            last_match_rounds = dict["value"]
        if dict["name"] == "last_match_wins":
            last_match_wins = dict["value"]
        if dict["name"] == "last_match_damage":
            last_match_damage = dict["value"]
        if dict["name"] == "total_time_played":
            total_time_played_s = dict["value"]
        if dict["name"] == "last_match_favweapon_id":
            last_match_favweapon = wepon_name(dict["value"])
        if dict["name"] == "last_match_contribution_score":
            last_match_score = dict["value"]
    total_time_played = round(total_time_played_s / 3600)
    last_match_loses = last_match_rounds - last_match_wins
    try:
        last_match_kd = round(last_match_kills/last_match_deaths, 2)
    except ZeroDivisionError:
        last_match_kd = 0
    last_match_favweapon = wepon_name(last_match_favweapon_id)
    mvps = int(round(total_mvps/total_rounds_played, 2) * 100)
    headshots = int(round(total_kills_headshot/kills, 2) * 100)
    accuracy = int(round(total_shots_hit/total_shots_fired, 2) * 100)
    try:
        kd = round(kills/deaths, 2)
    except ZeroDivisionError:
        kd = 0
    winrate = int(round(total_matches_won/total_matches_played, 2) * 100)
    last_adr = round(last_match_damage/last_match_rounds)


    converted_data = {
        "kd": kd,
        "winrate": winrate,
        "total_matches_played": total_matches_played,
        "accuracy": accuracy,
        "headshots": headshots,
        "mvps": mvps,
        "last_match_favweapon": last_match_favweapon,
        "last_match_kd": last_match_kd,
        "last_match_kills": last_match_kills,
        "last_match_wins": last_match_wins,
        "last_match_loses": last_match_loses,
        "last_match_adr": last_adr,
        "total_time_played": total_time_played,
        "last_match_fav_weapon": last_match_favweapon,
        "last_match_score": last_match_score,
    }
    return converted_data

def wepon_name(id):
    '''
    Input: CSGO wepons ID
    Output: CSGO wepons name 
    '''
    with open(".\\data\\csgo_wepons.json") as file:
        data = json.load(file)
    for key, value in data.items():
        if int(key) == id:
            return value

def get_saved_users():
    '''
    Input: None
    Output: All of the saved users in a list
    '''
    users = [file for file in os.listdir(".\\data\\saved_users")]
    return users