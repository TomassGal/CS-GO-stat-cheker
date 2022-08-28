from urllib import response
import requests

STEAM_KEY = "8A92919CC2C3078A7637C62178C516A1"

def get_stats(user_id:int):
    '''
    Input: users steamid.
    Output: json file of users stats in cs:go.
    '''
    params = {
        "steamid": user_id,
        "appid": 730,
        "key": STEAM_KEY
    }
    response = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/", params=params)
    
    if response.status_code == 500:
        return None

    return response.json()

def get_player_name(user_id:int):
    '''
    Input: users steamid.
    Output: Users steam name.
    '''
    params = {
        "steamids": user_id,
        "key": STEAM_KEY
    }
    response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/", params=params)
    data = response.json()
    try:
        name = data["response"]["players"][0]["personaname"]
    except IndexError:
        return None
    return name

def get_steamid(profile_link:str):
    '''
    Input: users steam profile link.
    Output: users steamid.
    '''
    try:

        if "id/" in profile_link:
            name = profile_link.split("id/")[1]
            name = name.replace("/", "")
            params = {
            "vanityurl": name,
            "key": STEAM_KEY
            }
            response = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/", params=params)
            try:
                steamid = response.json()["response"]["steamid"]
            except KeyError:
                return None
        else:
            second_part = profile_link.split("profiles")[1]
            steamid = second_part.replace("/", "")
    except IndexError:
        return None

    return int(steamid)




