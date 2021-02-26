import discord
import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class TwitchApiPy():
    def __init__(self):
        self.ClientID = "5qm3pqmbiuxesiq84g28kf3qpieknr"
        self.OAuth = "3k9dtpqn9z2izm6r0dc7s84y66aenh"

    """
    You don't really use this its for other requests
    """

    def GetUserID(self, name):
        r = requests.get(url="https://api.twitch.tv/helix/users?login={}".format(name),
                         headers={'Client-ID': self.ClientID, 'Authorization': self.OAuth})
        r = r.json()
        id = r["data"][0]['id']
        return id

    """
    This part will get you number of followers of asked channel
    """

    def GetFollowerCount(self, name):
        id = self.GetUserID(name)
        r = requests.get(url="https://api.twitch.tv/helix/users/follows?to_id={}".format(id),
                         headers={'Client-ID': self.ClientID, 'Authorization': self.OAuth})
        r = r.json()
        return r['total']

    """
     This part will say that if the streamer is online or not and the language the streamer streams
     """

    def GetChannelStatus(self, name):
        r = requests.get(url="https://api.twitch.tv/helix/search/channels?query={}".format(name),
                         headers={'Client-ID': self.ClientID, 'Authorization': self.OAuth})
        r = r.json()
        is_live = r["data"][0]['is_live']
        lang = r["data"][0]['broadcaster_language']
        total_info = {
            "islive": is_live,
            "language": lang,
        }
        return total_info

    """
     This part will get you general info about channel
     """

    def GetChannelInfo(self, name):
        id = self.GetUserID(name)
        r = requests.get(url="https://api.twitch.tv/helix/channels?broadcaster_id={}".format(id),
                         headers={'Client-ID': self.ClientID, 'Authorization': self.OAuth})
        r = r.json()
        name = r["data"][0]["broadcaster_name"]
        game = r["data"][0]["game_name"]
        title = r["data"][0]["title"]
        total_info = {
            "name": name,
            "game": game,
            "title": title
        }
        return total_info
