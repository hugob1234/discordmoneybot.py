import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())
import requests

@bot.event
async def on_ready():
  print("Bot is now online!")

@bot.command()
async def exchange(ctx):
  embed = discord.Embed(title="Money exchange", description="Options:", color=discord.Color.green())
  embed.add_field(name="!pounds", value="Converts foreign currencies into British pounds (!pounds $400) for example", inline=False)
  embed.add_field(name="!euro", value="  Converts foreign currencies into euros for example (!euro $400)", inline=False)
  embed.add_field(name="!dollar", value="Converts foreign currencies into US dollars for example (!dollar £400) ", inline=False)
  embed.add_field(name="!moneylogo", value="Shows profile pic of bot", inline=False)
  embed.set_footer(text="Made by Hugo B")
  await ctx.send(embed=embed)


@bot.command()
async def moneylogo(ctx):
  with open('money.jpg', 'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def pounds(ctx, amount):
  if amount[0] == "€":
    embed = discord.Embed(title="CURRENCY EXCHANGE", description="Euro to pounds", color=discord.Color.green())
    num1 = ''.join(amount[1:])
    num = float(num1)
    num = num * 0.88
    embed.add_field(name="Result:", value=f"€{num1} was converted into £{round(num, 2)}", inline=False)
    embed.set_footer(text="MONEY EXCHANGER @2024")
    await ctx.send(embed=embed)
  elif amount[0] == "$":
    embed = discord.Embed(title="CURRENCY EXCHANGE", description="US dollars to pounds", color=discord.Color.green())
    num1 = ''.join(amount[1:])
    num = float(num1)
    num = num * 0.95
    embed.add_field(name="Result:", value=f"${num1} was converted into £{round(num, 2)}", inline=False)
    embed.set_footer(text="MONEY EXCHANGER @2024")
    await ctx.send(embed=embed)
  elif amount[0] == "£":
    await ctx.send("This command is used to exchange foreign currencies to British pounds")
  else:
    await ctx.send("Currency isnt supported")
    
@bot.command()
async def euro(ctx, amount):
  if amount[0] == "£" or amount[0]== "p":
    embed = discord.Embed(title="CURRENCY EXCHANGE", description="Pounds to euros", color=discord.Color.green())
    num1 = ''.join(amount[1:])
    num = float(num1)
    num = num * 1.22
    embed.add_field(name="Result:", value=f"£{num1} was converted into €{round(num, 2)}", inline=False)
    embed.set_footer(text="MONEY EXCHANGER @2024")
    await ctx.send(embed=embed)
  elif amount[0] == "$" or amount[0] == "d":
    embed = discord.Embed(title="CURRENCY EXCHANGE", description="US dollars to euros", color=discord.Color.green())
    num1 = ''.join(amount[1:])
    num = float(num1)
    num = num * 1.12
    embed.add_field(name="Result:", value=f"${num1} was converted into €{(round(num, 2))}", inline=False)
    embed.set_footer(text="MONEY EXCHANGER @2024")
    await ctx.send(embed=embed)
  elif amount[0] == "€":
    await ctx.send("This command is used to exchange foreign currencies to Euros")
  else:
    await ctx.send("Currency isnt supported")

@bot.command()
async def dollar(ctx, amount):
  if amount[0] == "£" or amount[0]== "p":
    embed = discord.Embed(title="CURRENCY EXCHANGE", description="Pounds to dollars", color=discord.Color.green())
    num1 = ''.join(amount[1:])
    num = float(num1)
    num = num * 1.22
    embed.add_field(name="Result:", value=f"£{num1} was converted into ${round(num, 2)}", inline=False)
    embed.set_footer(text="MONEY EXCHANGER @2024")
    await ctx.send(embed=embed)
  elif amount[0] == "€" or amount[0] == "e":
    embed = discord.Embed(title="CURRENCY EXCHANGE", description="Euros to dollars", color=discord.Color.green())
    num1 = ''.join(amount[1:])
    num = float(num1)
    num = num * 1.08
    embed.add_field(name="Result:", value=f"€{num1} was converted into ${(round(num, 2))}", inline=False)
    embed.set_footer(text="MONEY EXCHANGER @2024")
    await ctx.send(embed=embed)
  elif amount[0] == "€":
    await ctx.send("This command is used to exchange foreign currencies to US dollars")
  else:
    await ctx.send("Currency isnt supported")



bot.run("MTIxNDIxMjk3NTk5MzQyMTg2NA.GugLAR.IQ6MaretPYUjgXop93h5kKnDvs9MF3-DUWoGnc")
