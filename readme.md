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

## Configuration 

the configuration is setup by a ini file that can be anywhere and called with the option -c at launch by default it will be /src/config.ini

##