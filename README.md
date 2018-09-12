# User_Pager_Bot
Reddit bot that notifies users when their username gets mentioned in a submission's title or body.

## Why?
Reddit has an auto-formatting feature that hyperlinks usernames so that you don't have to do `[sample_username](url_of_user_profile)`.
This feature *seemingly* works double as a notification feature as well, and will send a private message to that user. 

But notification only works if done in the comment section and will not work in a submission title or body.

The problem is, because the auto-formatting works both in submission bodies and comment sections, most assume the notification feature will work for submissions as well.

This bot is to simply implement this feature for submissions so that users can properly be notified if mentioned.



## Prerequisites
```
PRAW (Python API Wrapper)
Python 3.x
```

## Installing
```
pip install praw
```
**Note**: PRAW supports Python 2.7, 3.3, 3.4, 3.5, and 3.6. More info can be found in the [PRAW documentation](https://praw.readthedocs.io/).


## Configuration

You also need an client id and client secret to use Reddit API. Visit Reddit [OAuth2 documentation](https://github.com/reddit-archive/reddit/wiki/OAuth2) for the instructions on how to get those.

After that, you need to configure the `.ini` file placed within the same directory as the source code. I have included a template called `sample_praw.ini`:
```
[BotName]
client_id=
client_secret=
username=
password=
```
where username and password refer to your Reddit account name and password. 

## TODO
* Add subreddit and user blocklist
* Consider PM instead of commenting the notifiers





