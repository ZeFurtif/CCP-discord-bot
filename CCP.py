import discord
import json
import random
from discord import activity
from discord import team
from discord import channel
from discord import colour
from discord.enums import PremiumType
from discord.ext import commands
from discord.abc import GuildChannel
from discord.activity import CustomActivity
from discord.channel import VoiceChannel
from discord.gateway import DiscordWebSocket
from discord.team import Team

client = discord.Client()

def plus(data, name):
    if name in data:
        data[name] = data[name] + 10 
        return f"{name} 他已被举报给中共 | has been reported successfully."
    else:
        data[name] = 1000 
        return f"{name} 他已被举报给中共 | has been reported successfully."


@client.event
async def on_ready():
    print("我爱中国")
    
    await client.change_presence(activity=discord.CustomActivity(name="",emoji="🔥"))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):

    print(message.author, message.channel, message.content)

    if message.author.id == client.user.id:
        return
    else:
        #MISC
        if message.content.lower() == "china":
            await message.channel.send("荣耀归于中国 中国会赢 | China will prevail! Glory to China!")
        elif message.content.lower() == "taiwan":
            await message.channel.send("台湾属于中国 | Taiwan belongs to the Republic of China")
        elif message.content.lower() == "honkong":
            await message.channel.send("香港属于中国 | Honkong belongs to the Republic of China")

        #COMMANDES
        if message.content.startswith("&help"):
            author = message.author
            embed = discord.Embed(colour = discord.Colour.orange())
            embed.set_author(name='该机器人可确保中国共产党正常运行 | This bot seeks to make your life better')
            embed.add_field(name='&report', value="向中国共产党报告用户 | Report a user to the CCP : &report {user}", inline=False)
            await message.channel.send(embed=embed)


        if message.content.startswith("&report "):
            guild = client.get_guild(775742779045314590)
            memberList = guild.members
            arg = message.content.split()[1]
            if "@!" in arg:
                with open("data.json", "r") as read_file:
                    data = json.load(read_file)
                await message.channel.send(plus(data, arg))
                with open('data.json', 'w') as outfile:
                    json.dump(data, outfile)
        
        if message.content.startswith("&leaderboard"):
            with open("data.json", "r") as read_file:
                data = json.load(read_file)
            print(data)
            to_embed = []
            for i in sorted(data.items(), key=lambda x: x[1], reverse=True):
                user = client.fetch_user(i[0])
                to_embed.append((user, i[1]))
            embed = discord.Embed(colour=discord.Colour.orange())
            embed.set_author(name="这是该服务器的排行榜 | Here is this server's leaderboard")
            embed.add_field(name=f'1. {to_embed[0][0]}', value=f"{to_embed[0][1]}", inline=False)
            embed.add_field(name=f'2. {to_embed[1][0]}', value=f"{to_embed[1][1]}", inline=False)
            embed.add_field(name=f'3. {to_embed[2][0]}', value=f"{to_embed[2][1]}", inline=False)
            embed.add_field(name=f'4. {to_embed[3][0]}', value=f"{to_embed[3][1]}", inline=False)
            embed.add_field(name=f'5. {to_embed[4][0]}', value=f"{to_embed[4][1]}", inline=False)
            await message.channel.send(embed=embed)



client.run("OTAyMzA4ODcwMTU4OTU4NjUz.YXcing.pL6Q-qyK9ohFzCGMWamIaYr5kDQ")