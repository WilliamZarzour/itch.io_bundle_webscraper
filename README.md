# itch.io_bundle_webscraper
A webscraper that takes the scrapes the bundle information into a dataframe and csv

# itch.io_bundle_webscraper
A webscraper that takes the scrapes the bundle information into a dataframe and csv

A BeautifulSoup4 scraper written in python that scrapes the info for each game inside the provided bundle. 
Collects the Game Title, Game Description, Game Author, Link.

To run this project:

1. You will need python (make sure to have the PATH checked) 

2. To install dependencies inside a terminal run the following command  
>   pip install pandas beautifulsoup4


3. Find your account cookie info and save it in the Cookie.txt file 
>   Make sure you are logged out of Itch.io
>   Go to the bundle link (if you are logged out you wont see the bundle)
>   Before logging in inspect element for website (left click and inspect element or hit f12 on the website)
>   Go to the network Tab and keep it open (the tab will likely be blank)
>   Log into the bundle. It should now see network was populated with information. 
>   Click on your profile at the top of the "name" column 
>   Find the request headers and copy your cookie

# WARNING: Do not share this cookie with anyone or post it online!!!


4. Run the code and fill out the required bundle information! 

5. Enjoy your CSV
