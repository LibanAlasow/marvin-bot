import discord
import os
import json
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="-", help_command=None)
commands = []
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

prefix = "-"

@client.event
async def on_message(message):
  if message.author == client: return
  if message.channel.type is discord.ChannelType.private: return
  if str(message.guild.id) in get_bad_words():
    dat = get_bad_words()
    for i in dat[str(message.guild.id)]:
      if i in message.content.upper():
        await message.delete()
        await message.channel.send(embed=discord.Embed(description=f'{message.author.mention} your message contained a prohibited word!'))
        warnData = get_warnings()
        user = message.author
        if str(message.guild.id) in warnData.keys():
          if str(user.id) in warnData[str(message.guild.id)].keys():
            warnData[str(message.guild.id)][str(user.id)] += 1
          else:
            warnData[str(message.guild.id)][str(user.id)] = 1
        else:
          warnData[str(message.guild.id)] = {}
          warnData[str(message.guild.id)][str(user.id)] = 1
        save_warnings(warnData)
        break
  await client.process_commands(message)




commands.append({"name": "help", "description": "This command will help you use the bot", "usuage": f"{prefix}help <category>", "category": "begin"})
@client.command("help")
async def help(ctx, cat=None):
  if cat == None:
    embed = discord.Embed(title="Help", description="Welcome, please select a category", inline=True)
    embed.add_field(name="help begin", value="These commands will help you understand how the bot works")
    embed.add_field(name="help mod", value="These commands will help you moderate your server")
    embed.set_author(name="Marvin", icon_url="https://media.discordapp.net/attachments/926020950351302666/926021015849562152/defaultnobackgroundicon.png?width=481&height=481")
    await ctx.send(embed=embed)
  elif cat == "mod":
    string = ""
    for i in commands:
      if i["category"] == "mod":
        string += f'{i["usuage"]}  *{i["description"]}*\n'

    embed = discord.Embed(description=string)
    embed.set_footer(text="commands in the category mod")
    await ctx.send(embed=embed)
  elif cat == "begin":
    string = ""
    for i in commands:
      if i["category"] == "begin":
        string += f'{i["usuage"]}  *{i["description"]}*\n'

    embed = discord.Embed(description=string)
    embed.set_footer(text="commands in the category begin")
    await ctx.send(embed=embed)
      


def get_warnings():
  with open("warnings.json", "r") as f:
    return json.loads(f.read())
    f.close()

def save_warnings(warningsdata):
  with open("warnings.json", "w") as f:
    f.write(json.dumps(warningsdata))
    f.close()

def get_bad_words():
  with open("badwords.json", "r") as f:
    return json.loads(f.read())
    f.close()

def save_bad_words(warningsdata):
  with open("badwords.json", "w") as f:
    f.write(json.dumps(warningsdata))
    f.close()


commands.append({"name": "warn", "description": "This command will warn a user", "usuage": f"{prefix}warn <user> <reason>", "category": "mod"})
@discord.ext.commands.has_permissions(kick_members=True)
@client.command("warn")
async def warn(ctx, user:discord.Member,*, reason="No reason provided"):
  warnData = get_warnings()
  if str(ctx.guild.id) in warnData.keys():
    if str(user.id) in warnData[str(ctx.guild.id)].keys():
      warnData[str(ctx.guild.id)][str(user.id)] += 1
    else:
      warnData[str(ctx.guild.id)][str(user.id)] = 1
  else:
    warnData[str(ctx.guild.id)] = {}
    warnData[str(ctx.guild.id)][str(user.id)] = 1
  
  embed = discord.Embed(description=f'{user.mention} was warned for `{reason}`')
  embed.set_footer(text=f'by {ctx.author.name}, {warnData[str(ctx.guild.id)][str(user.id)]} warnings', icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)
  save_warnings(warnData)

commands.append({"name": "remove warn", "description": "This command will warn a user", "usuage": f"{prefix}remove_warn <user>", "category": "mod"})
@discord.ext.commands.has_permissions(kick_members=True)
@client.command("remove_warn")
async def remove_warn(ctx, user:discord.Member):
  warnData = get_warnings()
  if str(ctx.guild.id) in warnData.keys():
    if str(user.id) in warnData[str(ctx.guild.id)].keys():
       if warnData[str(ctx.guild.id)][str(user.id)] >= 1:
         warnData[str(ctx.guild.id)][str(user.id)] -= 1
    else:
      warnData[str(ctx.guild.id)][str(user.id)] = 0
  else:
    warnData[str(ctx.guild.id)] = {}
    warnData[str(ctx.guild.id)][str(user.id)] = 0
  
  embed = discord.Embed(description=f'removed a warning from {user.mention}')
  embed.set_footer(text=f'by {ctx.author.name}, {warnData[str(ctx.guild.id)][str(user.id)]} warnings', icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)
  save_warnings(warnData)


commands.append({"name": "add_bad_word", "description": "This command will add a prohibited word to the server (one word per command!)", "usuage": f"{prefix}add_bad_word <word>", "category": "mod"})
@discord.ext.commands.has_permissions(kick_members=True)
@client.command("add_bad_word")
async def add_bad_word(ctx, word):
  bad_words = get_bad_words()
  word = str(word)
  await ctx.message.delete()
  if str(ctx.guild.id) in bad_words.keys():
    words = bad_words[str(ctx.guild.id)]
    if word.upper() in words:
      await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} that word is already listed'))
    else:
      words.append(word.upper())
      embed = discord.Embed(description=f'{ctx.author.mention} listed a prohibited word')
      await ctx.send(embed=embed)
    bad_words[str(ctx.guild.id)] = words
  else:
    bad_words[str(ctx.guild.id)] = []
    words = bad_words[str(ctx.guild.id)]
    words.append(word.upper())
    bad_words[str(ctx.guild.id)] = words
    embed = discord.Embed(description=f'{ctx.author.mention} listed a prohibited word')
    await ctx.send(embed=embed)
  save_bad_words(bad_words)


commands.append({"name": "bad_words", "description": "This command will send you a list of all the prohibited words)", "usuage": f"{prefix}bad_words", "category": "mod"})
@client.command("bad_words")
@discord.ext.commands.has_permissions(kick_members=True)
async def bad_words(ctx):
  string = ""
  words = get_bad_words()[str(ctx.guild.id)]
  for i in words:
    string += f'||{i.lower()}||\n'
  embed = discord.Embed(title="Prohibited words in " + ctx.guild.name, description=string)
  await ctx.author.send(embed=embed)
  await ctx.reply(embed=discord.Embed(description="sent in your DM"))

commands.append({"name": "remove_bad_word", "description": "This command will a remove specific prohibited word", "usuage": f"{prefix}remove_bad_word <word>", "category": "mod"})
@discord.ext.commands.has_permissions(kick_members=True)
@client.command("remove_bad_word")
async def remove_bad_word(ctx, word):
  await ctx.message.delete()
  bad_words = get_bad_words()
  if str(ctx.guild.id) in bad_words.keys():
    words = bad_words[str(ctx.guild.id)]
    if word.upper() in words:
      words.remove(word.upper())
      await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} removed a bad word'))
    else:
      await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} that word isn\'t listed!'))
    bad_words[str(ctx.guild.id)] = words
  else:
    await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} removed a bad word'))
  save_bad_words(bad_words)




client.run(os.getenv("DISCORD_TOKEN"))