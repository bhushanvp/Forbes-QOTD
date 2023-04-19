# Forbes-QOTD

The Forbes organization posts some of the best quotes on its website as well as social media accounts.


Forbes-QOTD project helps display the daily quote everytime after the startup (if the internet is connected) in the form of a notification.
This project is Currently supported only for Ubuntu operating system

I web scrapped for these quotes in their [website](https://www.forbes.com) and found out the locations in their HTML as follows :-

1. **The quote**               - /html/body/div[1]/main/div[1]/div/p[1]/text()
2. **The author**              - /html/body/div[1]/main/div[1]/div/p[2]/span[1]
3. **The author's Profession** - /html/body/div[1]/main/div[1]/div/p[2]/span[2]



## Requirements
* [Python3](https://www.python.org/downloads/)
* [Beautifulsoup](https://pypi.org/project/beautifulsoup4/) for web scrapping.
* [Requests](https://pypi.org/project/requests/) for sending HTTP requests.
* [Notify-Py](https://pypi.org/project/notify-py/) for generating notifications.


## Installation and Setup
1. Download this repo in the .zip format and extract it.
2. Open the Forbes-QOTD folder.
3. Run the install.sh file from terminal - 
   ```bash
   sudo bash install.sh
   ```
   
   1. This creates a dir .forbes_qotd in the home dir.
   2. Copies all the files from Forbes-QOTD dir to the .forbes_qotd dir present in the home dir of the user

4. Open the 'Startup Applications Preferences' app in Ubuntu add a new program with parameters as follows :-

    a. **Name** - **Forbes-QOTD**
    
    b. **Command** -
    ```bash
    /usr/bin/python3 /home/$username/.forbes_qotd/forbes_qotd.py
    ```
5. Reboot

## Resources and Tweaks
The 'resources' dir present in .forbes_qotd contains :-
1. ***Notification Sound*** - Currently set to "Windows-XP startup sound"
   To make any changes to it :- 
      1. Download a .wav music
      2. Rename it to 'notify.wav'
      3. Copy it to the resources dir
      
2. ***Notification Icon*** - Currently set as Forbes logo
   To make any changes to it :-
      1. Download a new icon/image (.png preferred)
      2. Rename it to 'icon.png'
      3. Copy it to the resources dir
