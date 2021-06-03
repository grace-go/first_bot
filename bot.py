from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name="idea")
async def idea(ctx):
    await ctx.send("Ideas are hard")

with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)