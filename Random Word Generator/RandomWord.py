import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

random_word = ''
print('Please wait while the subjects are loading...')

options = webdriver.ChromeOptions()
options.add_argument("--headless")
category_dict = {'Animals':1,
                 'Food':2,
                 'Idioms':21,
                 'Movies':22,
                 'People & Characters':3,
                 'Places':4,
                 'Other':5,
                 'Any Word Ever!':999}
categories = []

url = 'https://www.thegamegal.com/word-generator/'
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
select = Select(driver.find_element_by_id('game'))
select.select_by_value('1')
cat = driver.find_element_by_id('category')

for index, option in enumerate(cat.find_elements_by_tag_name('option'), start= 1):
    categories.append(str(index) +  '. '+ option.text)
print('\n'.join(categories))

print('Select your category')
while(1):
    try:
        category = int(input('Enter the option and press Enter: '))
        if category in range(1,9):
            break
        else:
            print('Enter a valid choice between 1 and 8')
    except:
        print('Enter a valid choice between 1 and 8')

category_selected = categories[category - 1].split('.')
category_sent = category_dict[category_selected[1].lstrip()]
select_cat = Select(driver.find_element_by_id('category'))
select_cat.select_by_value(str(category_sent))

driver.find_element_by_xpath('//*[@id="newword-button"]').click()
while random_word == '':
    time.sleep(1)
    word = driver.find_element_by_xpath('//*[@id="gennedword"]')
    random_word = word.get_attribute('innerHTML')

print('Your Random word: '+random_word)
driver.close()
