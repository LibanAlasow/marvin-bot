import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import *

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
client = commands.Bot(command_prefix="-", help_command=None, intents=intents)
commands = []
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name="Just Fun")
    await client.change_presence(status=discord.Status.idle, activity=activity)




prefix = "-"



@client.event
async def on_member_join(member):
   if member.guild.id == 927307720451833896:
     await client.get_channel(927603402333098075).send(embed=discord.Embed(description=f"Welcome {member.mention} to our community, we're glad you joined!").set_author(name=f"{member.name} is now an official member", icon_url=member.avatar_url))

@client.event
async def on_member_remove(member):
   if member.guild.id == 927307720451833896:
     await client.get_channel(927603402333098075).send(embed=discord.Embed(description=f"{member.mention} Left the server!").set_author(name=f"{member.name} left", icon_url=member.avatar_url))




































from ro_py import Client





roblox = Client("C9446B052EFC196292BEE5100DC939D125DF7187C0E444919F2A86B3E91D14ABFF0C6008E332C11AB05B1AA690A5EC9AE8B2DBA3F8DF709481584BE91F65FE68920B3C14CD8220E8E758D19CEEC3B5B896505AFA407A50DC2D1B1C6EBF31381F1D523EF5C454393417425777FD27D4A519BB3DB6533B24613E86D3A542BD9F27EA6CF3065D9843E92BC448BD29E652B31CC68245AF25C59E6B81B1A3CE6F548D9675D6E5DA25BB34082105FA2740ED93025971D5899CF987C898BA6DEE52CF450C06E8D2CD5C4EBA855EE23214F8A3BF6B0F5324553B8D7CD4CCE45677A705D894A4B2B3BFC05207904DD890019371156FAB04AA34384EA1FA73E33891208909EE4E37EACB035EC780A758DE81D75EF6ACDB017CE8364418457007CE15ED883C27E19FD234ABC3BEA5BF851783B316C8B963C3A2C9139CC35B15681E6568F5471028280E57EE91633868E6DDAF01EBDEC20CFE54")






commands.append({"name": "whois", "description": "This command will get information about a roblox player", "usuage": f"{prefix}whois <username>", "category": "roblox"})
from ro_py.thumbnails import ThumbnailSize, ThumbnailType
@client.command("whois")
async def whois(ctx, username):
    user = await roblox.get_user_by_username(username)
    embed = discord.Embed(title=f"Info for {user.name}")
    embed.add_field(
        name="Username",
        value="`" + user.name + "`"
    )
    embed.add_field(
        name="Display Name",
        value="`" + user.display_name + "`"
    )
    embed.add_field(
        name="User ID",
        value="`" + str(user.id) + "`"
    )
    embed.add_field(
        name="Description",
        value="```" + (user.description or "No description") + "```"
    )

    avatar_image = await user.thumbnails.get_avatar_image(
        shot_type=ThumbnailType.avatar_headshot,
        size=ThumbnailSize.size_420x420, 
        is_circular=False 
    )
    embed.set_thumbnail(
        url=avatar_image
    )
    await ctx.send(embed=embed)







commands.append({"name": "get_group", "description": "This command will get information about a roblox group", "usuage": f"{prefix}get_group <id>", "category": "roblox"})
@client.command("get_group")
async def get_group(ctx, id):
  group = await roblox.get_group(id)
  icon_url = await group.owner.thumbnails.get_avatar_image(
        shot_type=ThumbnailType.avatar_headshot,
        size=ThumbnailSize.size_420x420, 
        is_circular=False 
    )
  await ctx.send(
    embed = discord.Embed(description=group.description)
      .set_author(name=group.name + f' by {group.owner.name}', icon_url=icon_url)
      .add_field(name="```group members```", value=group.member_count, inline=True)
      .add_field(name="```group id```", value=group.id, inline=True)
      .add_field(name="Last shout", value=f'``` {group.shout} ```', inline=False)
      
  )


commands.append({"name": "get_avatar", "description": "This command will get get the avatar of a user", "usuage": f"{prefix}get_avatar <username>", "category": "roblox"})
@client.command("get_avatar")
async def get_avatar(ctx, username):
  user = await roblox.get_user_by_username(username)
  try:
    icon_url = await user.thumbnails.get_avatar_image(
        size=ThumbnailSize.size_420x420, 
        is_circular=False 
    )
    await ctx.send(embed=discord.Embed(description=f'{user.name}\'s Avatar').set_image(url=icon_url))
  except:
    await ctx.send(embed=discord.Embed(description=f'Cannot find the username {username}'))
    








import random


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
    
  levels = get_levels()
  print("get levels")
  if str(message.guild.id) in levels:
    print("guild in data")
    if str(message.author.id) in levels[str(message.guild.id)]:
      print("user in data")
      levels[str(message.guild.id)][str(message.author.id)]["xp"] += random.randint(15, 30)
    else:
      levels[str(message.guild.id)][str(message.author.id)] = {"xp": 0, "level": 0}
      levels[str(message.guild.id)][str(message.author.id)]["xp"] = random.randint(15, 30)

  else:
    levels[str(message.guild.id)] = {}
    levels[str(message.guild.id)][str(message.author.id)] = {}
    levels[str(message.guild.id)][str(message.author.id)]["xp"] = random.randint(15, 30)
    levels[str(message.guild.id)][str(message.author.id)]["level"] = 0
  
  if levels[str(message.guild.id)][str(message.author.id)]["xp"] >= 500:
    levels[str(message.guild.id)][str(message.author.id)]["xp"] = 0
    levels[str(message.guild.id)][str(message.author.id)]["level"] += 1
    await message.channel.send(embed=discord.Embed(description=f":confetti_ball: {message.author.mention} You're now in level **{levels[str(message.guild.id)][str(message.author.id)]['level']}**"))
    if message.guild.id == 927307720451833896 or 852868160901480468:
      if levels[str(message.guild.id)][str(message.author.id)]['level'] == 5:
        role = discord.utils.get(message.guild.roles, name="Active")
        await message.author.add_roles(role)
      if levels[str(message.guild.id)][str(message.author.id)]['level'] == 10:
        role = discord.utils.get(message.guild.roles, name="Very Active")
        await message.author.add_roles(role)

  save_levels(levels)

  await client.process_commands(message)




commands.append({"name": "help", "description": "This command will help you use the bot", "usuage": f"{prefix}help <category>", "category": "begin"})
@client.command("help")
async def help(ctx, cat=None):
  if cat == None:
    embed = discord.Embed(title="Help", description="Welcome, please select a category\n[Bot website](https://bot-dashboard.libanalasow.repl.co/)", inline=True)
    embed.add_field(name=prefix+"help roblox", value="These commands will interact with roblox")
    embed.add_field(name=prefix+"help begin", value="These commands will help you understand how the bot works")
    embed.add_field(name=prefix+"help mod", value="These commands will help you moderate your server")
    embed.add_field(name=prefix+"help fun", value="These commands will entertain you!")
    embed.add_field(name=prefix+"help tools", value="These commands will help you do things easier and quicker!")
    embed.set_author(name="Marvin", icon_url="https://media.discordapp.net/attachments/926020950351302666/926021015849562152/defaultnobackgroundicon.png?width=481&height=481")
    embed.set_footer(text="Creator Liban Alasow")
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
  elif cat == "fun":
    string = ""
    for i in commands:
      if i["category"] == "fun":
        string += f'{i["usuage"]}  *{i["description"]}*\n'

    embed = discord.Embed(description=string)
    embed.set_footer(text="commands in the category fun")
    await ctx.send(embed=embed)
  elif cat == "roblox":
    string = ""
    for i in commands:
      if i["category"] == "roblox":
        string += f'{i["usuage"]}  *{i["description"]}*\n'

    embed = discord.Embed(description=string)
    embed.set_footer(text="commands in the category roblox")
    await ctx.send(embed=embed)
  elif cat == "tools":
    string = ""
    for i in commands:
      if i["category"] == "tools":
        string += f'{i["usuage"]}  *{i["description"]}*\n'

    embed = discord.Embed(description=string)
    embed.set_footer(text="commands in the category tools")
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

def get_levels():
  with open("levels.json", "r") as f:
    return json.loads(f.read())
    f.close()

def save_levels(warningsdata):
  with open("levels.json", "w") as f:
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

commands.append({"name" : "kick", "description" : "This command will kick a member", "usuage":f"{prefix}kick <member> <reason>", "category": "mod"})
@client.command()
@discord.ext.commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member=None,*, reason=None):
  await ctx.message.delete()
  if reason == None:
    reason = "No provided reason for kick"
  if member == None:
    await ctx.send("sorry, you have to mention the member you'd like to kick")
  else:
    embed = discord.Embed(description=f"{member.mention} was kicked (`{reason}`)")
    await member.kick(reason=reason)
    await ctx.send(embed=embed)

commands.append({"name" : "ban", "description" : f"{prefix}This command will ban a member", "usuage":"ban <member> <reason>", "category": "mod"})
@client.command()
@discord.ext.commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member=None,*, reason=None):
  await ctx.message.delete()
  if reason == None:
    reason = "No provided reason for ban"
  if member == None:
    await ctx.send("sorry, you have to mention the member you'd like to ban")
  else:
    embed = discord.Embed(description=f"{member.mention} was banned (`{reason}`)")
    await member.ban(reason=reason)
    await ctx.send(embed=embed)
  


commands.append({"name" : "say", "description" : "Make the bot say something!", "usuage":f"{prefix}say <something>", "category": "fun"})
@client.command("say")
async def say(ctx,*, wut):
  await ctx.message.delete()
  await ctx.send(wut)


commands.append({"name" : "embed", "description" : f"Turn a regular message into an embed", "usuage":f"{prefix}embed <text>", "category": "fun"})
@client.command("embed")
async def embed(ctx,*, wut):
  await ctx.message.delete()
  await ctx.send(embed=discord.Embed(description=wut))


commands.append({"name" : "poll", f"description" : "Create a poll and let people vote", "usuage":"poll <text>", "category": "fun"})
@has_permissions(manage_messages = True)
@client.command("poll")
async def poll(ctx,*,text):
  await ctx.message.delete()
  e = await ctx.send(embed=discord.Embed(description=text).set_author(name=ctx.author.name+" created a poll" ,icon_url=ctx.author.avatar_url))
  await e.add_reaction("☑")
  await e.add_reaction("❎")


commands.append({"name" : "clear", "description" : "Clear messages", "usuage":f"{prefix}clear <amount>", "category": "tools"})
@client.command()
@has_permissions(manage_messages = True)
async def clear(ctx , amount=5):
  await ctx.channel.purge(limit=amount + 1)


commands.append({"name" : "rank", "description" : "Check your rank", "usuage":f"{prefix}rank", "category": "tools"})
@client.command()
async def rank(ctx , member: discord.Member = None):
  levels = get_levels()
  if member == None:
    await ctx.send(embed=discord.Embed(description=f"You are in level {levels[str(ctx.guild.id)][str(ctx.author.id)]['level']}").set_author(name=f"{ctx.author.name}'s Rank in {ctx.guild.name}", icon_url=ctx.author.avatar_url).set_footer(text=f"{levels[str(ctx.guild.id)][str(ctx.author.id)]['xp']}/500 XP"))
  else:
    await ctx.send(embed=discord.Embed(description=f"{member.mention} is in level {levels[str(ctx.guild.id)][str(member.id)]['level']}").set_author(name=member.name+f"'s Rank in {ctx.guild.name}", icon_url=member.avatar_url).set_footer(text=f"{levels[str(ctx.guild.id)][str(member.id)]['xp']}/500 XP"))


@client.command()
async def servers(ctx):
  await ctx.send(f"I am in **{len(client.servers)}** servers")

client.run(os.getenv("DISCORD_TOKEN"))