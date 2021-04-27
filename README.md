# Amazon Stock Notifier

### A python script to check if a item is in stock mainly for amazon but can be adapted to other sites as well.

#### Run In Colab (Not recommended)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rhizomacomp10/stock-bot/blob/master/colab/colab.ipynb)

##### Replit would be better to run this rather then colab.

This is my first project I have made. This took me 3 days, the code might be rough and this is for my school community project.

Due to the sillicon shortage that is expected to last till 2022 and is plaguing graphics card stock, I have decided to make this bot in order to help people get their hands on a graphics card or anything that is affected by the shortage.

## Supports:
### · Windows
### · Linux

# Requirements
### SKIP THESE STEPS IF YOUR USING LINUX
1. You need to have the newest public version of chrome installed
2. Latest version of [Chrome Driver](https://chromedriver.chromium.org/) in the same directory as main.py

# Usage
1. Have Python 3.7 or higher installed to path.
1. Open cmd (or terminal if your using linux) and `CD` to the directory where main.py is located
2. Type in `python setup.py` to install the requirements for script
3. Open webhook.json in any text editor and paste in your [webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) url in between the empty quotes. 
4. Type in `python main.py` to start the bot
5. Done! The program will automatically refresh the site and check for stock and sending it to your desired discord webhook.
