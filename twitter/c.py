from django.shortcuts import render
import requests
import tweepy
from random import randint
from textblob import TextBlob
import re
from time import sleep
import json
import matplotlib.pyplot as plt
        
        
consumerkey="UNl49VtzHxHMzmocMHa00P7gQ"
consumersecret="W2SLgpJh6wmSe7Z46Q8361qvVcV0STbku7UpnLgvMpPJRonsFA"
accesskey="1174334913710940160-OXl03lmQzIGrDXOp2GaeUo6YnBS6od"
accesssecret="BwbJgpNYcLF3vr5Kb52RvEueReEcKA8JJ1Y7FnggxSSiX"
auth = tweepy.OAuthHandler(consumerkey, consumersecret) 
auth.set_access_token(accesskey, accesssecret)    
api=tweepy.API(auth)
auth.secure=True
ind=23424848
btrends=api.trends_place(ind)
print(btrends)
