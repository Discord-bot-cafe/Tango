import discord
from discord.ext import commands
import json
from discord.ui import Button, View
import random
import asyncio
from datetime import datetime
import praw
from discord_slash import SlashCommand, SlashContext
import time
import requests
from discord.ext.commands import Bot
import wikipedia
from keep_alive import keep_alive


TOKEN='OTQ4NDY3NjcxODc4NDk2Mjk3.Yh8PWg.ccHpufjp4v1DKkPVjr9Mgh1lfp4'

bot = commands.Bot(command_prefix='t!', activity=discord.Game(name="t!help for help"),help_command=None)
slash = SlashCommand(bot,sync_commands = True) 
guild_id = [949218723305238538]

reddit = praw.Reddit(client_id ="idMTAkYpGO4uLHn-TiTcoA",#
                    client_secret ="8CAl12wPM4hnS5qddd-SdNNVxfMQ3g",#
                    username ="Bulky_Carpet_6507",#8
                    password ="rama@gokul",#
                    user_agent ="tango lel")#

async def get_bank_data():
  with open("mainbank.json", "r") as f:
    users = json.load(f)
  return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    return bal

@bot.event
async def on_ready():
    print("The Tango BOT IS ONLINE")
    print("lol")

@bot.command()
async def help(ctx):
  economy = discord.Embed(title = 'Tango Economy Functions', description="**`t!bal` - To check your balance**\n**`userbal  <t!userbal @user>`  - Check any person's balance**\n **`t!buy   <t!buy item>` - Used to buy a item** \n**`t!crime` - Used to do random crimes for money**\n**`t!beg` - Beg to get random amount of coins**\n**`t!crx` - Check your coolness level 😎😎😎😎😎**\n**`t!crxu     <t!crxu @user>` - Check other's coolness**\n**`t!daily` - Collect your prize for nothing everyday!**\n**`t!dep` - Deposit you money from wallet to bank!**\n**`t!donate  <t!donate @user amount` - Donate your money to someone'**\n**`t!heist` - Heist a bank and rob money!**\n**`t!inventory` - Check you inventory**\n**`invest` - Invest in something and win or lose money (This is not real)**\n**`t!investstatus` - Check the status for you investment**\n**`t!leaderboard` - Check who is the richest person in the server**\n**`t!monthtly` - Claim you prize for doing nothing every month**\n**`t!rob      <t!rob @user>` - Rob anyone and get money**\n**`t!rob      <t!rob @user>` - Rob anyone and get money**\n**`t!shop` - See the shop and check if you can afford something**\n**`t!sell       <t!sell item>` - Sell the item you want to for money**\n**`t!sellstox` - Sell you stox and see if you got or lost money by investing!**" )
  await ctx.send(embed=economy)

  games = discord.Embed(title = 'Tango Games', description = '**`t!ttt    <t!ttt @user>` - Used To play a game of tic tac toe with you friends!**\n**`t!place   <t!place number>` - Used to place your token in the tic tac toe**\n**`t!rockpapperscissors` - PLay a game of rock paper scissors against a computer**\n**`t!trivia` - Play a Quiz!!!**')

  fun = discord.Embed(title = 'Tango Fun Functions', description = '**`t!bday  <t!bday @user>` - Wish someone on their birthday**\n**`t!hack   <t!hack @user>` - Hack someone**0\n**`t!meme   <t!meme *type of meme*>` - Wtach some of the most funny memes!!!**\n**`t!space` - Go on a space adventure and hopefully get some coins!**\n**THERE ARE MANY MORE COMMADNS WHICH WE ARE LEAVING TO YOU TO FIND OUT!!!!**')

  

  await ctx.send(embed = games)
  await ctx.send(embed=fun)
@bot.command()
async def bday(ctx,member : discord.Member,*,msg = ''):
  r = random.randrange(0,255)
  g = random.randrange(0,255)
  b = random.randrange(0,255)
  em = discord.Embed(title = 'Present sent!',color = discord.Color.from_rgb(r,g,b))
  em.set_footer(text = 'Wait untill you see his reaction')
  await ctx.send(embed = em)
  for i in range (1,50):

    await member.send('HAPPY BITHDAY!!!!!')
  else:
    if msg == '':
      pass
    else:
      e = discord.Embed(title = f'Present by {ctx.author.name}',
                       description = f'{ctx. author.name} has left a message!: ',
                       color = discord.Color.from_rgb(r,g,b))
      e.set_footer(text = msg)
                        
      await member.send(embed = e)

@bot.command(aliases=['INFO', 'Info'])
async def invite(ctx):
    now = datetime.now()

    current_time = now.strftime("%H:%M")
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    user = ctx.author
    embedVar = discord.Embed(
        title="Bot Invite link. press the link to invite the bot to your server",
        description=
        "https://discord.com/api/oauth2/authorize?client_id=948467671878496297&permissions=8&scope=bot",
        colour=discord.Colour.from_rgb(r, g, b))
    embedVar.set_footer(text=f"😏 {current_time} lol")
    file = discord. File("lolgo.jpg", filename="image.png")
    embedVar.set_image(url= "attachment://image.png")  
    await ctx.send(embed=embedVar)#run bot

@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def crime(ctx):
  user = ctx.author
  await open_account(ctx.author)
  users= await get_bank_data()
  crime = random.choice(["vandalism", "murder", "hecking", "shoplifting"])
  
  crime_paisa = random.randrange(0,3)
  krimesuces = random.randrange(200,5000)
  # contineu 
  if crime_paisa == 1:
    em = discord.Embed(title="unsuccesful crime", description=f"ur {crime} was unsuccesful  and u lost 20% of ur money")
    em.set_footer(text = 'next time try but never give up')

    benk = users[str(user.id)]["bank"] 
    welat = users[str(user.id)]["wallet"]
    totel = benk+welat
    totelhalf = totel/5
    await update_bank(ctx.author, -1*totelhalf)
    await ctx.send(embed=em)
  else:
    emblol = discord.Embed(title = "CRIME SUCCESFULL",description = f'{crime} was succesefull and u got {krimesuces}')
    await update_bank(ctx.author, krimesuces)
    
    await ctx.send(embed = emblol)
    
    
@bot.command()
async def invest(ctx,howmuchmoni, invest_item = 'None'):
  howmuchmoney = int(howmuchmoni)
  await open_account(ctx.author)
  user=ctx.author
  users=await get_bank_data()
  invbest_items = ['Bitcoin','Dogecoin','DBC','Gold','idkcoin','Indianrupees', 'belubucks']
  await ctx.send('This is not real!')
  await asyncio.sleep(5)
  userbal = users[str(user.id)]["wallet"]
  if invest_item == 'None':
    await ctx.send('Bruh in what will you invest in?')
  elif invest_item not in invbest_items:
    await ctx.send(f"Bruh {invest_item} aint available unfortunately")
  elif int(howmuchmoni) < 1000000:
    await ctx.send("You cant invest less than 1000000 in Tango.")
  elif (int(howmuchmoni) > 999999) and (userbal < 999999):
    await ctx.send("You have less than 1mln tangies in ur wallet so u cant invest .lol noob")
  else:
    users[str(user.id)]["investment"] += howmuchmoney
    users[str(user.id)]["investedin"]= invest_item
    users[str(user.id)]["originalinvestment"] += howmuchmoney
    users[str(user.id)]["wallet"] -= howmuchmoney
    await ctx.send(f"You have successfully invested **{howmuchmoni} in {invest_item}**")
    await ctx.send("your money will be returned to you after 2 years in tango logic(300 times of investment on running the command t!isellstox) of investment")

  with open("mainbank.json", "w") as f:
    json.dump(users,f)
  return True 

@bot.command()
@commands.cooldown(1, 7200, commands.BucketType.user)
async def sellstox(ctx):
  user=ctx.author
  users=await get_bank_data()
  await open_account(ctx.author)
  timesinvested=users[str(user.id)]["timesinvested"]
  originalinvestment = users[str(user.id)]["originalinvestment"]
  userinvestment= users[str(user.id)]["investment"]
  userinvestedin = users[str(user.id)]["investedin"]
  
  if (users[str(user.id)]["timesinvested"]<301):
    lossorpropitbyselling = random.randrange(-20000, 20001)
    await ctx.send(f"WAH, YOU WON {lossorpropitbyselling} tangies by investing in {userinvestedin}")  
    users[str(user.id)]["investment"] += lossorpropitbyselling
    users[str(user.id)]["timesinvested"]+=1

  elif (users[str(user.id)]["timesinvested"]>300):
    await ctx.send("You successfully invested for 2 years")
    lemon = userinvestment -originalinvestment
    if userinvestment > originalinvestment:
      profitpercent = (lemon/originalinvestment)*100
      em = discord.Embed(title="Profit detected in investment", description=f"You got a profit of **{lemon}** by investing **{originalinvestment}. A profit of {profitpercent}%**", color = discord.Colour.random())
      await ctx.send(embed=em)
      users[str(user.id)]["wallet"] += userinvestment
      users[str(user.id)]["originalinvestment"] = 0
      users[str(user.id)]["investment"] = 0
      users[str(user.id)]["investedin"] = ' '
      users[str(user.id)]["timesinvested"] = 0
    else:
      em = discord.Embed(title="LOSS 😥 detected in investment", description=f"You got a profit of **{lemon}** by investing **{originalinvestment}**", color = discord.Colour.random())
      await ctx.send(embed=em)
      users[str(user.id)]["originalinvestment"] = 0
      users[str(user.id)]["investment"] = 0
      users[str(user.id)]["wallet"] += userinvestment
      users[str(user.id)]["investedin"] = ' '
      users[str(user.id)]["timesinvested"] = 0
      
  with open("mainbank.json", "w") as f:
    json.dump(users,f)
  return True 

@sellstox.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"Hey guys, if you spam, you banned",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
  user = ctx.author
  await open_account(user)
  users = await get_bank_data()

  if users[str(user.id)] ["Profession"] == 'None':
    await ctx.send('first get a job use `t!get_job` to get a job u jobless dumbo!')
  else:
    await ctx.send('working..')
    userselery = users[str(user.id)]["salary"]
    lel = random.randrange(0,  6)
    if lel == 1:
      users[str(user.id)]["wallet"] += userselery
      await ctx.send(f"YOU EARNED **{userselery}** as your salary for this month.")
    elif lel == 2:
      salry2 = userselery-2000
      users[str(user.id)]["wallet"] += salry2
      await ctx.send(f"YOU EARNED **{salry2}** as your salary for this month.")
    elif lel == 3:
      salry3 = userselery-400
      users[str(user.id)]["wallet"] += salry3
      await ctx.send(f"YOU EARNED **{salry3}** as your salary for this month.")
    elif lel == 4:
      salry4 = userselery-6000
      users[str(user.id)]["wallet"] += salry4
      await ctx.send(f"YOU EARNED **{salry4}** as your salary for this month.")
    else:
      await ctx.send("```I am very sad to say u dint earn **ANY MONEY**```")
    
    time.sleep(5)
    await ctx.send("lol")
    time.sleep(5)
    
  with open("mainbank.json", "w") as f:
    json.dump(users,f)
  return True 

@work.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"overworking for late hrs isnt good for health",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)



@bot.command()
async def get_job(ctx):
  user = ctx.author
  
  await open_account(user)
  
  users = await get_bank_data()

  jobs = ['docter','lawyer','scemer','hecker','coder', 'babysitter']
  
  if users[str(user.id)] ["Profession"] == 'None':
    await ctx.send('searching a suitable job for you...')
    job_for_him = random.choice(jobs)
    time.sleep(2)
    await ctx.send(f'Got it! The perfect job for yu is {job_for_him} and ur salary will depend on ur work. you will get paid on an hourly basis but dont spoil ur money on waste thingz.')
    users[str(user.id)]["Profession"] = job_for_him
    if job_for_him == 'docter':
      seleri = 15000
      users[str(user.id)]["salary"]=seleri
    elif job_for_him == 'lawyer':
      seleri = 16000
      users[str(user.id)]["salary"]=seleri
    elif job_for_him == 'scemer':
      seleri = 8000
      users[str(user.id)]["salary"]=seleri
    elif job_for_him == 'hecker':
      seleri = 17000
      users[str(user.id)]["salary"]=seleri
    elif job_for_him == 'coder':
      seleri = 19000
      users[str(user.id)]["salary"]=seleri
    elif job_for_him == 'babysitter':
      seleri = 10000
      users[str(user.id)]["salary"]=seleri
  else:
    await ctx.send('You already have a job!')
  
  with open("mainbank.json", "w") as f:
    json.dump(users,f)
  return True 
#btw send come 5o chetdbc sar

@get_job.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"You cant multijob lol",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)


@bot.command()
@commands.cooldown(1, 18000, commands.BucketType.user)
async def resign(ctx):
  user=ctx.author
  users=await get_bank_data()
  await open_account(ctx.author)
  job=users[str(user.id)]["Profession"]
  salry=users[str(user.id)]["salary"]
  await ctx.send(f"successfully resigned from job of {job} with salary of {salry} per hour")
  users[str(user.id)]["Profession"]="None"
  users[str(user.id)]["salary"]=0
  with open("mainbank.json", "w") as f:
    json.dump(users,f)
  return True 

@resign.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"WE DONT PROMOTE **OVERRESIGNATIION**",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def investstatus(ctx):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  await open_account(ctx.author)
  user=ctx.author
  users=await get_bank_data()
  inv = users[str(user.id)]["investment"]
  tinv = users[str(user.id)]["timesinvested"]
  oinv=users[str(user.id)]["originalinvestment"]
  invi=users[str(user.id)]["investedin"] 
  em=discord.Embed(title=f"{ctx.author}'s investment stats'", description=f"**user investment: {inv}**\n **original i nvestment: {oinv}**\n **Times invested:{tinv}**\n**Invested in :{invi}**", color = discord.Colour.from_rgb(r, g, b))
  await ctx.send(embed=em)

@investstatus.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"WE DONT PROMOTE **OVERRESPAMMIN**",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)
      
@bot.command(aliases=["Bal", "BAL"])
async def bal(ctx):
  

  now = datetime.now()

  current_time = now.strftime("%H:%M")

  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  await open_account(ctx.author)
  users = await get_bank_data()
  user = ctx.author
  
  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]
  totelmoni = wallet_amt + bank_amt
  em = discord.Embed(title = f"{ctx.author.name}'s balance", description=f"**Wallet Balance : {wallet_amt} tangies \n Bank Balance : {bank_amt} tangies\n Total Money : {totelmoni} tangies **", colour=discord.Colour.from_rgb(r, g, b))
  em.set_footer(text=f'😏 dumbos lukin smart ... {current_time}')
  await ctx.send(embed = em)

@bot.command(aliases=["userbal"])
async def beluge(ctx, member:discord.Member):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  await open_account(member)
  users = await get_bank_data()
  user = member
  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]
  totelmoni = wallet_amt + bank_amt
  em = discord.Embed(title = f"{member}'s balance", description=f"**Wallet Balance : {wallet_amt} tangies \n Bank Balance : {bank_amt} tangies\n Total Money : {totelmoni} tangies **", colour=discord.Colour.from_rgb(r, g, b))
  em.set_footer(text=f'😏 dumbos lukin smart ...')
  await ctx.send(embed = em)

  
@bot.command()
async def meme(ctx,*,meme = 'None'):
  subreddit = reddit.subreddit(meme)
  all_memes = []
  top = subreddit.top(limit = 100)
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)

  if meme == 'None':
    meme = 'meme'
  for submission in top:
    all_memes.append(submission)
  random_meme = random.choice(all_memes)

  name = random_meme.title
  url = random_meme.url

  em = discord.Embed(title = name,
                    color = discord.Color.from_rgb(r,g,b))
  em.set_footer(text = '🤣🤣🤣🤣🤣😂😂😂😂😂😂😂😎😎😎😎😎')

  em.set_image(url = url)
  await ctx.send(embed = em)

@bot.command()
async def hack(ctx, member):
  user = ctx.author
  await open_account(user)
  if ctx.author==member:
    await ctx.send("Dumbo, you cant hack yoursgeelf")
  else:
      msg = await ctx.send('H')
      await asyncio.sleep(1)
      await msg.edit(content="Ha")
      await asyncio.sleep(1)
      await msg.edit(content="Hac")
      await asyncio.sleep(1)
      await msg.edit(content="Hack")
      await asyncio.sleep(1)
      await msg.edit(content="Hacki")
      await asyncio.sleep(1)
      await msg.edit(content="Hackin")
      await asyncio.sleep(1)
      await msg.edit(content="Hacking")
      await asyncio.sleep(1)
      await msg.edit(content=f'Well this is not easy {ctx.author}, have some patience! {ctx.author}')
      await asyncio.sleep(1)
      await msg.edit(content=f"Hacked {member}")
      await asyncio.sleep(1)
      await msg.edit("credentials leaked in facebook and twitter LOL")
    

@bot.command()
async def thoughtofday(ctx):
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  await ctx.send("```YOUR THOUGHT OF THE DAY for assembly:```")
  await ctx.send(quote)

  

@bot.command(aliases = ['BEG','Beg'])
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  user = ctx.author
  await open_account(user)

  users = await get_bank_data()

  earnings =random.randrange(2,2500)

  em = discord.Embed(title="*YOU GOT SOME MONEY*", description=f'Someone was kind enough to give you {earnings} tangies!', colour = discord.Colour.from_rgb(r, g, b))
  em.set_footer(text="Garib aadmi : tomorrowtides.com")
  users[str(user.id)]["xp"] += 1
  await ctx.send(embed=em)

  users[str(user.id)]["wallet"] += earnings

  with open("mainbank.json", "w") as f:
        json.dump(users, f)
  return users

@beg.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"Spam Isn't cool Fam!",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
async def dep(ctx, money= 'None'):
  user = ctx.author
  users = await get_bank_data()
  walet = users[str(user.id)]["wallet"]
  if money == 'None':
    money = walet
  money = int(money)
  now = datetime.now()

  current_time = now.strftime("%H:%M")

  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  await open_account(ctx.author)
  
  if walet <= 0:
    await ctx.send("no money to deposit. error 404")
  else:
    users[str(user.id)]["wallet"] -= money
    users[str(user.id)]["bank"] +=money
    users[str(user.id)]["xp"] += 1
    
  
    embedVar = discord.Embed(title = 'Successful Transaction',
                            description = f'{money} tangies was shifted to the bank securely' ,
                            color = discord.Color.from_rgb(r,g,b))
  
    embedVar.set_footer(text=f"Rick Astley is impressed with your balanse 😏{current_time}")
    await ctx.send(embed=embedVar)
  with open("mainbank.json", "w") as f:
        json.dump(users, f)
  return users

@bot.command(aliases = ["with"])
async def withdraw(ctx, money = 'None'):
  user = ctx.author
  users = await get_bank_data()
  benk = users[str(user.id)]["bank"]

  if money == 'None':
    money = benk
  money = int(money)
  now = datetime.now()

  current_time = now.strftime("%H:%M")
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  await open_account(ctx.author)
  

  if benk <= 0:
    await ctx.send("You have no money to withdraw huh, wat a fool.")
  else:
    users[str(user.id)]["wallet"] +=money
    users[str(user.id)]["bank"] -=money  
    benk = users[str(user.id)]["bank"]
    embedVar = discord.Embed(title = 'Successful Transaction',       description = f'{money} tangies was  shifted to the wallet securely', color = discord.Color.from_rgb(r,g,b))
  
  
    embedVar.set_footer(text="Hah what a fool 😏")
  
    users[str(user.id)]["xp"] += 1
                             
    await ctx.send(embed=embedVar) 
  with open("mainbank.json", "w") as f:
        json.dump(users, f) #chek disco
  return users

@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def heist(ctx):
  user = ctx.author
  await open_account(user)
  users = await get_bank_data()
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  heist_result = random.randrange(0,2)
  heist_profit = random.randrange(1,10000)
  heist_loss = random.randrange(1,200000)

  wallet_amt = users[str(user.id)]["wallet"]
  wallet_int = int(wallet_amt)

  if wallet_amt < 200000:
    em = discord.Embed(title="Not worthy of heisting", description=f"Garib aadmi = {user}", color=discord.Color.from_rgb(r, g, b))
    em.set_footer(text="😏")
    await ctx.send(embed=em)
    
  else:

    if heist_result == 0:
      users[str(user.id)]['wallet'] += heist_profit
      em = discord.Embed(title = 'Heist Succesfull!!!!!!!!!',
                         description = f'The heist was succesfull and you got {heist_profit} tangies!!',
                         color = discord.Color.from_rgb(r,g,b))
      em.set_footer(text="🤣😂")
      await ctx.send(embed = em)
      users[str(user.id)]["xp"] += 1
    elif heist_result == 1:
      users[str(user.id)]['wallet'] -= heist_loss
      em = discord.Embed(title= 'You got caught!',
                         description =f'You were caught by police and charged {heist_loss}',
                         color = discord.Color.from_rgb(r,g,b))#
      em.set_footer(text="🤣😂")
      await ctx.send(embed = em)
      users[str(user.id)]["xp"] += 1
    else:
      await ctx.send("*No propit / loss lolol*"
                    )
      users[str(user.id)]["xp"] += 1#lelelelelel secret messsage which is not accesiblre

  with open("mainbank.json", "w") as f:
        json.dump(users, f) #chek disco
  return users
    
@heist.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"Hey guys, if you spam, you banned",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1,75 , commands.BucketType.user)
async def donate(ctx, member:discord.Member, money):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  money = int(money)
  await open_account(ctx.author)
  await open_account(member)

  user = ctx.author
  await open_account(ctx.author)
  users = await get_bank_data()

  moneytobegiven = money
  usermoney = users[str(user.id)]["wallet"]
  if usermoney < 300000:
    em = discord.Embed(title="not worthy of donating money", description = f"Bhikari lol = {ctx.author}", colour = discord.Colour.from_rgb(r, g, b))
    em.set_footer(text="😏😏")
    await ctx.send(embed=em)
  else:
    await update_bank(ctx.author, -1*money)
    await update_bank(member, money)
    em = discord.Embed(title="Donation successful", description=f"{ctx.author} has successfully donated {money} tangies to {member}", colour = discord.Colour.from_rgb(r, g, b))
    em.set_footer(text="🤑💸💰")
    users[str(user.id)]["xp"] += 5
    await ctx.send(embed=em)

@donate.error
async def command_name_error(ctx, error):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  if isinstance(error, commands.CommandOnCooldown):
    em = discord.Embed(
            title=f"IDIOT, STOP SPAMMING ",
            description=f"Try again in {error.retry_after:.2f}s.",
            color=discord.Colour.from_rgb(r, g, b))
    em.set_footer(text="😆")
    await ctx.send(embed=em)

mainshop = [{"name":"Magic Orange","id": " `mo` ","price": 500,"description":'A really magical orange'},     
            {"name":"Apple","id":" `a`","price": 10000,"description":"it's a privilege level 2 item"}, 
            {"name":"Akshat's Laptop and REPLIT", "id":"`precious`", "price":15000000000, "description":"Extremely costly, only the richest can afford it."},
            {"name":"Rama's flower", "id":"`rf`", "price":10000000000, "description":"Extremely costly, only one of richest can get it"},
            {"name":"Banana", "id":"`bn`", "price": 1500, "description":"only to go bananas"},
            {"name":"mango", "id":"`mn", "price": 1500000, "description":"its an amazing mango which is really tasty"}, 
            {"name":"tango crown", "id":"`tc`", "price":150000000000, "description":"**ONLY THE RICHEST CAN AFFORD IT OFFER VALID FOR ONLY 730 DAYS (4/3/22-4/3/24)**"},
           {"name":"monkey", "id":"`mk`", "price":159000, "description":"**very op monkey**"}, 
           {"name":"noonecangetit", "id":"`nocgi`", "price":999999999999999999999999999999999999999, "description":
           "THE MOST EXPENSIVE ITEM IN TANGO."}, 
           {"name":"Tango bot", "id":"tg", "price":45886482578421045210456842145587675321012458635401786252145664684546873548673, "description":"Get this, and im passin the bot over to ya"}]

@bot.command()
async def shop(ctx):
  r= random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  em = discord.Embed(title = '.                   Shop                  .', color = discord.Colour.from_rgb(r, g, b))
  em.set_footer(text="op shop  lmeo")

  for item in mainshop:
    name = item["name"]
    price = item["price"]
    desc = item["description"]
    id = item["id"]
    em.add_field(name = name, value = f" id:{id}\n{price} tangies \n{desc}")
  await ctx.send(embed = em)

@bot.command()
async def use(ctx,i):
  user = ctx.author()
  await open_account(user)
  with open("mainbank.json", "r") as f:
    users = json.load(f)
  for i in range(users):
    if users[str(user.id)]["bag"] == i:
      i -= users.bag
      if i == 'mo':
        meney = random.randrange(100,600)
        users[str(user.id)]["wallet"] += meney 
        await ctx.send('Money sent')
      elif i == 'a':
        users[str(user.id)]["wallet"] *= 2
        ctx.send('ok!')
  
  

@bot.command(aliases = ['inv'])
async def inventory(ctx):
    r=random.randrange(0, 255)
    g=random.randrange(0, 255)
    b=random.randrange(0, 255)
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title=f"{user}'s inventory'", color = discord.Colour.from_rgb(r, g, b))
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)

@bot.command()
async def sell(ctx,item,amount = 1):
    r=random.randrange(0, 255)
    g=random.randrange(0, 255)
    b=random.randrange(0, 255)
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount=1)

    if not res[0]:
        if res[1]==1:
            em = discord.Embed(title="Object not found", description="The object you have mentinoned isnt found", color = discord.Colour.from_rgb(r, g, b))
            await ctx.send(embed=em)
            return
        if res[1]==2:
            em = discord.Embed(title="Object not found", description="The object you have mentinoned isnt found in your bag", color = discord.Colour.from_rgb(r, g, b))
            await ctx.send(embed=em)
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    em = discord.Embed(title="successful sale", description=f"You just sold {amount} {item}", color = discord.Colour.from_rgb(r, g, b))
    await ctx.send(embed=em)

async def sell_this(user,item_name,amount=1,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["id"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.55* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt <0:
                  return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
          return [False, 3]
    except:
      return [False, 3]


    await update_bank(user, cost * -1, "wallet")
    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return [True, "Worked"]


@bot.command()
async def buy(ctx, item, amount=1):
    r=random.randrange(0, 255)
    g=random.randrange(0, 255)
    b=random.randrange(0, 255)
    amount = 1
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount=1)

    if not res[0]:
        if res[1] == 1:
            embedVar = discord.Embed(title="error", description=f"You don't have enough tangies in your wallet to buy {amount} {item}", color=198)
            await ctx.send(embed=embedVar)
            return
        if res[1] == 2:
            embedVar = discord.Embed(title="error", description="Item not found sorry", color=discord.Colour.from_rgb(r, g, b))
            await ctx.send(embed=embedVar)
            return
    await ctx.send(f"You just bought {amount} {item}")

async def buy_this(user, item_name, amount):
    amount = 1
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["id"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]

    if name_ == None:
        return [False, 1]

    cost = price * 1

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount":amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]

@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def rob(ctx, member:discord.Member):
  r =random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  await open_account(ctx.author)
  await open_account(member)

  user = ctx.author
  await open_account(ctx.author)
  users = await get_bank_data()
  bal = await update_bank(member)
  usrrpaisa = users[str(user.id)]["wallet"]
  
  if bal[0] <100000:
    await ctx.send(f"**{member} isnt worthy of getting robbed. You need to have minimum 100000 to get robbed**")
    return False
  elif usrrpaisa < 100000:
    await ctx.send(f"**{ctx.author}, You arent worthy of robbin people. You must have 100000 in wallet to rob people**")
    return False
  
  earnings = random.randrange(0, 100000)
  successornot = random.randrange(0, 2)
  if successornot == 1:
      await update_bank(ctx.author, earnings)
      await update_bank(member, -1*earnings)
      em = discord.Embed(title=f"Robbery successful for {ctx.author}", description=f"{ctx.author} robbed {earnings} from {member}. LOL", color = discord.Colour.from_rgb(r, g, b))
      em.set_footer(text=f"{ctx.author}, ameer ban gaya kya")
      await ctx.send(embed=em)
  else:
    await update_bank(ctx.author, -1*earnings)
    await update_bank(member, earnings)
    em = discord.Embed(title=f"Robbery unsuccessful for {ctx.author}", description=f"{ctx.author} paid fine of {earnings} to {member}. LEL HAPPENED", color = discord.Colour.from_rgb(r, g, b))
    em.set_footer(text=f"{member}, ameer ban gaya kya!!!")
    users[str(user.id)]["xp"] += 1
    await ctx.send(embed=em)  

@rob.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"No spam pls",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)


@bot.command()
async def profile(ctx):
  await open_account(ctx.author)
  user = ctx.author
  users=await get_bank_data()
  r = random.randrange(0, 255)
  g=random.randrange(0, 255)
  b =random.randrange(0, 255)
  em=discord.Embed(title=f"{ctx.author}'s profile", color = discord.Colour.from_rgb(r, g, b))
  bank = users[str(user.id)]["bank"]
  wallet = users[str(user.id)]["wallet"]
  xp = users[str(user.id)]["xp"]
  oriinves = users[str(user.id)]["originalinvestment"]
  investin = users[str(user.id)]["investment"]
  lossorpopet=0
  if investin <oriinves:
    loss=oriinves-investin
    lossorpopet=-(loss)
  else:
    propet=oriinves-investin
    lossorpopet=propet
    
  em.add_field(name=f"~{user}'s balance~", value=f"Bank Balance: {bank}\n Wallet Balance: {wallet}")
  em.add_field(name=f"~       {user}'s xp~", value = f"User xp : {xp}")
  em.add_field(name=f"{user}'s investin status(only loss or profit)'", value=f"Investment value: {lossorpopet}")

  await ctx.send(embed=em)

@bot.command()
async def xp(ctx):
  r = random.randrange(0, 255)
  g=random.randrange(0, 255)
  b =random.randrange(0, 255)
  user = ctx.author
  users=await get_bank_data()
  await open_account(ctx.author)
  autherxp = users[str(user.id)]["xp"]

  em = discord.Embed(title=f"{user} xp", description=f"**User xp/experience points: {autherxp}**\n This value determines your wealth and your experience in Tango", color = discord.Colour.from_rgb(r, g, b))
  em.set_footer(text="😏😏😏😏😏😏")
  await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1, 10000, commands.BucketType.user)
async def spamindm(ctx, member:discord.Member, whatuwannasend=' '):
  spemindm = random.randrange(0, 15)
  if (spemindm == 1) or (spemindm==3) or (spemindm==5) or (spemindm==7) or (spemimdm==9) or (spemindm==11) or (spemindm==13) or (spemindm==15):
    await ctx.send(f"**Haha spam is successful @{ctx.author}. You will spam 1000 times successfully in {member}'s dm'**")
    for i in range(0, 1000):
      await member.send(f"**{whatuwannasend}**")
  else:
    await ctx.send(f"**unsuccessful spam {ctx.author} sadd.**")

@spamindm.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"Hey guys, if you spam, you banned",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command(aliases=['Tango'])
async def tango(ctx):
  em=discord.Embed(title="Tango", color = discord.Colour.from_rgb(255, 174, 66))
  em.add_field(name="What's Tango", value="Tango is multipurpose fun economy bot build by DBC(Discord Bot Cafe.) Has atleast 50+ commands with containing various kinds of stuff.", inline=False)
  em.add_field(name="What does tango have?", value="It has many types of commands like economy, fun, games, moderation etc. You will love it when u use the bot. Its packed with various kinds of features.", inline=False)
  await ctx.send(embed=em)

@bot.command(aliases=["lb"])
async def leaderboard(ctx, x=15):
  users=await get_bank_data()
  leader_board={}
  total=[]
  for user in users:
    name=int(user)
    total_amount = users[user]["wallet"]+users[user]["bank"]
    leader_board[total_amount]=name
    total.append(total_amount)

  total=sorted(total, reverse=True)
  em = discord.Embed(title=f"Top {x} richest people in Tango based on money in bank and wallet")
  index = 1
  for amt in total:
    id_=leader_board[amt]
    member=await bot.fetch_user(id_)
    name=member.name
    em.add_field(name=f"{index}. {name} ",value=f"{amt}", inline=False)
    if index==x:
      break
    else:
      index+=1
  await ctx.send(embed=em)

@bot.command()
@commands.cooldown(1, 120000, commands.BucketType.user)
async def spinthewheel(ctx):
  users=await get_bank_data()
  user=ctx.author
  emb=discord.Embed(title="Spin the Wheel Rewards", description="Win/lose a random amount of money ranging from -5,500,000 to 5,100,000", color=discord.Colour.from_rgb(255, 174, 66))

  await ctx.send(embed = emb)
  randommoneywin=random.randrange(-5500000, 5100000)
  users[str(user.id)]["xp"]+=1
  time.sleep(1)
  if randommoneywin >0:
    e=discord.Embed(title="Congratulations for winning money", description=f"You won {randommoneywin} tangies", color=discord.Colour.from_rgb(255, 174, 66))
    e.set_footer(text="😏😏")
    await ctx.send(embed=e)
    await update_bank(user, randommoneywin)
  else:
    em=discord.Embed(title="Congratulations for losing money", description=f"You won {randommoneywin} tangies", color=discord.Colour.from_rgb(255, 174, 66))
    await ctx.send(embed=em)
    em.set_footer(text="😏😏")
    await update_bank(user, -1*randommoneywin)
    
@spinthewheel.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"No spam pls",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def space(ctx):
  user=ctx.author
  users=await get_bank_data()
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  em = discord.Embed(title="Space Adventure on demand!", description="Its a fun adventure command where you can win 1000-15000 tangies every 5min", color=discord.Colour.from_rgb(r, g, b))
  await ctx.send(embed=em)
  moneyucenwin = random.randrange(500, 15000)
  em1 = discord.Embed(title="Adventure in progress!", description=f"Bhai aapne {moneyucenwin} paisa jeeta hai.", color=discord.Colour.from_rgb(r, g, b))
  await ctx.send(embed=em1)
  users[str(user.id)]["wallet"]+=moneyucenwin
  await ctx.send("**congratulatenons**")

@space.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"No spam pls",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def ttt(ctx, p1:discord.Member, p2:discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if p1 == 'Tango':
      await ctx.send('IMMA NOT IN THE MOOD')
      return
    elif p2 == 'Tango':
      await ctx.send('IMMA NOT IN THE MOOD')
      return
    else:
      pass
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + f" {ctx.author}"+"wins!")
                    user = ctx.author
                    users = await get_bank_data()
                    await open_account(ctx.author)
                    users[str(user.id)]["wins"]+=1
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the t!ttt command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ttt.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players.")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


@bot.command()
@commands.cooldown(1, 75, commands.BucketType.user)
async def trivia(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users=await get_bank_data()  
    await update_bank(user, 1*10)

    _list = [
    'Who is the owner of microsoft?', 
    'When did Kohli step down as indian test captain?',
    'Whats the capital of Kiribati?',
    'Which team does lord play for',
    'What is my name?',
    'What is the capital of Manipur?',
    'Who is owner of dbc?',
    'Who is sun microsystem"s co founder', 
    'Who made da rickroll(ez one)?',
    'When was Tango released(important day for dbc)',
    'How many people were in the team that made Tango?',
    'Which type of plastic have cross linked chains?',
    'Which type of sound has frequency more than 20000hz?',
    'Which type of sound has frequency less than 20000hz?',
    'IS there a YT channel for tango?',
    'In which year was discord, the famous chatting application made?']

    list1 = random.choice(_list)
    print(list1)

    def answer():
        answer = "0"
        if _list[0] == list1:
            answer = "bill gates"
        elif _list[1] == list1: 
            answer = "january 15th"
        elif _list[2] == list1: 
            answer = "tarawa"
        elif _list[3] == list1: 
            answer = "delhi capitals"
        elif _list[4] == list1:
            answer="Tango"
        elif _list[5] == list1:
          answer="Imphal"
        elif _list[6] == list1:
            answer="scemer#5643"
        elif _list[7] == list1:
            answer="vinod khosla"
        elif _list[8] == list1:
            answer="rick astley"
        elif _list[9] == list1:
            answer="27th april 2022"
        elif _list[10] == list1:
            answer="3 people"
        elif _list[11] == list1:
            answer="thermosetting plastic"
        elif _list[12] == list1:
            answer="ultrasonic sound"
        elif _list[13] == list1:
            answer="infrasonic sound"
        elif _list[14] == list1:
            answer="no"
        elif _list[15] == list1:
            answer="2015"
        return answer

    await ctx.send("What is the answer to this question?")
    await asyncio.sleep(1)
    await ctx.send(list1)
    def check(m): return m.author == ctx.author and m.channel == ctx.channel

    msg = await bot.wait_for('message', check=check, timeout=None)

    if msg.content == answer():
        await ctx.send("good")
        await ctx.send("WAH, YOU ARE AN OP GENIUS CONGRATS.")
    else:
        await ctx.send("no")   
        await ctx.send("NOOB, THE ANSWER ISNT WHAT YOU TOLD NOOOOOB.")
    await ctx.send("You got 10 tangies for playing trivia")
    await ctx.send('https://tenor.com/view/kekw-kek-bttv-twitch-emote-gif-15123134')
    await ctx.send("JOKIN U DINT GET ANY MONI.")
    await update_bank(ctx.author, 10*2)

@trivia.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"No overtriviacfication pls",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def rockpaperscissors(ctx):
    user = ctx.author
    users=await get_bank_data()
    await open_account(ctx.author)
    usrscore=0
    botscore=0
    for i in range(15):
      
      rpsGame = ['rock', 'paper', 'scissors']
      await ctx.send(f"Rock, paper, or scissors? Choose wisely...")
  
      def check(msg):
          return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame
  
      user_choice = (await bot.wait_for('message', check=check)).content
  
      comp_choice = random.choice(rpsGame)
      if user_choice == 'rock':
          if comp_choice == 'rock':
              await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
          elif comp_choice == 'paper':
              await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
              botscore+=1
          elif comp_choice == 'scissors':
              await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")
              usrscore+=1
  
      elif user_choice == 'paper':
          if comp_choice == 'rock':
              await ctx.send(f' More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
              botscore+=1
          elif comp_choice == 'paper':
              await ctx.send(f'Oh, . We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
          elif comp_choice == 'scissors':
              await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")
              usrscore+=1
  
      elif user_choice == 'scissors':
          if comp_choice == 'rock':
              await ctx.send(f'HAHA!! I JUST DEFEATED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
              botscore+=1
          elif comp_choice == 'paper':
              await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
              usrscore+=1
          elif comp_choice == 'scissors':
              await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")
    if usrscore > botscore:
      emb=discord.Embed(title=f"THE USER NAMED {ctx.author} won", description="user won and bot lost yessssssssss", color=145)
      await ctx.send(embed=emb)
      await ctx.send(f"BOT SCORE: {botscore}")
      await ctx.send(f"USER SCORE : {usrscore}")
      await update_bank(ctx.author, 1*1000)

    elif botscore>usrscore:
      emb=discord.Embed(title=f"THE USER NAMED {ctx.author} lost", description="What a dumbo", color=145)
      await ctx.send(embed=emb)
      await ctx.send(f"BOT SCORE: {botscore}")
      await ctx.send(f"USER SCORE : {usrscore}")

    else:
      emb=discord.Embed(title=f"A tie with {ctx.author}", description="OH NO, A TIE!!!!!!!!!!!!!!!!", color=145)
      await ctx.send(embed=emb)
      await ctx.send(f"BOT SCORE: {botscore}")
      await ctx.send(f"USER SCORE : {usrscore}")
      await update_bank(ctx.author, 1*500)

@rockpaperscissors.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"YOU GOT ROCKPAPERSCISSORED",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
async def crx(ctx):
  coolpercent = random.randrange(101)
  em = discord.Embed(title=f"cool index for {ctx.author}", description=f"{ctx.author.mention} coolness: {coolpercent}%", color=discord.Color.random())
  await ctx.send(embed=em)

@bot.command()
async def crxu(ctx, member:discord.Member):
  coolpercent = random.randrange(101)
  em = discord.Embed(title=f"cool index for {member}", description=f"{member.mention} coolness: {coolpercent}%", color=discord.Color.random())
  await ctx.send(embed=em)

@bot.command()
async def telefonkhomba(ctx):
  await ctx.send('https://i.ytimg.com/vi/LuZV9kkzscg/mqdefault.jpg')

@bot.command()
async def passedaway(ctx):
  await ctx.send('https://www.facebook.com/Corporatebytes/videos/worst-job-interview/775663769476168/')

@bot.command()
async def whatsmyname(ctx):
  await ctx.send('yOUR NEME IS BUFELO')


@bot.command()
async def search(ctx,*,matter):
  try:
    result = wikipedia.summary(matter, sentences = 20)
    await ctx.send(result)
  except Exception as e:
    await ctx.send("Pls specify whatever you want to search properly")


@bot.command()
async def rr(ctx, member:discord.Member):
  rikrel = 'https://www.youtube.com/watch?v=xvFZjo5PgG0'
  await member.send("a surprise")
  await member.send(rikrel)
  await ctx.send("SARPRIZ SENT")
  await ctx.send('😈😈😈😈😈😈😈😈😈')

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
  await open_account(ctx.author)
  user=ctx.author
  users=await get_bank_data()
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  em = discord.Embed(title="You earn a sum of 10k tangies using this command", description="WAH, YOU EARNED 10K coins as daily", color = discord.Colour.from_rgb(r, g, b))
  await ctx.send(embed=em)

  await update_bank(ctx.author, 1*10000)
  
@daily.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"YOU GOT SORED",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1, 2592000, commands.BucketType.user)
async def monthly(ctx):
  await open_account(ctx.author)
  user=ctx.author
  users=await get_bank_data()
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  em = discord.Embed(title="You earn a sum of 40k tangies using this command", description="WAH, YOU EARNED 40K coins as daily", color = discord.Colour.from_rgb(r, g, b))
  await ctx.send(embed=em)


  await update_bank(ctx.author, 4*10000)
  
@daily.error
async def command_name_error(ctx, error):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    if isinstance(error, commands.CommandOnCooldown):
        embedVar = discord.Embed(
            title=f"YOU GOT MONTHLIED",
            description=f"Try again in {error.retry_after:.2f}s.",
            colour=discord.Colour.from_rgb(r, g, b))
        await ctx.send(embed=embedVar)
@bot.command()
async def yt(ctx):
  ytchannellink = "https://www.youtube.com/channel/UChzhY6L_TfY6wvmyg_yRf2Q"
  yttrailer="https://www.youtube.com/watch?v=_SuTOCuhJkU"
  em = discord.Embed(title="Tango on YOUTUBE")
  em.add_field(name="The Youtube channel", value=ytchannellink)
  em.add_field(name="The Youtube Trailer", value=yttrailer)
  await ctx.send(embed=em)

#the main bot settings! for economt only(note it) lelolol
async def open_account(user):
  with open("mainbank.json", "r") as f:
    users = json.load(f)
  
  if str(user.id) in users:
    return False 
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 0
    users[str(user.id)]["bank"] = 0
    users[str(user.id)]["xp"] = 0
    users[str(user.id)]["bag"] = []
    users[str(user.id)] ["Profession"] = 'None'
    users[str(user.id)]["salary"] = 0
    users[str(user.id)]["investment"] = 0
    users[str(user.id)]["timesinvested"] = 0
    users[str(user.id)]["originalinvestment"] = 0
    users[str(user.id)]["investedin"]= ' '
  
  with open("mainbank.json", "w") as f:
    json.dump(users,f)
  return True

keep_alive()

bot.run(TOKEN)
#last line
#+extraz
#Sed life
#Tango End
