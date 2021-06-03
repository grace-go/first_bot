from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name="description")
async def description(ctx):
    await ctx.send("If you want to get a recommendation randomly, type \"!random\". \n ")

@bot.command(name="idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")

# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)