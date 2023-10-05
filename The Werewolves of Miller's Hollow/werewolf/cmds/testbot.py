### just for test ###
# discord mods

import discord
from discord.ext import commands

# other mods

# my mods
from core.classes import myCog

class Test(myCog):
    @commands.command()
    async def test1(self, ctx):
        await ctx.send("<@977929252404072458>")
        user = await self.bot.fetch_user(977929252404072458)
        await ctx.send(f"{user.mention}")

async def setup(bot):
    await bot.add_cog(Test(bot))