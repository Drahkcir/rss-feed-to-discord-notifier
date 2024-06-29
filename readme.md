# Project description

This project allow via a configuration file to listen to a rss_feed and to send the news items to a discord webhook
the first goal was to be specific to a rss_feed in particular whisch is the CERT-FR rss but the goal is now to be more generic a try and handles more platform or at least handle several standardized format.  


## Prerequisite


Python3 with the following modules imported :

```python 
certifi==2024.2.2
charset-normalizer==3.3.2
discord-webhook==1.3.1
feedparser==6.0.11
idna==3.7
requests==2.32.2
sgmllib3k==1.0.0
urllib3==2.2.1
```
## Usage

```
usage: main.py [-h] [-d] [-v] [-c CONFIG] [-s SECTION] [-l [0-1800]]

get rss feed updates and send them on a discord server via a webhook

options:
  -h, --help
  -d, --debug           activate debug logs for debugging purpose
  -v, --verbose         set the logger to info level to have more info on activity of the script
  -c CONFIG, --config CONFIG
                        path to the config INI file to get the webhook url and the rss feed url
  -s SECTION, --section SECTION
                        Section of the config INI file to get the webhook url and the rss feed url
  -l [0-1800], --loop [0-1800]
                        if set to other than 0 the programm will loop to continuously to read the feed every {X} seconds
```


## Configuration 

the configuration is setup by a ini file that can be anywhere and called with the option -c at launch by default it will be /src/config.ini

```ini
[default]
webhook_url = '' 
rss_feed_url = ''

author_name = ''
author_image_url = ''
author_url = ''

embeded_image_url = ''

footer_message = ''
footer_image_url = ''


# this will be updated at each item processed to avoid treating several time the same item 
last_pub_date_processed = ''
```

you can have mutlple configuration in the same file and change the section loaded a exec via the `-s,--section` argument of the main script.

## 
