#!/usr/bin/python3

import os
import praw
import re
import requests
from os.path import sys
from prawcore import OAuthException
from praw.exceptions import APIException
from time import sleep

# Global constants
REPLY_TEMPLATE = '''Paging {}!

***
^^This ^^action ^^was ^^performed ^^by ^^a ^^bot'''

DEFAULT_SUB = 'User_Pager_Bot'

def authenticate():
    ''' returns a Reddit instance after aunthetication '''
    print("Authenticating...")

    # http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
    if not os.path.isfile("praw.ini"):
        print("Ensure praw.ini file exists")
        sys.exit()

    reddit = praw.Reddit('User_Pager_Bot', user_agent = 'User_Pager_Bot v1.0')

    try:
        print("Welcome {}!".format(reddit.user.me()))
    except OAuthException:
        print("Authentication failed. Ensure proper credentials in praw.ini")
        sys.exit()

    return reddit

def parse_username(text):
    ''' return a list of usernames mentioned from text '''
    usernames = set()

    username_rx = re.compile(r"(?:^|[^\w-])\/?u\/([\w-]{3,20})(?:$|[^\w-])")     # test /u/name|/u/name2
    usernames = username_rx.findall(text)

    # remove any duplicates
    usernames = list(set(usernames))

    return usernames

def valid_username(reddit, username):
    ''' return true if valid username '''
    try:
        reddit.redditor(username).id
        return True
    except:
        print("/u/{} is invalid".format(username))
        return False

def get_submissions():
    ''' return a list of submission id '''
    if not os.path.isfile("submissions_replied_to.txt"):
        submissions_replied_to = []
    else:
        with open("submissions_replied_to.txt", "r") as f:
            submissions_replied_to = f.read()
            submissions_replied_to = submissions_replied_to.split("\n")
            submissions_replied_to = list(filter(None, submissions_replied_to))

    return submissions_replied_to

def run_bot(reddit):
    '''  '''
    submissions_replied_to = get_submissions()

    subreddit_stream = reddit.subreddit(DEFAULT_SUB).stream.submissions()

    for submission in subreddit_stream:
        print(submission.id)
        if submission.id not in submissions_replied_to:
            usernames = parse_username(submission.title + " " + submission.selftext)

            for username in usernames:
                if valid_username(reddit, username):
                    try:
                        submission.reply(REPLY_TEMPLATE.format("/u/" + username))
                    except APIException as e:
                        print(e)
                        print("Sleeping")
                        sleep(300)
            with open("submissions_replied_to.txt", "a") as f:
                f.write(submission.id + "\n")

def main():
    reddit = authenticate()

    run_bot(reddit)

if __name__ == "__main__":
    main()