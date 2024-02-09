import discord
from webserver import keep_alive
import os


from discord.ext import commands

from webserver import keep_alive

import os

async def on_ready():

    print("Bot is currently online!")



    #help command

    @client.command(pass_context=True)

    async def help(ctx):

        author = ctx.message.author

        embed = discord.Embed(

            colour = discord.Colour.orange()

        )


        embed.set_author(name="Help")

        embed.add_field(name="!help",value="Help command",inline=False)

        channel = await author.create_dm()

        await channel.send(author,embed=embed)

        await ctx.message.channel.send("Message sent to your DMs")




keep_alive()