import discord
from discord.ext import commands
from discord.ui import Select,View
import asyncio
from datetime import datetime
from core.classes import Cog_Extension



class Myselect(View):
    @discord.ui.select(
        placeholder="Choose an option",
        options=[
            discord.SelectOption(label="Eddd",value='1',description="This"),
            discord.SelectOption(label="Ed",value='2',description="Tis"),
            discord.SelectOption(label="Edd",value='3',description="w")
            ]
    )
    async def select_callback(self,select,interaction):
        select.disabled=True
        if select.values[0]=="1":
            em=discord.Embed()
            em.set_author(name="aaa")
            em.add_field(name="ss",value="sdad",inline=False)
            await interaction.response.edit_message(embed=em)
        if select.values[0]=="2":
            await interaction.response.edit_message(content="edeeE")
        if select.values[0]=="3":
            await interaction.response.send_message("heoo")
class Menu(Cog_Extension):
    @commands.command()
    async def menu(self,ctx):
        view=Myselect()
        await ctx.send("Hellp",view=view)
def setup(bot):
    bot.add_cog(Menu(bot))
