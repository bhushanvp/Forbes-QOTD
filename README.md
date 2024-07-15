# Forbes-QOTD

The Forbes organization posts some of the best quotes on its website as well as social on their media handles.


Forbes-QOTD project helps display the daily quote everytime after the startup (if the internet is connected else a default quote) in the form of a notification.
Works only on Ubuntu operating system

I web scrapped this quote from [website](https://www.forbes.com) and found out the HTML class ids as follows

1. **The quote**               - qotd-section__description
2. **The author**              - qotd-section__byline-author
3. **The author's Profession** - qotd-section__byline-title



## Requirements
* [Python3](https://www.python.org/downloads/)

## Installation and Setup
1. Give required permissions to the installation script
   ```bash
   chmod +x install.sh
   ```
2. Run the script
   ```bash
   ./install.sh
   ```

3. Open the `Startup Applications Preferences` app in Ubuntu add a new program with parameters as follows :-

    a. **Name** - Forbes-QOTD
    
    b. **Command**
    ```bash
    python3 /home/$username/.forbes_qotd/main.py
    ```
4. Reboot

## Resources and Tweaks
The `resources` dir present in .forbes_qotd contains :-
1. ***Notification Sound***
   To make any changes to it :- 
      1. Download a `.wav` music
      2. Rename it to `notify.wav`
      3. Copy it to the `resources` dir
      
2. ***Notification Icon***
   To make any changes to it :-
      1. Download a new icon/image (.png preferred)
      2. Rename it to `icon.png`
      3. Copy it to the `resources` dir
