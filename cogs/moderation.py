import os, sys, discord
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', pass_context=True)
    async def kick(self, context, member: discord.Member, *args):
        """
        Kick a user out of the server.
        """
        if context.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Affe!",
                    description="Der User hat Adminrechte, du vollidiot :P",
                    color=0x00FF00
                )
                await context.send(embed=embed)
            else:
                try:
                    reason = " ".join(args)
                    embed = discord.Embed(
                        title="User Kicked!",
                        description=f"**{member}** was kicked by **{context.message.author}**!",
                        color=0x00FF00
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    try:
                        await member.send(
                            f"You were kicked by **{context.message.author}**!\nReason: {reason}"
                        )
                    except:
                        pass
                except:
                    embed = discord.Embed(
                        title="Error!",
                        description="Es ist ein fehler aufgetreten beim kicken des Users..",
                        color=0x00FF00
                    )
                    await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.command(name="nick")
    async def nick(self, context, member: discord.Member, *, name: str):
        """
        Change the nickname of a user on a server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if name.lower() == "!reset":
                    name = None
                embed = discord.Embed(
                    title="Changed Nickname!",
                    description=f"**{member}'s** new nickname is **{name}**!",
                    color=0x00FF00
                )
                await context.send(embed=embed)
                await member.change_nickname(name)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="Es ist ein Fehler aufgetreten beim Nickname ändern.",
                    color=0x00FF00
                )
                await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.command(name="ban")
    async def ban(self, context, member: discord.Member, *args):
        """
        Bans a user from the server.
        """
        if context.message.author.guild_permissions.administrator:
            try:
                if member.guild_permissions.administrator:
                    embed = discord.Embed(
                        title="Error!",
                        description="Ey du vollpfosten? Der User hat immer noch Adminrechte :P",
                        color=0x00FF00
                    )
                    await context.send(embed=embed)
                else:
                    reason = " ".join(args)
                    embed = discord.Embed(
                        title="User Banned!",
                        description=f"**{member}** was banned by **{context.message.author}**!",
                        color=0x00FF00
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await context.send(embed=embed)
                    await member.send(f"You were banned by **{context.message.author}**!\nReason: {reason}")
                    await member.ban(reason=reason)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="Ein Fehler ist aufgetreten.",
                    color=0x00FF00
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.command(name="warnen")
    async def warnen(self, context, member: discord.Member, *args):
        """
        Warns a user in his private messages.
        """
        if context.message.author.guild_permissions.administrator:
            reason = " ".join(args)
            embed = discord.Embed(
                title="User Warned!",
                description=f"**{member}** was warned by **{context.message.author}**!",
                color=0x00FF00
            )
            embed.add_field(
                name="Reason:",
                value=reason
            )
            await context.send(embed=embed)
            try:
                await member.send(f"You were warned by **{context.message.author}**!\nReason: {reason}")
            except:
                pass
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            
    @commands.command(name="unwarn")
    async def warn(self, context, member: discord.Member, *args):
        """
        Warns a user in his private messages.
        """
        if context.message.author.guild_permissions.administrator:
            reason = " ".join(args)
            embed = discord.Embed(
                title="User Unwarned!",
                description=f"**{member}** was unwarned by **{context.message.author}**!",
                color=0x00FF00
            )
            await context.send(embed=embed)
            try:
                await member.send(f"You were unwarned by **{context.message.author}**")
            except:
                pass
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.command(name="purge")
    async def purge(self, context):
        """
        Delete a number of messages.
        """
        if context.message.author.guild_permissions.administrator:
            purged_messages = await context.message.channel.purge(limit=400)
            embed = discord.Embed(
                title="Chat Cleared!",
                description=f"**{context.message.author}** Nuked **{len(purged_messages)}** biatches!",
                color=0x00FF00
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

def setup(bot):
    bot.add_cog(moderation(bot))