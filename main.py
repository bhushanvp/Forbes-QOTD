import time
import requests
from bs4 import BeautifulSoup as bs
from notifypy import Notify


time.sleep(5)

try:
    page = requests.get("http://www.forbes.com/").text
    soup = bs(page, "html.parser")

    quote = soup.find(class_="qotd-section__description").text
    author = soup.find(class_="qotd-section__byline-author").text
    author_desc = soup.find(class_="qotd-section__byline-title").text
except:
    quote = '"If there is a single key to success, it is the trait of being able to make things happen in this world."'
    author = "Sam Altman"
    author_desc = ", CEO, OpenAI"

notification = Notify()
notification.application_name = "Forbes"
notification.icon = "/home/bhushan/.forbes_qotd/resources/icon.png"
notification.audio = "/home/bhushan/.forbes_qotd/resources/notify.wav"
notification.title = "Quote of The Day"
notification.message = f"<b>{quote}</b>\n\n    <b>{author}</b>{author_desc}"
notification.send(block=False)
