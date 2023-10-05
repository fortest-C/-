from typing import Literal, Optional
import discord
from discord.ext.commands import Greedy, Context
from discord import app_commands
from discord.ext import commands
import logging
import asyncio

#------ Bot ------
# Can add command_prefix='!', in commands.Bot() for Prefix Commands
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='+/')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}') #Bot Name
    print(bot.user.id)

@bot.command()
async def test1(ctx):
    print('+/test1')
    await ctx.send('+/test1')
#=================================================
class aView(discord.ui.View):
    foo: bool = None

    async def disable_all_items(self):
        for item in self.children:
            item.disable = True
        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send('!timeout')
        await self.disable_all_items()

    @discord.ui.button(label="i am button1",
                       style=discord.ButtonStyle.success)
    async def DoIt(self, interaction: discord.Integration, button: discord.Button):
        print("id",button.custom_id)
        print("labal",button.label)
        print("message",interaction.message)
        await interaction.response.edit_message(embed=discord.Embed(title="i am a Embed" ,description="a embed 2") ,content="i am not sure is this correct")
        self.foo = True
        self.stop()
        for item in  self.children:
            item.disable = True

    @discord.ui.button(label="i am button2",
                       style=discord.ButtonStyle.primary)
    async def DontDoIt(self, interaction: discord.Integration, button: discord.Button):
        print("id",button.custom_id)
        print("labal",button.label)
        print("message",interaction.message)
        await interaction.response.edit_message(embed=discord.Embed(title="i am a Embed" ,description="a embed 3") ,content="i am not sure is this correct")
        self.foo = False
        self.stop()
        for item in  self.children:
            item.disable = True
            
    @discord.ui.button(label="magic!",
                       style=discord.ButtonStyle.secondary)
    async def change(self, interaction: discord.Integration, button: discord.Button):
        view_in_change = discord.ui.View(timeout=3)
        ch_bt = discord.ui.Button(label="i am changed!")
        view_in_change.add_item(ch_bt)
        await interaction.response.edit_message(view=GetBt())
        if not await view_in_change.wait():
            await self.message.channel.send("correct")
        else:
            await self.message.channel.send("oh my")
    
    
@bot.command()
async def button(ctx):
    view = aView(timeout=7)
    embed = discord.Embed(title="i am a ambed", description="a ambed 1")
    view.message = await ctx.send(view=view, embed=embed)

    await view.wait()


    if view.foo is None:
        logging.error('time out!')
    elif view.foo:
        logging.error('Fine')
    else:
        logging.error('Nooo')



class GetBt(discord.ui.View):
    msg: discord.Message = None
    @discord.ui.button(label="Get01")
    async def get01(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            remsg = await self.msg.reply(content="u got it!")
        except:
            pass
        await interaction.response.edit_message(view=aView())
        await asyncio.sleep(3)
        try:
            await remsg.delete()
        except:
            pass

@bot.command()
async def getbt(ctx):
    view = GetBt()
    view.msg = await ctx.send(view=view)

@bot.command()
async def msg(ctx):
    await ctx.send(content="Message" ,ephemeral=True)





bot.run('MTAwOTQ5MzI5MTM5OTY0MzE3OA.GkLSvb.w6vt_aypO_pRhwPwU_EZfqxWyKzoatK7PoOkFs')