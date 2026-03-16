import requests
from flask import current_app


RAWG_BASE_URL = "https://api.rawg.io/api"

def get_games():
    api_key = current_app.config["RAWG_API_KEY"]
    
    params = {
        "key": api_key,
        "page_size": 10
    }

    response = requests.get(f"{RAWG_BASE_URL}/games", params=params)
    response.raise_for_status()

    return response.json()

def get_details(game_id:int ):
    api_key = current_app.config["RAWG_API_KEY"]
    params={"key":api_key}
    response=requests.get(f"{RAWG_BASE_URL}/games/{game_id}",params=params)
    response.raise_for_status()
    return response.json()