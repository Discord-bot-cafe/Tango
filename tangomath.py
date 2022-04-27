import discord
import os
import re
from discord.ext import commands
from keep_alive import keep_alive

embededMSG = discord.Embed()
client = discord.Client(activity=discord.Game(name="+help for help"))
@client.event

async def on_ready():
  print('Logged in as {0.user}'.format(client))
#---------------.--------------------

@client.event
@commands.cooldown(1, 10, commands.BucketType.user)
async def on_message(message):
  if message.author == client.user:
    return
  msgContent = message.content
  msgSend = message.channel.send


  if msgContent.startswith('+add'): 
    numbers = msgContent.split('+add ',1)[1]#Here the '+add' is seperated from the main content
    numbers0 = re.split('\s', numbers)#This is me splitting the numbers without the space in between    
    addend1 = numbers0[0] 
    addend2 = numbers0[1]
    sum = int(addend1)+int(addend2)
    desc1 = str(numbers0[0])+ '+'+ str(numbers0[1])+ '='+ str(sum)
    await message.channel.send(embed=discord.Embed(title="Your Answer Is:", description=desc1, color=7143423
    ))
  if msgContent.startswith('+help'): 
    Embed = discord.Embed(title="Here are a few tips:", description="Look below not here(Lol)", color=6094592
)
    Embed.add_field(name="To Add 2 numbers:", value="+add num1 num2", inline=False)
    Embed.add_field(name="Multiplication", value="+x num1 num2", inline=False)
    Embed.add_field(name="Subtration", value="+- num1 num2", inline=False)
    Embed.add_field(name="Squaring", value="+2 num1", inline=False)
    Embed.add_field(name="Powering", value="+** num1 num2", inline=False)
    Embed.add_field(name="Square roots", value="+sqrt num1", inline=False)
    Embed.add_field(name="To add invite link", value="+invite", inline=False)
    Embed.add_field(name="Bot owner", value="+owner", inline=False)
    await message.channel.send(embed=Embed)

  if msgContent.startswith('+x'): 
    numbers = msgContent.split('+x ',1)[1]#Here the '+add' is seperated from the main content
    numbers1 = re.split('\s', numbers)#This is me splitting the numbers without the space in between
    print(numbers1)
    factor2 = int(float(numbers1[0])) 
    factor1 = int(float(numbers1[1]))
    print(factor1)
    multiply = int(float(factor1))*int(float(factor2))
    desc1 = str(numbers1[0])+ '*'+ str(numbers1[1])+ '='+ str(multiply)
    await message.channel.send(embed=discord.Embed(title="Your Answer Is:", description=desc1, color=16711680
    ))
  if msgContent.startswith('+-'): 
    numbers = msgContent.split('+- ',1)[1]#Here the '+add' is seperated from the main content
    numbers1 = re.split('\s', numbers)#This is me splitting the numbers without the space in between
    print(numbers1)
    factor2 = int(float(numbers1[0])) 
    factor1 = int(float(numbers1[1]))
    print(factor1)
    sub = int(float(factor1))-int(float(factor2))
    desc1 = str(numbers1[0])+ '-'+ str(numbers1[1])+ '='+ str(sub)
    await message.channel.send(embed=discord.Embed(title="Your Answer Is:", description=desc1, color=16711680
    ))

  if msgContent.startswith('+/'): 
    numbers = msgContent.split('+/ ',1)[1]#Here the '+add' is seperated from the main content
    numbers1 = re.split('\s', numbers)#This is me splitting the numbers without the space in between
    print(numbers1)
    factor2 = int(float(numbers1[0])) 
    factor1 = int(float(numbers1[1]))
    print(factor1)
    div = int(float(factor1)) // int(float(factor2))
    desc1 = str(numbers1[0])+ '/'+ str(numbers1[1])+ '='+ str(div)
    await message.channel.send(embed=discord.Embed(title="Your Answer Is:", description=desc1, color=16711680
    ))

  if msgContent.startswith('+2'): 
    numbers = msgContent.split('+2 ',1)[1]#Here the '+add' is seperated from the main content
    numbers1 = re.split('\s', numbers)#This is me splitting the numbers without the space in between
    print(numbers1)
    factor1 = int(float(numbers1[0])) 
    print(factor1)
    div = int(float(factor1))*int(float(factor1))
    desc1 = str(numbers1[0])+ ' squared'+ '='+ str(div)
    await message.channel.send(embed=discord.Embed(title="Your Answer Is:", description=desc1, color=16711680
    ))

  if msgContent.startswith('+**'): 
    numbers = msgContent.split('+** ',1)[1]#Here the '+add' is seperated from the main content
    numbers1 = re.split('\s', numbers)#This is me splitting the numbers without the space in between
    print(numbers1)
    factor2 = int(float(numbers1[0])) 
    factor1 = int(float(numbers1[1]))
    print(factor1)
    div = int(float(factor2)) ** int(float(factor1))
    desc1 = str(numbers1[0])+ ' to the power of '+ str(numbers1[1])+ ' is '+ str(div)
    await message.channel.send(embed=discord.Embed(title="Your Answer Is:", description=desc1, color=16711680
    ))

  if msgContent.startswith('+sqrt'): 
    numbers = msgContent.split('+sqrt ',1)[1]#Here the '+add' is seperated from the main content
    numbers1 = re.split('\s', numbers)#This is me splitting the numbers without the space in between
    print(numbers1)
    factor1 = int(float(numbers1[0])) 
    print(factor1)
    sqrt = float(factor1)**0.5
    sqrtint = float(sqrt)
    desc1 = str(numbers1[0])+ "'s square root"+ '='+ str(sqrtint)
    await message.channel.send(embed=discord.Embed(title="Your Answer Is:", description=desc1, color=65280
    ))
  if msgContent.startswith('+invite'):
    await message.channel.send(embed=discord.Embed(title="Invite link for bot", description='https://discord.com/api/oauth2/authorize?client_id=951790853557477376&permissions=534723950656&scope=bot', color=65281))
  if msgContent.startswith('+owner'):
    await message.channel.send(embed=discord.Embed(title="Owner of bot", description="Ameya Joshi", color=65280))

  if msgContent.startswith('+/'):
    num = msgContent.split('+/',1)[1]
    num1,num2 = num.split()
    numm1 = int(num1)
    numm2 = int(num2)
    ans = numm1/numm2
    await message.channel.send(ans)
#--------------------------------------------------

keep_alive()

client.run(os.getenv('TOKEN'))  
