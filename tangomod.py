import discord
from discord.ext import commands
import random
import os
import json
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='tm!', activity=discord.Game(name="Tango mod bot"), help_command=None)

badwords =['bdword1','bdword2']

@bot.event
async def on_ready():
  print('mod is here to rescuse the mods')
  print("lelmo")

@bot.event
async def on_message(msg):  
  for word in badwords:
    if word in msg.content:
      r = 136
      g = 8
      b=8
      await msg.delete()
      em = discord.Embed(title = f'{msg.author} used a bad word')
      await msg.channel.send(embed = em)
      em = discord.Embed(title="DO NOT USE SUCH WORDS", color = discord.Colour.from_rgb(r, g, b))
      await msg.author.send(embed=em)
    
        
      
  await bot.process_commands(msg)
  
  


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member, *, reason):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  await member.ban(reason=reason)
  banembed = discord.Embed(title=f"{member.name}#{member.discriminator} has been banned by {ctx.message.author}", color = discord.Colour.from_rgb(r, g, b))
  banembed.set_footer(text=f'Reason:{reason}')
  await ctx.send(embed=banembed)
  await member.send(embed = discord.Embed(title=f"{member.name}{member.discriminator} has been banned by {ctx.message.author}"))

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  banned_users = await ctx.guild.bans() 
  member_name, member_discriminator = member.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user) 
      em =discord.Embed(title="Unban successful",
                       desciption = f"{member.name} has been succesfully unbanned", color = discord.Colour.from_rgb(r, g, b))
      em.set_footer(text= f"action done by {ctx.author}")
      await ctx.send(embed=em)
      return

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member, * , reason):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    await member.kick(reason = reason)
    kickembed = discord.Embed(title=f"{member.name}#{member.discriminator}has been kicked. By {ctx.message.author}")
    kickembed.set_footer(text=f'Reason:{reason}', color=discord.Colour.from_rgb(r, g, b))
    await ctx.send(embed=kickembed)
    em = discord.Embed(title=f"{member.name}{member.discriminator} has been banned by {ctx.message.author}", color=discord.Colour.from_rgb(r, g, b))
    await member.send(embed = em)

@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx,member:discord.Member):
  muted_role = ctx.guild.get_role(954007726046998598)

  await member.add_roles(muted_role)

  await ctx.send(f"muted {member} successfully.")

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx,member:discord.Member):
  muted_role = ctx.guild.get_role(954007726046998598)

  await member.remove_roles(muted_role)

  await ctx.send(f"unmuted {member} lol,")                   

@bot.command()
async def invite(ctx):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  em=discord.Embed(title="Invite tango mod to save your server!", description="https://discord.com/api/oauth2/authorize?client_id=953998729659183104&permissions=8&scope=bot", color= discord.Colour.from_rgb(r, g, b))
  em.set_footer(text="lemon")
  await ctx.send(embed=em)

@bot.command()
async def help(ctx):
  r = random.randrange(0, 255)
  g = random.randrange(0, 255)
  b = random.randrange(0, 255)
  em=discord.Embed(title='Bot commands', description="1)`tm!ban` **tm!ban @user reason**: this is used to ban people if you want to in the server\n2)`tm!unban `**tm!unban @user**: used to unban naughty users who begged for it.\n3)`tm!kick`**tm!kick @user reason**:to kick users(tempban)\n4)`tm!mute`**tm!mute @user**: to mute users indefinitely\n5)`tm!unmute `**tm!unmute @user** to unmute indefinitely muted users\n6)`tm!invite `**tm!invite**: invite link for bot\n7)`tm!help` **tm!help**: shows this", color=discord.Colour.from_rgb(r, g, b))
  em.set_footer(text="LOOK ABOVE NOT HERE, LOL ")
  await ctx.send(embed=em)

keep_alive()
bot.run(os.getenv('TOKEN'))
