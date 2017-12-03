from selenium import webdriver
import random

base_url = 'https://watcheng.com/en/show/friends/'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Dictionary containing the list of episodes of each season
episodes = {1: 24
            , 2: 24
            , 3: 25
            , 4: 24
            , 5: 24
            , 6: 25
            , 7: 24
            , 8: 24
            , 9: 24
            , 10: 18}

season = random.randint(1, 10) # Generate a random season
episode_to_play = random.randint(1, episodes[season]) # Generate a random episode from the season
full_url = base_url + 'season-' + str(season) + '/episode-' + str(episode_to_play) + '/'
print(full_url)

driver = webdriver.Chrome(chrome_options=options)
driver.get(full_url)
driver.find_element_by_xpath('//*[@id="player"]/button').click() # Play Button
driver.find_element_by_xpath('//*[@id="player"]/div[4]/button[2]').click() # Full Screen
