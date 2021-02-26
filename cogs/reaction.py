

import discord
import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class RoleReactClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 808746946277277716  # ID of message that can be reacted to to add role
        self.emoji_to_role = {
            partial_emoji_1: 808388285989650530,  # ID of role associated with partial emoji object 'partial_emoji_1'
            partial_emoji_2: 808388285989650525  # ID of role associated with partial emoji object 'partial_emoji_2'
        }

    async def on_raw_reaction_add(self, payload):
        """Dir wurde die Rolle erfolgreich gegeben.."""
        # Make sure that the message the user is reacting to is the one we care about
        if payload.message_id != self.role_message_id:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally add the role
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    async def on_raw_reaction_remove(self, payload):
        """Dir wurde die Rolle erfolgreich weggenommen..."""
        # Make sure that the message the user is reacting to is the one we care about
        if payload.message_id != self.role_message_id:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            # Makes sure the member still exists and is valid
            return

        try:
            # Finally, remove the role
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

# This bot requires the members and reactions intents.
intents = discord.Intents.default()
intents.members = True

client = RoleReactClient(intents=intents)

def setup(bot):
    bot.add_cog(reactions(bot))