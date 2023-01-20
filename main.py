import discord
from discord import app_commands
from discord.ui import Select, View, Button
from discord import components
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import CommandNotFound
from discord.utils import get
from configuration import *
from utils import *
#import asyncio

@client.event
async def on_ready():
    await bot.sync(guild=discord.Object(id=YOUR_GUILD_ID)) # INT TYPE
    print(f"{client.user} has connected to Discord!")


class walletModal(discord.ui.Modal,title="Do not insert private keys or mnemonics!"):
    walletAdd = discord.ui.TextInput(label=f"Enter your public {network_prefix} address",placeholder = f"{network_prefix}3f2sb13h2d1ntj4sm3cal2aznt4dducvv2v3t1b", style=discord.TextStyle.short, required=True, min_length=43, max_length=43)

    async def on_submit(self,interaction:discord.Interaction):
        user_id = interaction.user.id

        resolution = await wallet_reg(user_id,self.walletAdd)
        if resolution == "400":
            await interaction.response.send_message(f"The wallet address `{self.walletAdd}` was saved successfully!",ephemeral = True)
            return
        elif resolution == "402":
            await interaction.response.send_message(f"The wallet address `{self.walletAdd}` was updated successfully!",ephemeral = True)
            return
        elif resolution == "404":
            await interaction.response.send_message(f"The wallet address `{self.walletAdd}` is invalid!",ephemeral = True)
            return
        else:
            return


@bot.command(name="reward",description="Send reward to user's wallet [Owner only]",guild=discord.Object(id=880885156490133514))
async def reward(interaction:discord.Interaction, member: discord.Member,amount:int):
    if interaction.user.id == YOUR_ADMIN_USER_ID:
        member_to_reward = member.id
        if int(amount) <= 0:
            return
        resolution,treasury_balance = await reward_sent_clear(member_to_reward,amount)
        if resolution =="400":
            await interaction.response.send_message(f"<@{member_to_reward}> was airdropped `{amount} ${network_prefix}` :tada:!")
        elif resolution == "405":
            await interaction.response.send_message(f"The treasure does not have enough funds to airdrop {amount} ${network_prefix}. Treasury balance is: `{treasury_balance}{network_prefix}`")
        elif resolution == "406":
            await interaction.response.send_message(f"Error 406 - API might be down, cannot query treasury balance.")
        else:
            return
    else:
        await interaction.response.send_message(f"No permission to use this command.",ephemeral=True)
        

@bot.command(name="wallet",description=f"Complete {network_prefix} wallet address.",guild=discord.Object(id=YOUR_GUILD_ID)) # INT TYPE
async def wallet(interaction):
    await interaction.response.send_modal(walletModal())

client.run(DISCORD_TOKEN)
