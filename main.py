#William Zarzour
# 5/12/2023
# Itch.io bundle webscraper


# install dependencies with: pip install pandas beautifulsoup4
import requests
from bs4 import BeautifulSoup
import pandas as pd

#create the link
bundle_url = "https://itch.io/bundle/download/"
secret_key = input(f"Please enter the secret_key: ").strip() #key is the latter half of the bundle link excluding pagination
page_url = "?page="
total_pages = int(input("How many pages in the bundle: "))

game_info = []

#use cookie to make it look like I am logged in on your profile
cookie = open("cookie.txt","r").read().strip()
headers = {"Cookie":cookie}

for page in range(1,total_pages+1):
    page_num = f"{page_url}{page}"
    url = bundle_url+secret_key+page_num

    response = requests.get(url,headers=headers)

    #get html to read
    soup = BeautifulSoup(response.text, 'html.parser')

    #soup finds the specific div information needed for us to then iterate through the list of games
    game_list = soup.find_all(class_="game_row")

    #for loop iterating through the games and searching for each games title, description, author,and link
    for game in game_list: 
        game_title = game.find(class_="game_title").get_text().strip()
        game_description = game.find(class_="meta_row game_short_text").get_text().strip()
        game_author = game.find(class_="meta_row game_author").get_text().strip()
        game_link = game.find('a').get('href')
        
        #Using append to create a list of of the game information
        game_info.append([game_title,game_description,game_author,game_link])
        
#using pandas to create a dataframe and converting that dataframe to a CSV
df=pd.DataFrame(game_info, columns=['Game Title', 'Game Description','Author', 'Link'])
df.to_csv('bundle_info.csv')
print(df)





