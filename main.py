print('Importing libraries..')

from os import system
import sys
import json
import time
from urllib.parse import urlparse
from json import dumps
from selenium import webdriver ## the webscraper
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=chrome_options)
driver = webdriver.Chrome('chromedriver',options=chrome_options)
from discord_webhook import DiscordWebhook, DiscordEmbed

print('Libraries have been imported.')

## Variables

istrue = 'true'
notification_sent = False

data = {}

with open('webhook.json') as f:
    data = json.load(f)
webhook = data['webhook']

embed_webhook = DiscordWebhook(url=webhook)
url = input("Enter the URL: ")
timeout = float(input("Enter the timeout: "))
hostname = urlparse(url).hostname

while istrue == 'true': #Infinite while loop
  try:
    print('Getting Site..')
    wd.get(url) ## Scrape Website
    amazon_title = wd.find_element_by_id('productTitle').text

    instock = bool("In Stock." in wd.page_source)

    if instock == True: ## In Stock Checker
      if notification_sent == False:
        print(amazon_title + ' Is in stock. Sending notification.')
        notification_sent = True

        embed = DiscordEmbed(title=amazon_title + ' is now in stock!', description='Get your item now!', color='1e457b')
        embed.set_author(name='https://'+hostname, url='https://'+hostname, icon_url='https://'+hostname+'/favicon.ico')
        embed.set_footer(text='Stock Bot')
        embed.add_embed_field(name='Link', value=url)
        embed.set_timestamp()

        embed_webhook.add_embed(embed)
        response = embed_webhook.execute()

        webhook = DiscordWebhook(url=webhook, content='@everyone') ## sends everyone the notification
        response = webhook.execute()

        time.sleep(timeout)
      else:
        print(amazon_title + ' Is in stock. Already sent notification.')
        time.sleep(timeout)
    else:
      notification_sent = False
      print(amazon_title + ' is not in stock, trying again..')
    time.sleep(timeout)
  except KeyboardInterrupt: ## Stop the loop and exit
    break
