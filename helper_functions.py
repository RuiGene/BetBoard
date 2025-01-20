import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def calculate_profit(units, multiplier, outcome):
    if outcome == 1 or outcome == 'Won':
        profit = units*multiplier - units
    else:
        profit = units*-1
    
    return profit

def get_player_id(player_name):
    first_name, last_name = player_name.split(" ")
    last_name = last_name[0:5].lower()
    first_name = first_name[0:2].lower()

    formatted_name = last_name + first_name + '01'
    url = f"https://www.basketball-reference.com/players/d/{formatted_name}.html"

    return url

def scrape_player_stats(player_href):
    """
    Scrapes detailed player statistics from their profile page.
    Args:
    Returns:
    """
    response = requests.get(player_href)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', id='per_game_stats') 
        if table:
            df = pd.read_html(str(table))[0]
            df = df[df['Season'].notna()] 
            df['Season'] = df['Season'].str.split('-').str[0] 
            df = df[df['Age'].notnull()] 
            return df
    return pd.DataFrame() 

def player_headshot(player_href):
    response = requests.get(player_href)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser') 

        media_item = soup.find('div', class_='media-item')
        if media_item:
            img_tag = media_item.find('img')
            if img_tag and 'src' in img_tag.attrs:
                img_url = img_tag['src']
                
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    image = Image.open(BytesIO(img_response.content))
                    return image 
    return None