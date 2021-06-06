from discord import channel
import discord
from discord.ext import commands
import random

# detail description
menu_description = ['bogus']
recipe = {}
recipe['Carbonara'] = 'STEP 1\nPut a large saucepan of water on to boil.'
recipe['Carbonara'] += '\nSTEP 2\nFinely chop the 100g pancetta, having first removed any rind. Finely grate 50g pecorino cheese and 50g parmesan and mix them together.'
recipe['Carbonara'] += '\nSTEP 3\nBeat the 3 large eggs in a medium bowl and season with a little freshly grated black pepper. Set everything aside.'
recipe['Carbonara'] += '\nSTEP 4\nAdd 1 tsp salt to the boiling water, add 350g spaghetti and when the water comes back to the boil, cook at a constant simmer, covered, for 10 minutes or until al dente (just cooked).'
recipe['Carbonara'] += '\nSTEP 5\nSquash 2 peeled plump garlic cloves with the blade of a knife, just to bruise it.'
recipe['Carbonara'] += '\nSTEP 6\nWhile the spaghetti is cooking, fry the pancetta with the garlic. Drop 50g unsalted butter into a large frying pan or wok and, as soon as the butter has melted, tip in the pancetta and garlic.'
recipe['Carbonara'] += '\nSTEP 7\nLeave to cook on a medium heat for about 5 minutes, stirring often, until the pancetta is golden and crisp. The garlic has now imparted its flavour, so take it out with a slotted spoon and discard.'
recipe['Carbonara'] += '\nSTEP 8\nKeep the heat under the pancetta on low. When the pasta is ready, lift it from the water with a pasta fork or tongs and put it in the frying pan with the pancetta. Don’t worry if a little water drops in the pan as well (you want this to happen) and don’t throw the pasta water away yet.'
recipe['Carbonara'] += '\nSTEP 9\nMix most of the cheese in with the eggs, keeping a small handful back for sprinkling over later.'
recipe['Carbonara'] += '\nSTEP 10\nTake the pan of spaghetti and pancetta off the heat. Now quickly pour in the eggs and cheese. Using the tongs or a long fork, lift up the spaghetti so it mixes easily with the egg mixture, which thickens but doesn’t scramble, and everything is coated.'
recipe['Carbonara'] += '\nSTEP 11\nAdd extra pasta cooking water to keep it saucy (several tablespoons should do it). You don’t want it wet, just moist. Season with a little salt, if needed.'
recipe['Carbonara'] += '\nSTEP 12\nUse a long-pronged fork to twist the pasta on to the serving plate or bowl. Serve immediately with a little sprinkling of the remaining cheese and a grating of black pepper. If the dish does get a little dry before serving, splash in some more hot pasta water and the glossy sauciness will be revived.'

bot = commands.Bot(command_prefix='!')

@bot.command(name="description")
async def description(ctx):
    await ctx.send("If you want to get a recommendation randomly, type \"!random\". \n ")

@bot.command(name="pick")
async def pick(ctx):
    global menu_description
    await ctx.send("It's hard to choose which menu you are going to cook!")
    food_list = ['Carbonara', 'Jumbalaya', 'Chicken Noodle Soup', 'Pho', 'Butter Chicken', 'Philly Cheese Steak', 'Frittata']
    food = random.choice(food_list)
    await ctx.send("How about...")
    await ctx.send("a " + food + "?")
    menu_description.insert(0, food)
    await ctx.send("If you want to read a recipe of it, please type \"!yes\"")
    

@bot.command(name="yes")
async def yes(ctx):
    global recipe
    global menu_description
    await ctx.send(recipe.get(menu_description[0], 'Please type \"!pick\" first and check out the randomly picked menu!'))
    await ctx.send("and here is the photo of the menu!")
    # await ctx.send(file=discord.File('pasta.jpg'))


@bot.command(name="Carbonara")
async def carbonara(ctx):
    await ctx.send(recipe['Carbonara'])

# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)