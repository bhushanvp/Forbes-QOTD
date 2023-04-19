from bs4 import BeautifulSoup as bs
import requests
from notifypy import Notify

page = requests.get("http://www.forbes.com/").text
soup = bs(page, "html.parser")

quote = soup.find(class_= 'qotd-section__description').text
author = soup.find(class_= 'qotd-section__byline-author').text
author_desc = soup.find(class_= 'qotd-section__byline-title').text

notification = Notify()
notification.application_name ="Forbes"
notification.icon = "./resources/icon.png"
notification.audio = "./resources/notify.wav"
notification.title = "QOTD"
notification.message = f"{quote}\n\n    <b>{author}</b>{author_desc}"
notification.send(block=False)