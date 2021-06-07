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
recipe['Carbonara2'] = '\nSTEP 7\nLeave to cook on a medium heat for about 5 minutes, stirring often, until the pancetta is golden and crisp. The garlic has now imparted its flavour, so take it out with a slotted spoon and discard.'
recipe['Carbonara2'] += '\nSTEP 8\nKeep the heat under the pancetta on low. When the pasta is ready, lift it from the water with a pasta fork or tongs and put it in the frying pan with the pancetta. Don’t worry if a little water drops in the pan as well (you want this to happen) and don’t throw the pasta water away yet.'
recipe['Carbonara2'] += '\nSTEP 9\nMix most of the cheese in with the eggs, keeping a small handful back for sprinkling over later.'
recipe['Carbonara2'] += '\nSTEP 10\nTake the pan of spaghetti and pancetta off the heat. Now quickly pour in the eggs and cheese. Using the tongs or a long fork, lift up the spaghetti so it mixes easily with the egg mixture, which thickens but doesn’t scramble, and everything is coated.'
recipe['Carbonara2'] += '\nSTEP 11\nAdd extra pasta cooking water to keep it saucy (several tablespoons should do it). You don’t want it wet, just moist. Season with a little salt, if needed.'
recipe['Carbonara2'] += '\nSTEP 12\nUse a long-pronged fork to twist the pasta on to the serving plate or bowl. Serve immediately with a little sprinkling of the remaining cheese and a grating of black pepper. If the dish does get a little dry before serving, splash in some more hot pasta water and the glossy sauciness will be revived.'
recipe['Carbonara2'] += '\nfrom https://www.bbcgoodfood.com/recipes/ultimate-spaghetti-carbonara-recipe'

recipe['Jumbalaya'] = 'STEP 1\nSauté the chicken and sausage.  Sauté until the chicken is cooked through and the sausage is lightly browned.  Then transfer to a clean plate and set aside.'
recipe['Jumbalaya'] += '\nSTEP 2\nSauté the veggies.  Sauté the onion, bell pepper, celery, jalapeño and garlic until soft.'
recipe['Jumbalaya'] += '\nSTEP 3\nAdd rice, liquids and seasonings.  Add in the uncooked rice, chicken stock, crushed tomatoes, Cajun/Creole seasoning, thyme, cayenne and bay leaf.  Give everything a good stir.'
recipe['Jumbalaya'] += '\nSTEP 4\nCover and cook.  Then cook for 25-30 minutes, being sure to stir the mixture every 5 minutes or so (to prevent burning) until the rice is nearly tender.'
recipe['Jumbalaya2'] = '\nSTEP 5\nAdd the okra and shrimp.  And cook for a final 5 minutes or so, until the shrimp is pink and opaque.  Add the chicken and sausage back in.'
recipe['Jumbalaya2'] += '\nSTEP 6\nTaste and season.  Season the jambalaya with salt and pepper (and extra Cajun/Creole seasoning, if needed) to taste.'
recipe['Jumbalaya2'] += '\nSTEP 7\nServe warm.  Garnished with your desired toppings!'
recipe['Jumbalaya2'] += '\nfrom https://gimmesomeoven.com/jambalaya-recipe'

recipe['Frittata'] = 'Ingredients: 12 eggs, 3 tablespoons full-fat dairy (heavy cream, half-and-half, whole milk, sour cream, crème fraîche or yogurt), ½ teaspoon salt, 1 cup (4 ounces) grated or crumbled cheese, 3 to 5 cups chopped vegetables or greens of choice (or up to 3 cups leftover cooked vegetables or greens), 1 tablespoon olive oil, Garnish: Chopped or torn fresh, leafy herbs (basil, parsley, cilantro, or dill)'
recipe['Frittata'] += '\nSTEP 1\nPreheat the oven to 425 degrees Fahrenheit for the traditional stovetop method, or 350 degrees for the baked methods (casserole or mini/muffins).'
recipe['Frittata'] += '\nSTEP 2\nCrack the eggs into a medium mixing bowl. Add your dairy of choice and the salt. Whisk just until the egg yolks and whites are blended. Whisk in all or half of the cheese (you can reserve the other half for topping the frittata before baking, if desired). Set the mixture aside.'
recipe['Frittata'] += '\nSTEP 3\nIn a 12-inch cast iron skillet (or any other large skillet that’s oven safe), warm the olive oil over medium heat until shimmering. Add the vegetables, starting with chopped onions or other dense vegetables. Cook for a few minutes, stirring occasionally, then add any softer vegetables such as zucchini. Cook until those vegetables are tender, then add any garlic or greens, and cook until fragrant or wilted. Season with salt, to taste.'
recipe['Frittata'] += '\nSTEP 4\nTraditional stovetop option: Whisk the eggs once more and pour the mixture over the vegetables. Stir with a spatula briefly to combine and distribute the mixture evenly across the pan. If you reserved any cheese, sprinkle it on top of the frittata now.'
recipe['Frittata'] += '\nSTEP 5\nOnce the outside edge of the frittata turns lighter in color (about 30 seconds to 1 minute), carefully transfer the frittata to the oven. Bake for 7 to 14 minutes (keep an eye on it), until the eggs are puffed and appear cooked, and the center of the frittata jiggles just a bit when you give it a gentle shimmy. Remove the frittata from the oven and place it on a cooling rack to cool. Garnish with herbs, slice with a sharp knife, and serve.'
recipe['Frittata2'] = '\nSTEP 6\nBaked casserole option: Let the cooked vegetables cool for a few minutes. In the meantime, grease a 9 by 13-inch pan with butter, which works better than cooking spray. Stir the lightly cooled veggies into the egg mixture, then pour it all into the pan. If you reserved any cheese, sprinkle it on top of the frittata now.'
recipe['Frittata2'] += '\nSTEP 7\nBake for 20 to 25 minutes (keep an eye on it), until the eggs are puffed and appear cooked, and the center of the frittata jiggles just a bit when you give it a gentle shimmy. Remove the frittata from the oven and place it on a cooling rack to cool. Garnish with herbs, slice with a sharp knife, and serve.'
recipe['Frittata2'] += '\nSTEP 8\nBaked mini frittata option: Let the cooked vegetables cool for a few minutes, then stir them into the egg mixture. Grease 18 muffin cups (I used two muffin pans for this), then fill the cups evenly with a scant ⅓ cup of the mixture. If you reserved any cheese, sprinkle it on top of the frittatas now.'
recipe['Frittata2'] += '\nSTEP 9\nBake for 13 to 17 minutes, until the eggs are puffed and appear cooked, and the center of the frittatas jiggle just a bit when you give the pan a gentle shimmy (this happens quickly so keep an eye on them; my pan with only 6 muffins finished sooner). Remove the pans from the oven and place them on a cooling rack to cool. Garnish with herbs, and serve.'
recipe['Frittata2'] += '\n from https://cookieandkate.com/best-frittata-recipe/'

recipe['Creamycodchowderstew'] = 'Ingredients: 200g floury potatoes(cubed), 200g parsnips(cubed), 140g skinless cod fillet, 140g skinless undyed smoked haddock fillets, 500ml semi-skimmed milk, ¼ small pack parsley , leaves finely chopped, stalks reserved, 6 spring onions , whites and greens separated, both finely chopped, 2 tbsp plain flour, zest and juice 1 lemon, 2 tbsp chopped parsley, and crusty wholemeal bread , to serve'
recipe['Creamycodchowderstew'] += '\nSTEP 1\nBring a saucepan of salted water to the boil, add the potato and parsnips, and boil until almost tender – about 4 mins. Drain well.'
recipe['Creamycodchowderstew'] += '\nSTEP 2\nMeanwhile, put the fish in a pan where they will fit snugly but not on top of each other. Cover with the milk, poke in the parsley stalks and bring the milk to a gentle simmer. Cover the pan, turn off the heat and leave to sit in the milk for 5 mins. Lift the fish out and break into large chunks. Discard the parsley stalks but keep the milk.'
recipe['Creamycodchowderstew2'] = '\nSTEP 3\nPut the spring onion whites, milk and flour in a saucepan together. Bring to a simmer, whisking continuously, until the sauce has thickened and become smooth. Turn the heat down, add the drained potatoes and parsnips, the lemon zest and half the juice, and cook gently for 5 mins, stirring occasionally. Stir in the spring onion greens, fish and parsley, and taste for seasoning – it will need plenty of pepper, some salt and maybe more lemon juice from the leftover half. Divide between two shallow bowls, serve with chunks of crusty bread and enjoy.'
recipe['Creamycodchowderstew2'] += '\n from https://www.bbcgoodfood.com/recipes/creamy-cod-chowder-stew'


bot = commands.Bot(command_prefix='!')

@bot.command(name="description")
async def description(ctx):
    """description: gives a brief intro about this chatbot"""
    
    await ctx.send("Hello, this is a menu-picking chatbot!")
    await ctx.send("If you want to get a recommendation randomly, type \"!pick\".")
    await ctx.send("If you want to get a recommendation by a budget, type \"!budget your_budget\".")
    await ctx.send("If you want to know the recipe of a specific menu, type \"!recipe menu_name\"")
    await ctx.send("When you type a menu_name, please type it without a whitespace!")

@bot.command(name="delivery")
async def delivery(ctx):
    """randomly chooses a delivery food"""

    deliver_list = ['Burger', 'Pizza', 'Pasta', 'Taco', 'Doughnuts', 'Pancake']
    await ctx.send("If you are tired and can't cook, food delivery is also a good choice!")
    await ctx.send(f'How about a {random.choice(deliver_list)}?')

@bot.command(name="pick")
async def pick(ctx):
    """randomly recommends a menu to cook"""

    global menu_description
    await ctx.send("It's hard to choose which menu you are going to cook!")
    food_list = ['Carbonara', 'Jumbalaya', 'Frittata', 'Creamycodchowderstew']
    food = random.choice(food_list)
    await ctx.send("How about...")
    await ctx.send("a " + food + "?")
    menu_description.insert(0, food)
    await ctx.send("If you want to read a recipe of it, please type \"!yes\"")

@bot.command(name="yes")
async def yes(ctx):
    """gives a recipe for the previous randomly-chosen dish"""

    global recipe
    global menu_description
    await ctx.send(recipe.get(menu_description[0], 'Please type \"!pick\" first '))
    await ctx.send(recipe.get((menu_description[0] + '2'), 'and check out the randomly picked menu!'))
    await ctx.send('Wanna check another menu? Please type \"!pick\" and check out another menu and its recipe!')
    # await ctx.send("and here is the photo of the menu!")
    # await ctx.send(file=discord.File('pasta.jpg'))

@bot.command(name="recipe")
async def how_to_cook(ctx, dish: str):
    """shows the recipe of a specific dish"""

    global recipe
    await ctx.send(dish)
    await ctx.send(recipe.get(dish, 'The recipe for this dish is not available :sweat_smile:'))
    await ctx.send(recipe.get(dish + '2', 'Please visit this chatbot later or try to search different recipe!'))

@bot.command(name="budget")
async def budget(ctx, dollar: float):
    """randomly recommends a food to cook according to the user's budget"""

    budget_under_five = ['Microwave Macaroni and Cheese', 'Cheeseburger Quesadillas', 'Chicken Sandwich', 'Potato Soup', 'Broccoli Rice']
    budget_under_ten = ['Sloppy Joes', 'Philly Cheesesteak Pasta Skillet', 'French Onion Frittata', 'Burrito', 'Tomato Spaghetti', 'Bulgogi']
    budget_under_twenty = ['Caprese Skillet Chicken', 'Ground Turkey Taco Salad', 'Pork Teriyaki Fried Rice', 'Lemon Pepper Chicken', 'Pork Carnitas']
    await ctx.send('It\'s hard to pick a menu by budget.')
    await ctx.send('But...')
    if dollar >= 20:
        await ctx.send(f'{random.choice(budget_under_twenty)}')
    elif dollar >= 10:
        await ctx.send(f'{random.choice(budget_under_ten)}')
    elif dollar >= 5:
        await ctx.send(f'{random.choice(budget_under_five)}')
    await ctx.send('will be a great choice for your budget!')

# make sure to create a token file (in real life use env variables)
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    bot.run(TOKEN)
